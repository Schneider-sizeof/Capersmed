from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Product
from .forms import ContactForm
from django.utils.translation import gettext as _
from django.utils import translation

def home(request):
    featured_products = Product.objects.filter(is_featured=True)[:3]
    return render(request, 'core/home.html', {'featured_products': featured_products})

def about(request):
    return render(request, 'core/about.html')

def products(request):
    vinegars = Product.objects.filter(category='vinegars')
    pickles = Product.objects.filter(category='pickles')
    spicy = Product.objects.filter(category='spicy')
    
    context = {
        'vinegars': vinegars,
        'pickles': pickles,
        'spicy': spicy
    }
    return render(request, 'core/products.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'core/product_detail.html', {'product': product})

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            # Send email to admin
            send_mail(
                subject=f"New Contact Message from {contact_msg.full_name}",
                message=f"Name: {contact_msg.full_name}\nEmail: {contact_msg.email}\nPhone: {contact_msg.phone}\nMessage:\n{contact_msg.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
            # Send auto-reply
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
