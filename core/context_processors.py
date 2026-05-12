from .models import SiteSettings

def site_settings(request):
    settings = SiteSettings.objects.first()
    if not settings:
        # Provide defaults if not created yet
        settings = SiteSettings(
            site_name='CAPERSMED',
            phone='+212 6 61 48 28 83',
            email='info@capersmed.com',
            address='Hay Namae Bensouda 371/3, Fes 30000, Morocco'
        )
    return {'site_settings': settings}
