from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, BlogPost, Certification
from .forms import ContactForm
from django.utils.translation import gettext as _
from django.utils import translation
from django.urls import reverse
from django.utils.translation import override as lang_override

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
    from django.db.models import Q
    product = get_object_or_404(Product, Q(slug=slug) | Q(slug_fr=slug) | Q(slug_ar=slug) | Q(slug_es=slug) | Q(slug_it=slug) | Q(slug_pt=slug))
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
    from django.db.models import Q
    post = get_object_or_404(BlogPost, Q(slug=slug) | Q(slug_fr=slug) | Q(slug_ar=slug) | Q(slug_es=slug) | Q(slug_it=slug) | Q(slug_pt=slug), is_published=True)
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

def wholesale_export(request):
    return render(request, 'core/wholesale_export.html')

def set_language(request, language_code):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    translation.activate(language_code)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
    return response


def sitemap_xml(request):
    products = Product.objects.all()
    posts = BlogPost.objects.filter(is_published=True)
    base_url = settings.SITE_URL
    languages = [code for code, name in settings.LANGUAGES]
    
    urls = []
    
    # 1. Static Pages
    static_names = ['home', 'products', 'certifications', 'branding', 'blog', 'contact', 'about', 'wholesale_export']
    for name in static_names:
        page_urls = {}
        for lang in languages:
            with lang_override(lang):
                page_urls[lang] = base_url + reverse(name)
        urls.append({
            'loc': page_urls['en'], # default language location is 'en'
            'changefreq': 'weekly' if name == 'home' else 'monthly',
            'priority': '1.0' if name == 'home' else '0.9' if name == 'products' else '0.7',
            'links': [{'lang': lang, 'href': href} for lang, href in page_urls.items()]
        })
        
    # 2. Product Pages
    for product in products:
        page_urls = {}
        for lang in languages:
            slug = getattr(product, f'slug_{lang}', None) or getattr(product, 'slug_en', None) or product.slug
            with lang_override(lang):
                page_urls[lang] = base_url + reverse('product_detail', kwargs={'slug': slug})
        urls.append({
            'loc': page_urls['en'],
            'changefreq': 'monthly',
            'priority': '0.8',
            'links': [{'lang': lang, 'href': href} for lang, href in page_urls.items()]
        })
        
    # 3. Blog Posts
    for post in posts:
        page_urls = {}
        for lang in languages:
            slug = getattr(post, f'slug_{lang}', None) or getattr(post, 'slug_en', None) or post.slug
            with lang_override(lang):
                page_urls[lang] = base_url + reverse('blog_detail', kwargs={'slug': slug})
        urls.append({
            'loc': page_urls['en'],
            'changefreq': 'monthly',
            'priority': '0.6',
            'lastmod': post.updated_at.strftime('%Y-%m-%d') if post.updated_at else None,
            'links': [{'lang': lang, 'href': href} for lang, href in page_urls.items()]
        })
        
    return render(request, 'core/sitemap.xml', {
        'urls': urls,
    }, content_type='application/xml')


def robots_txt(request):
    from urllib.parse import urlparse
    host = urlparse(settings.SITE_URL).netloc.split(':')[0]
    
    request_host = request.get_host()
    is_staging = getattr(settings, 'ROBOTS_DISALLOW_ALL', False) or 'duckdns.org' in request_host or 'pythonanywhere.com' in request_host
    
    base_url = settings.SITE_URL
    return render(request, 'core/robots.txt', {
        'base_url': base_url,
        'is_staging': is_staging,
        'host': host,
    }, content_type='text/plain')

