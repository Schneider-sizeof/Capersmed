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


