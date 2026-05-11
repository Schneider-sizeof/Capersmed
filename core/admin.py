from django import forms
from django.contrib import admin
from .models import Product, ContactMessage, SiteSettings, BlogPost

# ─── Predefined choices ───────────────────────────────────────────────────────

PACKAGING_CHOICES = [
    ('200ml',       '🍶 200ml'),
    ('Pet 200ml',   '🍶 PET 200ml (Plastic Bottle)'),
    ('500ml',       '🍶 500ml'),
    ('2L',          '🪣 2L'),
    ('7L',          '🪣 7L'),
    ('1000L IBC',   '🏭 1000L IBC (Intermediate Bulk Container)'),
    ('200kg',       '🛢️ 200kg Drum'),
]

CERTIFICATION_CHOICES = [
    ('HALAL',  '☪️  HALAL'),
    ('KOSHER', '✡️  KOSHER'),
    ('IFS',    '🏅 IFS Food'),
    ('BRC',    '🏅 BRC Global Standard'),
    ('FDA',    '🇺🇸 FDA — U.S. Food & Drug Administration'),
]


# ─── Custom admin form with checkbox widgets ──────────────────────────────────

class ProductAdminForm(forms.ModelForm):
    packaging_choices = forms.MultipleChoiceField(
        choices=PACKAGING_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Packaging Options',
        help_text='Tick all packaging sizes available for this product.',
    )

    certification_choices = forms.MultipleChoiceField(
        choices=CERTIFICATION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Certifications',
        help_text='Tick all certifications that apply.',
    )

    class Meta:
        model = Product
        exclude = ['packaging', 'certifications']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-populate checkboxes from the JSONField values
        if self.instance and self.instance.pk:
            self.fields['packaging_choices'].initial = self.instance.packaging or []
            self.fields['certification_choices'].initial = self.instance.certifications or []

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Write checkbox selections back to the JSONFields
        instance.packaging = self.cleaned_data.get('packaging_choices', [])
        instance.certifications = self.cleaned_data.get('certification_choices', [])
        if commit:
            instance.save()
        return instance


# ─── Admin classes ────────────────────────────────────────────────────────────

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name_en', 'category', 'is_featured', 'is_premium', 'packaging_summary', 'certifications_summary')
    list_filter = ('category', 'is_featured', 'is_premium')
    prepopulated_fields = {'slug': ('name_en',)}

    fieldsets = (
        ('Basic Info', {
            'fields': ('name_en', 'name_fr', 'name_ar', 'slug', 'category', 'is_featured', 'is_premium', 'image')
        }),
        ('Descriptions', {
            'fields': (
                'short_description_en', 'short_description_fr', 'short_description_ar',
                'description_en', 'description_fr', 'description_ar',
            )
        }),
        ('📦 Packaging Available', {
            'fields': ('packaging_choices',),
        }),
        ('🏅 Certifications', {
            'fields': ('certification_choices',),
        }),
        ('Product Details', {
            'classes': ('collapse',),
            'fields': (
                'features_en', 'features_fr', 'features_ar',
                'uses_en', 'uses_fr', 'uses_ar',
                'specifications_en', 'specifications_fr', 'specifications_ar',
            ),
        }),
    )

    # Helper methods for list_display
    def packaging_summary(self, obj):
        if obj.packaging:
            return ', '.join(obj.packaging[:3]) + ('...' if len(obj.packaging) > 3 else '')
        return '—'
    packaging_summary.short_description = 'Packaging'

    def certifications_summary(self, obj):
        if obj.certifications:
            return ' · '.join(obj.certifications)
        return '—'
    certifications_summary.short_description = 'Certifications'


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
    list_display  = ('title_en', 'category', 'author', 'is_published', 'published_at')
    list_filter   = ('category', 'is_published')
    search_fields = ('title_en', 'title_fr', 'content_en', 'author')
    prepopulated_fields = {'slug': ('title_en',)}
    list_editable = ('is_published',)
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
    )

