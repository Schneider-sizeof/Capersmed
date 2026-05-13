"""Seed products from JSON fixture. Run: python manage.py seed_products"""
import json, os
from django.core.management.base import BaseCommand
from core.models import Product, Preservation, Packaging, Certification

PRESERVATIONS = [
    {'name':'En saumure','name_fr':'En saumure','name_ar':'\u0641\u064a \u0645\u062d\u0644\u0648\u0644 \u0645\u0644\u062d\u064a','name_es':'En salmuera','name_it':'In salamoia'},
    {'name':'En vinaigre','name_fr':'En vinaigre','name_ar':'\u0641\u064a \u0627\u0644\u062e\u0644','name_es':'En vinagre','name_it':'In aceto'},
    {'name':'En sel sec','name_fr':'En sel sec','name_ar':'\u0641\u064a \u0645\u0644\u062d \u062c\u0627\u0641','name_es':'En sal seca','name_it':'In sale secco'},
]
PACKAGINGS = [
    {'name':'Fut 250L','name_fr':'Fût 250L','name_ar':'\u0628\u0631\u0645\u064a\u0644 250 \u0644\u062a\u0631','name_es':'Barril 250L','name_it':'Fusto 250L'},
    {'name':'Fut 65L','name_fr':'Fût 65L','name_ar':'\u0628\u0631\u0645\u064a\u0644 65 \u0644\u062a\u0631','name_es':'Barril 65L','name_it':'Fusto 65L'},
    {'name':'Fut 35L','name_fr':'Fût 35L','name_ar':'\u0628\u0631\u0645\u064a\u0644 35 \u0644\u062a\u0631','name_es':'Barril 35L','name_it':'Fusto 35L'},
    {'name':'Fut 17L','name_fr':'Fût 17L','name_ar':'\u0628\u0631\u0645\u064a\u0644 17 \u0644\u062a\u0631','name_es':'Barril 17L','name_it':'Fusto 17L'},
    {'name':'Seaux a partir de 100ml','name_fr':'Seaux à partir de 100ml','name_ar':'\u062f\u0644\u0627\u0621 \u0627\u0628\u062a\u062f\u0627\u0621\u064b \u0645\u0646 100\u0645\u0644','name_es':'Cubos desde 100ml','name_it':'Secchi da 100ml'},
    {'name':'Bocal','name_fr':'Bocal','name_ar':'\u0628\u0631\u0637\u0645\u0627\u0646','name_es':'Tarro','name_it':'Barattolo'},
    {'name':'Boite metallique','name_fr':'Boîte métallique','name_ar':'\u0639\u0644\u0628\u0629 \u0645\u0639\u062f\u0646\u064a\u0629','name_es':'Lata metálica','name_it':'Scatola metallica'},
    {'name':'Doypack bag','name_fr':'Doypack','name_ar':'\u0643\u064a\u0633 \u062f\u0648\u064a\u0628\u0627\u0643','name_es':'Bolsa Doypack','name_it':'Busta Doypack'},
]
CERTIFICATIONS = [
    ('KOSHER','Kosher Certified','✡️'),
    ('IFS','IFS Food Safety Standard','🏅'),
    ('BRC','BRC Global Standard','🏅'),
    ('FDA','U.S. Food & Drug Administration','🇺🇸'),
]

class Command(BaseCommand):
    help = 'Seed products from JSON fixture'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Preservation.objects.all().delete()
        Packaging.objects.all().delete()
        Certification.objects.all().delete()
        self.stdout.write('Cleared old data.')

        pres_map = {}
        for p in PRESERVATIONS:
            obj, _ = Preservation.objects.get_or_create(name=p['name'], defaults={
                'name_fr':p['name_fr'],'name_ar':p['name_ar'],'name_es':p['name_es'],'name_it':p['name_it']})
            pres_map[p['name']] = obj
        self.stdout.write(f'Created {len(pres_map)} preservation methods.')

        pkg_map = {}
        for p in PACKAGINGS:
            obj, _ = Packaging.objects.get_or_create(name=p['name'], defaults={
                'name_fr':p['name_fr'],'name_ar':p['name_ar'],'name_es':p['name_es'],'name_it':p['name_it']})
            pkg_map[p['name']] = obj
        self.stdout.write(f'Created {len(pkg_map)} packaging options.')

        cert_map = {}
        for code, name, icon in CERTIFICATIONS:
            obj, _ = Certification.objects.get_or_create(code=code, defaults={'name':name,'icon':icon})
            cert_map[code] = obj
        self.stdout.write(f'Created {len(cert_map)} certifications.')

        fixture = os.path.join(os.path.dirname(__file__), '..', '..', 'fixtures', 'products.json')
        with open(fixture, 'r', encoding='utf-8') as f:
            products = json.load(f)

        for p in products:
            product = Product.objects.create(
                name_en=p['name_en'], name_fr=p['name_fr'], name_ar=p['name_ar'],
                name_es=p['name_es'], name_it=p['name_it'],
                slug=p['slug'], category=p['category'],
                is_featured=p.get('is_featured', False),
                short_description_en=p['short_en'], short_description_fr=p['short_fr'],
                short_description_ar=p['short_ar'], short_description_es=p['short_es'],
                short_description_it=p['short_it'],
                description_en=p['desc_en'], description_fr=p['desc_fr'],
                description_ar=p['desc_ar'], description_es=p['desc_es'],
                description_it=p['desc_it'],
                calibers=p.get('calibers', []), grades=p.get('grades', []),
                shelf_life=p.get('shelf_life', ''), storage_conditions=p.get('storage', ''),
                origin=p.get('origin', 'Morocco'),
                image=p.get('image', ''),
            )

            # Set per-product preservation methods
            pres_objs = [pres_map[n] for n in p.get('preservations', []) if n in pres_map]
            product.preservation.set(pres_objs)

            # Set per-product packaging (from fixture, not all)
            pkg_objs = [pkg_map[n] for n in p.get('packaging', []) if n in pkg_map]
            product.packaging.set(pkg_objs)

            # Set per-product certifications (from fixture, not all)
            cert_objs = [cert_map[c] for c in p.get('certifications', []) if c in cert_map]
            product.certifications.set(cert_objs)

            self.stdout.write(f'  [OK] {product.name_en}  '
                              f'[pkg: {len(pkg_objs)}] [cert: {len(cert_objs)}]')

        self.stdout.write(self.style.SUCCESS(f'Created {len(products)} products with individual packaging & certifications.'))
