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
