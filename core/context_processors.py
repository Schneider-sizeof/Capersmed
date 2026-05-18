from django.conf import settings as django_settings
from .models import SiteSettings, HeroMedia

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

    # Build hero media lookup: { 'home': <HeroMedia>, 'about': <HeroMedia>, ... }
    hero_backgrounds = {}
    for hero in HeroMedia.objects.all():
        hero_backgrounds[hero.page] = hero

    return {
        'site_settings': settings,
        'LANGUAGES': django_settings.LANGUAGES,
        'SITE_URL': SITE_URL,
        'hero_backgrounds': hero_backgrounds,
    }

