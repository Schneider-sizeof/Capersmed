from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('set-language/<str:language_code>/', views.set_language, name='set_language'),
]
