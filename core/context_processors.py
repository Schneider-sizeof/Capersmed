from django.conf import settings as django_settings
from .models import SiteSettings

SITE_URL = 'https://www.capersmed.com'

def site_settings(request):
    settings = SiteSettings.objects.first()
    if not settings:
        settings = SiteSettings(
            site_name='CAPERSMED',
            phone='+212 6 61 48 28 83',
            email='capersmed.maroc@gmail.com',
            address='Hay Namae Bensouda 371/3, Fes 30000, Morocco'
        )
    return {
        'site_settings': settings,
        'LANGUAGES': django_settings.LANGUAGES,
        'SITE_URL': SITE_URL,
    }

