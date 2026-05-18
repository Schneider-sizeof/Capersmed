from django.contrib import admin
from .models import (
    Product, ContactMessage, SiteSettings, BlogPost,
    Preservation, Packaging, Certification, HeroMedia,
)


# ─── Lookup models ────────────────────────────────────────────────────────────

@admin.register(Preservation)
class PreservationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'icon', 'image')
    fieldsets = (
        ('Basic', {'fields': ('code', 'name', 'icon', 'image', 'theme_color')}),
        ('English Content', {'fields': ('subtitle_en', 'description_en')}),
        ('French Content', {'fields': ('subtitle_fr', 'description_fr')}),
        ('Arabic Content', {'fields': ('subtitle_ar', 'description_ar')}),
        ('Spanish Content', {'fields': ('subtitle_es', 'description_es')}),
        ('Italian Content', {'fields': ('subtitle_it', 'description_it')}),
    )


# ─── Hero Backgrounds ────────────────────────────────────────────────────────

@admin.register(HeroMedia)
class HeroMediaAdmin(admin.ModelAdmin):
    list_display = ('page', 'media_type', 'image', 'video')
    list_editable = ('media_type',)
    fieldsets = (
        (None, {
            'fields': ('page', 'media_type'),
            'description': 'Select which page and whether to use an image or video.',
        }),
        ('Image Background', {
            'fields': ('image',),
            'description': 'Upload a high-quality background image (JPEG, PNG, WebP). Recommended: 1920x1080 or larger.',
        }),
        ('Video Background', {
            'fields': ('video',),
            'description': 'Upload a background video (MP4 or WebM). The video will autoplay muted in the hero section. Keep file size under 10MB for best performance.',
        }),
    )


# ─── Product ──────────────────────────────────────────────────────────────────

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name_en', 'category', 'is_featured', 'is_premium',
        'packaging_summary', 'certifications_summary',
    )
    list_filter  = ('category', 'is_featured', 'is_premium', 'certifications')
    search_fields = ('name_en', 'name_fr')
    prepopulated_fields = {'slug': ('name_en',)}
    filter_horizontal = ('preservation', 'packaging', 'certifications')

    fieldsets = (
        ('Basic Info', {
            'fields': (
                'name_en', 'name_fr', 'name_ar', 'name_es', 'name_it', 'name_pt',
                'slug', 'category', 'is_featured', 'is_premium', 'image',
            )
        }),
        ('Descriptions', {
            'fields': (
                'short_description_en', 'short_description_fr', 'short_description_ar',
                'short_description_es', 'short_description_it', 'short_description_pt',
                'description_en', 'description_fr', 'description_ar',
                'description_es', 'description_it', 'description_pt',
            )
        }),
        ('🫙 Preservation Methods', {
            'fields': ('preservation',),
        }),
        ('📦 Packaging Available', {
            'fields': ('packaging',),
        }),
        ('🏅 Certifications', {
            'fields': ('certifications',),
        }),
        ('Product Details', {
            'classes': ('collapse',),
            'fields': (
                'features_en', 'features_fr', 'features_ar', 'features_es', 'features_it', 'features_pt',
                'uses_en', 'uses_fr', 'uses_ar', 'uses_es', 'uses_it', 'uses_pt',
                'specifications_en', 'specifications_fr', 'specifications_ar',
                'specifications_es', 'specifications_it', 'specifications_pt',
            ),
        }),
        ('B2B Catalog', {
            'classes': ('collapse',),
            'fields': ('calibre', 'calibers', 'grades', 'shelf_life', 'storage_conditions', 'origin'),
        }),
    )

    def packaging_summary(self, obj):
        items = list(obj.packaging.values_list('name', flat=True)[:3])
        suffix = '…' if obj.packaging.count() > 3 else ''
        return ', '.join(items) + suffix if items else '—'
    packaging_summary.short_description = 'Packaging'

    def certifications_summary(self, obj):
        items = list(obj.certifications.values_list('code', flat=True))
        return ' · '.join(items) if items else '—'
    certifications_summary.short_description = 'Certifications'


# ─── Other models ─────────────────────────────────────────────────────────────

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'company', 'country', 'created_at')
    search_fields = ('full_name', 'email', 'company')
    readonly_fields = ('created_at',)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display   = ('title_en', 'category', 'author', 'is_published', 'published_at')
    list_filter    = ('category', 'is_published')
    search_fields  = ('title_en', 'title_fr', 'content_en', 'author')
    prepopulated_fields = {'slug': ('title_en',)}
    list_editable  = ('is_published',)
    date_hierarchy = 'published_at'

    fieldsets = (
        ('Publication', {
            'fields': ('is_published', 'published_at', 'author', 'category', 'image', 'slug')
        }),
        ('English Content', {
            'fields': ('title_en', 'excerpt_en', 'content_en')
        }),
        ('French Content', {
            'classes': ('collapse',),
            'fields': ('title_fr', 'excerpt_fr', 'content_fr')
        }),
        ('Arabic Content', {
            'classes': ('collapse',),
            'fields': ('title_ar', 'excerpt_ar', 'content_ar')
        }),
        ('Spanish Content', {
            'classes': ('collapse',),
            'fields': ('title_es', 'excerpt_es', 'content_es')
        }),
        ('Italian Content', {
            'classes': ('collapse',),
            'fields': ('title_it', 'excerpt_it', 'content_it')
        }),
        ('Portuguese Content', {
            'classes': ('collapse',),
            'fields': ('title_pt', 'excerpt_pt', 'content_pt')
        }),
    )
