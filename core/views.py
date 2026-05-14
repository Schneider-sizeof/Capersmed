from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, BlogPost, Certification
from .forms import ContactForm
from django.utils.translation import gettext as _
from django.utils import translation

def home(request):
    featured_products = Product.objects.filter(is_featured=True).order_by('id')[:3]
    certs = Certification.objects.all()
    return render(request, 'core/home.html', {
        'featured_products': featured_products,
        'certifications': certs
    })

def about(request):
    return render(request, 'core/about.html')

def products(request):
    all_products = Product.objects.all().order_by('category', 'name_en')
    capers  = all_products.filter(category='capers')
    peppers = all_products.filter(category='peppers')
    pickles = all_products.filter(category='pickles')
    context = {
        'capers': capers,
        'peppers': peppers,
        'pickles': pickles,
        'all_products': all_products,
    }
    return render(request, 'core/products.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'core/product_detail.html', {'product': product})

def certifications(request):
    certs = Certification.objects.all()
    return render(request, 'core/certifications.html', {'certifications': certs})

def blog(request):
    category = request.GET.get('category', '')
    posts = BlogPost.objects.filter(is_published=True)
    if category:
        posts = posts.filter(category=category)
    categories = BlogPost.objects.filter(is_published=True).values_list('category', flat=True).distinct()
    context = {
        'posts': posts,
        'active_category': category,
        'categories': list(categories),
    }
    return render(request, 'core/blog.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related = BlogPost.objects.filter(is_published=True, category=post.category).exclude(pk=post.pk)[:3]
    return render(request, 'core/blog_detail.html', {'post': post, 'related': related})

def branding(request):
    return render(request, 'core/branding.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            send_mail(
                subject=f"New Contact Message from {contact_msg.full_name}",
                message=f"Name: {contact_msg.full_name}\nEmail: {contact_msg.email}\nPhone: {contact_msg.phone}\nMessage:\n{contact_msg.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
            send_mail(
                subject="Thank you for contacting CAPERSMED",
                message="We have received your message and will get back to you shortly.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact_msg.email],
                fail_silently=True,
            )
            messages.success(request, _('Your message has been sent successfully!'))
            return redirect('contact')
        else:
            messages.error(request, _('Please correct the errors below.'))
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def set_language(request, language_code):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    translation.activate(language_code)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
    return response


def sitemap_xml(request):
    products = Product.objects.all()
    posts = BlogPost.objects.filter(is_published=True)
    base_url = 'https://capersmed.pythonanywhere.com'
    static_pages = [
        '',               # home
        'products/',
        'certifications/',
        'branding/',
        'blog/',
        'contact/',
        'about/',
    ]
    return render(request, 'core/sitemap.xml', {
        'products': products,
        'posts': posts,
        'base_url': base_url,
        'static_pages': static_pages,
    }, content_type='application/xml')


def robots_txt(request):
    base_url = request.build_absolute_uri('/').rstrip('/')
    return render(request, 'core/robots.txt', {
        'base_url': base_url,
    }, content_type='text/plain')

