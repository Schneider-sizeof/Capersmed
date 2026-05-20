from django.db import models
from django.utils.text import slugify

CATEGORY_CHOICES = [
    ('capers',  'Capers & Caperberries'),
    ('peppers', 'Peppers & Hot Products'),
    ('pickles', 'Pickled Vegetables & Condiments'),
]


class Preservation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_fr = models.CharField(max_length=100, blank=True, default='')
    name_ar = models.CharField(max_length=100, blank=True, default='')
    name_es = models.CharField(max_length=100, blank=True, default='')
    name_it = models.CharField(max_length=100, blank=True, default='')
    name_pt = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['name']
        verbose_name = 'Preservation Method'
        verbose_name_plural = 'Preservation Methods'

    def __str__(self):
        return self.name


class Packaging(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_fr = models.CharField(max_length=100, blank=True, default='')
    name_ar = models.CharField(max_length=100, blank=True, default='')
    name_es = models.CharField(max_length=100, blank=True, default='')
    name_it = models.CharField(max_length=100, blank=True, default='')
    name_pt = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['name']
        verbose_name = 'Packaging'
        verbose_name_plural = 'Packaging Options'

    def __str__(self):
        return self.name


class Certification(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=10, default='🏅')
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    description_en = models.TextField(blank=True, default='')
    description_fr = models.TextField(blank=True, default='')
    description_ar = models.TextField(blank=True, default='')
    description_es = models.TextField(blank=True, default='')
    description_it = models.TextField(blank=True, default='')
    description_pt = models.TextField(blank=True, default='')
    subtitle_en = models.CharField(max_length=100, blank=True, default='')
    subtitle_fr = models.CharField(max_length=100, blank=True, default='')
    subtitle_ar = models.CharField(max_length=100, blank=True, default='')
    subtitle_es = models.CharField(max_length=100, blank=True, default='')
    subtitle_it = models.CharField(max_length=100, blank=True, default='')
    subtitle_pt = models.CharField(max_length=100, blank=True, default='')
    theme_color = models.CharField(max_length=20, default='#1B4332')

    class Meta:
        ordering = ['code']
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'

    def __str__(self):
        return self.code


class Product(models.Model):
    name_en = models.CharField(max_length=200)
    name_fr = models.CharField(max_length=200, blank=True, default='')
    name_ar = models.CharField(max_length=200, blank=True, default='')
    name_es = models.CharField(max_length=200, blank=True, default='')
    name_it = models.CharField(max_length=200, blank=True, default='')
    name_pt = models.CharField(max_length=200, blank=True, default='')
    slug = models.SlugField(unique=True, blank=True)
    slug_fr = models.SlugField(unique=True, blank=True, null=True, max_length=260)
    slug_ar = models.SlugField(unique=True, blank=True, null=True, max_length=260, allow_unicode=True)
    slug_es = models.SlugField(unique=True, blank=True, null=True, max_length=260)
    slug_it = models.SlugField(unique=True, blank=True, null=True, max_length=260)
    slug_pt = models.SlugField(unique=True, blank=True, null=True, max_length=260)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    is_premium = models.BooleanField(default=False)

    short_description_en = models.CharField(max_length=300, blank=True, default='')
    short_description_fr = models.CharField(max_length=300, blank=True, default='')
    short_description_ar = models.CharField(max_length=300, blank=True, default='')
    short_description_es = models.CharField(max_length=300, blank=True, default='')
    short_description_it = models.CharField(max_length=300, blank=True, default='')
    short_description_pt = models.CharField(max_length=300, blank=True, default='')

    description_en = models.TextField(blank=True, default='')
    description_fr = models.TextField(blank=True, default='')
    description_ar = models.TextField(blank=True, default='')
    description_es = models.TextField(blank=True, default='')
    description_it = models.TextField(blank=True, default='')
    description_pt = models.TextField(blank=True, default='')

    features_en = models.JSONField(default=list, blank=True)
    features_fr = models.JSONField(default=list, blank=True)
    features_ar = models.JSONField(default=list, blank=True)
    features_es = models.JSONField(default=list, blank=True)
    features_it = models.JSONField(default=list, blank=True)
    features_pt = models.JSONField(default=list, blank=True)

    uses_en = models.JSONField(default=list, blank=True)
    uses_fr = models.JSONField(default=list, blank=True)
    uses_ar = models.JSONField(default=list, blank=True)
    uses_es = models.JSONField(default=list, blank=True)
    uses_it = models.JSONField(default=list, blank=True)
    uses_pt = models.JSONField(default=list, blank=True)

    specifications_en = models.JSONField(default=dict, blank=True)
    specifications_fr = models.JSONField(default=dict, blank=True)
    specifications_ar = models.JSONField(default=dict, blank=True)
    specifications_es = models.JSONField(default=dict, blank=True)
    specifications_it = models.JSONField(default=dict, blank=True)
    specifications_pt = models.JSONField(default=dict, blank=True)

    # B2B catalog fields
    calibre = models.CharField(max_length=100, blank=True, null=True, default=None, help_text='Product calibre e.g. "7/8", "8/9", "9/11", "11/13", "13+"')
    calibers = models.JSONField(default=list, blank=True, help_text='Available calibers e.g. [1, 2, 3]')
    grades = models.JSONField(default=list, blank=True, help_text='Available grades e.g. ["A","B","C","D","E"]')
    shelf_life = models.CharField(max_length=100, blank=True, default='')
    storage_conditions = models.CharField(max_length=200, blank=True, default='')
    origin = models.CharField(max_length=100, blank=True, default='Morocco')

    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    preservation   = models.ManyToManyField(Preservation,   blank=True, related_name='products')
    packaging      = models.ManyToManyField(Packaging,      blank=True, related_name='products')
    certifications = models.ManyToManyField(Certification,  blank=True, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)
        if self.name_fr and not self.slug_fr:
            self.slug_fr = slugify(self.name_fr)
        if self.name_es and not self.slug_es:
            self.slug_es = slugify(self.name_es)
        if self.name_it and not self.slug_it:
            self.slug_it = slugify(self.name_it)
        if self.name_pt and not self.slug_pt:
            self.slug_pt = slugify(self.name_pt)
        if self.name_ar and not self.slug_ar:
            self.slug_ar = slugify(self.name_ar, allow_unicode=True)
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
    email = models.EmailField(default='export@capersmed.com')
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


HERO_PAGE_CHOICES = [
    ('home',           'Homepage'),
    ('about',          'About Us'),
    ('products',       'Products'),
    ('certifications', 'Certifications'),
    ('blog',           'Blog'),
    ('branding',       'Branding'),
    ('contact',        'Contact'),
    ('services',       'Services'),
]


class HeroMedia(models.Model):
    page = models.CharField(max_length=50, choices=HERO_PAGE_CHOICES, unique=True,
                            help_text='Which page this hero background is for.')
    media_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')], default='image')
    image = models.ImageField(upload_to='backgrounds/', blank=True, null=True,
                              help_text='Upload a hero background image (JPEG, PNG, WebP).')
    video = models.FileField(upload_to='backgrounds/videos/', blank=True, null=True,
                             help_text='Upload a hero background video (MP4, WebM). Used only when media type is Video.')

    class Meta:
        verbose_name = 'Hero Background'
        verbose_name_plural = 'Hero Backgrounds'
        ordering = ['page']

    def __str__(self):
        return f"Hero — {self.get_page_display()}"


BLOG_CATEGORY_CHOICES = [
    ('news',     'Company News'),
    ('industry', 'Industry Insights'),
    ('recipes',  'Recipes & Uses'),
    ('export',   'Export & Trade'),
    ('products', 'Product Spotlight'),
]


class BlogPost(models.Model):
    title_en = models.CharField(max_length=250)
    title_fr = models.CharField(max_length=250, blank=True)
    title_ar = models.CharField(max_length=250, blank=True)
    title_es = models.CharField(max_length=250, blank=True)
    title_it = models.CharField(max_length=250, blank=True)
    title_pt = models.CharField(max_length=250, blank=True)

    slug = models.SlugField(unique=True, blank=True, max_length=260)
    slug_fr = models.SlugField(unique=True, blank=True, null=True, max_length=260)
    slug_ar = models.SlugField(unique=True, blank=True, null=True, max_length=260, allow_unicode=True)
    slug_es = models.SlugField(unique=True, blank=True, null=True, max_length=260)
    slug_it = models.SlugField(unique=True, blank=True, null=True, max_length=260)
    slug_pt = models.SlugField(unique=True, blank=True, null=True, max_length=260)
    category = models.CharField(max_length=50, choices=BLOG_CATEGORY_CHOICES, default='news')

    excerpt_en = models.TextField(max_length=400, blank=True)
    excerpt_fr = models.TextField(max_length=400, blank=True)
    excerpt_ar = models.TextField(max_length=400, blank=True)
    excerpt_es = models.TextField(max_length=400, blank=True)
    excerpt_it = models.TextField(max_length=400, blank=True)
    excerpt_pt = models.TextField(max_length=400, blank=True)

    content_en = models.TextField()
    content_fr = models.TextField(blank=True)
    content_ar = models.TextField(blank=True)
    content_es = models.TextField(blank=True)
    content_it = models.TextField(blank=True)
    content_pt = models.TextField(blank=True)

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
        if self.title_fr and not self.slug_fr:
            self.slug_fr = slugify(self.title_fr)
        if self.title_es and not self.slug_es:
            self.slug_es = slugify(self.title_es)
        if self.title_it and not self.slug_it:
            self.slug_it = slugify(self.title_it)
        if self.title_pt and not self.slug_pt:
            self.slug_pt = slugify(self.title_pt)
        if self.title_ar and not self.slug_ar:
            self.slug_ar = slugify(self.title_ar, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en
