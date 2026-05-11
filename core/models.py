from django.db import models
from django.utils.text import slugify

CATEGORY_CHOICES = [
    ('vinegars', 'Premium Vinegars'),
    ('pickles', 'Pickled Vegetables & Condiments'),
    ('spicy', 'Hot & Spicy'),
]

class Product(models.Model):
    name_en = models.CharField(max_length=200)
    name_fr = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    is_premium = models.BooleanField(default=False)
    
    short_description_en = models.CharField(max_length=300, default='')
    short_description_fr = models.CharField(max_length=300, default='')
    short_description_ar = models.CharField(max_length=300, default='')
    
    description_en = models.TextField()
    description_fr = models.TextField()
    description_ar = models.TextField()
    
    features_en = models.JSONField(default=list)
    features_fr = models.JSONField(default=list)
    features_ar = models.JSONField(default=list)
    
    uses_en = models.JSONField(default=list)
    uses_fr = models.JSONField(default=list)
    uses_ar = models.JSONField(default=list)
    
    specifications_en = models.JSONField(default=dict)
    specifications_fr = models.JSONField(default=dict)
    specifications_ar = models.JSONField(default=dict)
    
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    # Packaging: list of size strings, e.g. ["370g Jar", "720g Jar", "5L Bulk"]
    packaging = models.JSONField(default=list, blank=True)
    # Certifications: list of codes, e.g. ["ISO22000", "HACCP", "HALAL", "FDA", "EU", "BIO"]
    certifications = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_en

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    wholesale_interest = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name}"

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default='CAPERSMED')
    phone = models.CharField(max_length=50, default='+212 6 61 48 28 83')
    email = models.EmailField(default='info@capersmed.com')
    address = models.TextField(default='Hay Namae Bensouda 371/3, Fes 30000, Morocco')
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    google_analytics_id = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name


BLOG_CATEGORY_CHOICES = [
    ('news',     'Company News'),
    ('industry', 'Industry Insights'),
    ('recipes',  'Recipes & Uses'),
    ('export',   'Export & Trade'),
    ('products', 'Product Spotlight'),
]

class BlogPost(models.Model):
    # Multilingual titles
    title_en = models.CharField(max_length=250)
    title_fr = models.CharField(max_length=250, blank=True)
    title_ar = models.CharField(max_length=250, blank=True)

    slug = models.SlugField(unique=True, blank=True, max_length=260)
    category = models.CharField(max_length=50, choices=BLOG_CATEGORY_CHOICES, default='news')

    # Excerpts
    excerpt_en = models.TextField(max_length=400, blank=True)
    excerpt_fr = models.TextField(max_length=400, blank=True)
    excerpt_ar = models.TextField(max_length=400, blank=True)

    # Full content
    content_en = models.TextField()
    content_fr = models.TextField(blank=True)
    content_ar = models.TextField(blank=True)

    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.CharField(max_length=100, default='CAPERSMED Team')

    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en

