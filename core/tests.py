from django.test import TestCase, override_settings
from django.urls import reverse
from django.conf import settings

class SEOTestCase(TestCase):

    @override_settings(SITE_URL='https://www.capersmed.com', ENABLE_DOMAIN_REDIRECT=True)
    def test_domain_redirect_middleware_active(self):
        # Request with a non-canonical host should redirect to the canonical host
        response = self.client.get('/', HTTP_HOST='capersmed.duckdns.org')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], 'https://www.capersmed.com/')

        # Request with a non-canonical host and a path should keep the path
        response = self.client.get('/en/products/', HTTP_HOST='capersmed.com')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], 'https://www.capersmed.com/en/products/')

        # Request with canonical host and correct scheme should not redirect
        response = self.client.get('/en/', HTTP_HOST='www.capersmed.com', secure=True)
        self.assertEqual(response.status_code, 200)

    @override_settings(SITE_URL='https://www.capersmed.com', ENABLE_DOMAIN_REDIRECT=False)
    def test_domain_redirect_middleware_inactive(self):
        # When redirect is disabled, it should not redirect non-canonical hosts
        response = self.client.get('/en/', HTTP_HOST='capersmed.duckdns.org')
        self.assertEqual(response.status_code, 200)

    @override_settings(SITE_URL='https://staging.capersmed.com')
    def test_sitemap_uses_site_url(self):
        from core.models import Product, BlogPost
        Product.objects.create(name_en="Test Product", slug="test-product", category="capers")
        BlogPost.objects.create(title_en="Test Post", slug="test-post", content_en="Content", is_published=True)

        response = self.client.get(reverse('sitemap'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'https://staging.capersmed.com/en/')
        self.assertContains(response, 'https://staging.capersmed.com/en/products/test-product/')
        self.assertContains(response, 'https://staging.capersmed.com/en/blog/test-post/')

    @override_settings(SITE_URL='https://www.capersmed.com', ROBOTS_DISALLOW_ALL=True)
    def test_robots_txt_disallow_all(self):
        response = self.client.get(reverse('robots'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Disallow: /')
        self.assertNotContains(response, 'Allow: /')

    @override_settings(SITE_URL='https://www.capersmed.com', ROBOTS_DISALLOW_ALL=False)
    def test_robots_txt_allow_production(self):
        response = self.client.get(reverse('robots'), HTTP_HOST='www.capersmed.com')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Allow: /')
        self.assertContains(response, 'Host: www.capersmed.com')

    def test_canonical_and_hreflang_encoding(self):
        # Visit the Arabic products page (Unicode URL resolved to /ar/%D8%A7%D9%84%D9%85%D9%86%D8%AA%D8%AC%D8%A7%D8%AA/)
        # This will render base.html where we check that canonical and hreflang tags match and are URL-encoded.
        from django.utils.translation import override as lang_override
        with lang_override('ar'):
            ar_products_path = reverse('products') # returns /ar/%D8%A7%D9%84%D9%85%D9%86%D8%AA%D8%AC%D8%A7%D8%AA/
        
        response = self.client.get(ar_products_path)
        self.assertEqual(response.status_code, 200)
        
        # Verify that the canonical link has the URL-encoded path, not the raw Unicode path
        expected_canonical = f'https://www.capersmed.com{ar_products_path}'
        self.assertContains(response, f'<link rel="canonical" href="{expected_canonical}">', html=True)
        
        # Verify that the hreflang link for Arabic matches the canonical link exactly
        self.assertContains(response, f'<link rel="alternate" hreflang="ar" href="{expected_canonical}">', html=True)

        # 2. Test with a decoded path (simulating a standard WSGI environment where request.path has decoded Unicode)
        response_decoded = self.client.get('/ar/المنتجات/')
        self.assertEqual(response_decoded.status_code, 200)
        
        # Verify that both the canonical and the alternate tags remain perfectly URL-encoded and identical
        self.assertContains(response_decoded, f'<link rel="canonical" href="{expected_canonical}">', html=True)
        self.assertContains(response_decoded, f'<link rel="alternate" hreflang="ar" href="{expected_canonical}">', html=True)



