from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(_('about/'), views.about, name='about'),
    path(_('products/'), views.products, name='products'),
    path(_('products/<slug:slug>/'), views.product_detail, name='product_detail'),
    path(_('certifications/'), views.certifications, name='certifications'),
    path(_('blog/'), views.blog, name='blog'),
    path(_('blog/<slug:slug>/'), views.blog_detail, name='blog_detail'),
    path(_('branding/'), views.branding, name='branding'),
    path(_('services/'), views.services, name='services'),
    path(_('contact/'), views.contact, name='contact'),
    path('set-language/<str:language_code>/', views.set_language, name='set_language'),
]
