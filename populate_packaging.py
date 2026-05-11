import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capersmed.settings')
import django
django.setup()

from core.models import Product

data = {
    'moroccan-capers':  (['106g Jar', '370g Jar', '720g Jar', '5L Bulk'],       ['ISO22000', 'HACCP', 'HALAL', 'EU']),
    'caperberries':     (['106g Jar', '370g Jar', '720g Jar', '3L Bulk'],        ['ISO22000', 'HACCP', 'HALAL', 'EU']),
    'lampascioni':      (['106g Jar', '370g Jar', '720g Jar', '3L Bulk'],        ['ISO22000', 'HACCP', 'HALAL']),
    'citrons-confits':  (['370g Jar', '720g Jar', '5L Bulk'],                    ['ISO22000', 'HACCP', 'HALAL']),
    'oignons-blancs':   (['106g Jar', '370g Jar', '720g Jar'],                   ['ISO22000', 'HACCP', 'HALAL']),
    'cornichons':       (['106g Jar', '370g Jar', '720g Jar', '3L Bulk'],        ['ISO22000', 'HACCP', 'HALAL']),
    'apple-cider-vinegar': (['250ml Bottle', '500ml Bottle', '1L Bottle', '5L Bulk'], ['ISO22000', 'HACCP', 'HALAL', 'BIO']),
    'red-wine-vinegar': (['250ml Bottle', '500ml Bottle', '1L Bottle'],          ['ISO22000', 'HACCP', 'HALAL']),
    'white-wine-vinegar': (['250ml Bottle', '500ml Bottle', '1L Bottle'],        ['ISO22000', 'HACCP', 'HALAL']),
    'moroccan-harissa': (['106g Jar', '370g Jar', '720g Jar'],                   ['ISO22000', 'HACCP', 'HALAL']),
    'piri-piri-peppers': (['106g Jar', '370g Jar'],                              ['ISO22000', 'HACCP', 'HALAL']),
    'piparra-peppers':  (['106g Jar', '370g Jar', '720g Jar'],                   ['ISO22000', 'HACCP', 'HALAL']),
}

updated = 0
for slug, (packaging, certs) in data.items():
    try:
        p = Product.objects.get(slug=slug)
        p.packaging = packaging
        p.certifications = certs
        p.save()
        print("  [OK] " + p.name_en)
        updated += 1
    except Product.DoesNotExist:
        print("  [MISS] " + slug)

print("Done! Updated " + str(updated) + " products.")
