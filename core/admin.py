from django.contrib import admin
from .models import Product, ContactMessage, SiteSettings

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('name_en', 'name_fr', 'name_ar')
    prepopulated_fields = {'slug': ('name_en',)}

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'wholesale_interest', 'created_at')
    list_filter = ('wholesale_interest', 'created_at')
    search_fields = ('full_name', 'email', 'company')
    readonly_fields = ('created_at',)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)
