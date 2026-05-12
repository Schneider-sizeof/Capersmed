"""
Management command: seed preservation, packaging, certifications, and products.
Run:  python manage.py seed_products
"""
from django.core.management.base import BaseCommand
from core.models import Product, Preservation, Packaging, Certification


PRESERVATIONS = [
    'En saumure',
    'En vinaigre',
    'En sel sec',
]

PACKAGINGS = [
    'Fut 250L',
    'Fut 65L',
    'Fut 35L',
    'Fut 17L',
    'Seaux a partir de 100ml',
    'Bocal',
    'Boite metallique',
    'Doypack bag',
]

CERTIFICATIONS = [
    ('KOSHER', 'Kosher Certified',                     '\u2721\ufe0f'),
    ('IFS',    'IFS Food Safety Standard',             '\U0001F3C5'),
    ('BRC',    'BRC Global Standard',                  '\U0001F3C5'),
    ('FDA',    'U.S. Food & Drug Administration',      '\U0001f1fa\U0001f1f8'),
]

PRODUCTS = [
    {
        'name_en': 'Capers',
        'name_fr': 'Capres',
        'name_ar': '\u0643\u0628\u0627\u0631',
        'slug': 'capers',
        'category': 'capers',
        'is_featured': True,
        'short_en': 'Premium hand-picked Moroccan capers, cured to perfection.',
        'short_fr': 'Capres marocaines cueillies a la main, affinees a la perfection.',
        'short_ar': '\u0643\u0628\u0627\u0631 \u0645\u063a\u0631\u0628\u064a \u0645\u0642\u0637\u0648\u0641 \u064a\u062f\u0648\u064a\u0627\u064b',
        'desc_en': 'Hand-picked Moroccan capers sorted by calibre. Available in brine, vinegar, or dry salt preservation.',
        'desc_fr': 'Capres marocaines cueillies a la main, triees par calibre. Disponibles en saumure, vinaigre ou sel sec.',
        'desc_ar': '\u0643\u0628\u0627\u0631 \u0645\u063a\u0631\u0628\u064a \u0645\u0642\u0637\u0648\u0641 \u064a\u062f\u0648\u064a\u0627\u064b \u0648\u0645\u0635\u0646\u0641 \u062d\u0633\u0628 \u0627\u0644\u062d\u062c\u0645.',
        'preservations': ['En saumure', 'En vinaigre', 'En sel sec'],
    },
    {
        'name_en': 'Caperberries',
        'name_fr': 'Caprons',
        'name_ar': '\u062b\u0645\u0627\u0631 \u0627\u0644\u0643\u0628\u0627\u0631',
        'slug': 'caperberries',
        'category': 'capers',
        'is_featured': True,
        'short_en': 'Moroccan caperberries with a mild, olive-like flavour.',
        'short_fr': 'Caprons marocains a la saveur douce ressemblant a l\'olive.',
        'short_ar': '\u062b\u0645\u0627\u0631 \u0627\u0644\u0643\u0628\u0627\u0631 \u0627\u0644\u0645\u063a\u0631\u0628\u064a\u0629 \u0628\u0646\u0643\u0647\u0629 \u062e\u0641\u064a\u0641\u0629',
        'desc_en': 'Caperberries with stems, ideal for tapas, cocktails, and gourmet garnishes.',
        'desc_fr': 'Caprons avec tiges, ideals pour les tapas, cocktails et garnitures gastronomiques.',
        'desc_ar': '\u062b\u0645\u0627\u0631 \u0627\u0644\u0643\u0628\u0627\u0631 \u0628\u0627\u0644\u0633\u064a\u0642\u0627\u0646\u060c \u0645\u062b\u0627\u0644\u064a\u0629 \u0644\u0644\u0645\u0642\u0628\u0644\u0627\u062a.',
        'preservations': ['En saumure', 'En vinaigre'],
    },
    {
        'name_en': 'Hot Peppers',
        'name_fr': 'Les piments',
        'name_ar': '\u0627\u0644\u0641\u0644\u0641\u0644 \u0627\u0644\u062d\u0627\u0631',
        'slug': 'hot-peppers',
        'category': 'peppers',
        'is_featured': False,
        'short_en': 'Assorted hot peppers preserved in brine or vinegar.',
        'short_fr': 'Assortiment de piments conserves en saumure ou vinaigre.',
        'short_ar': '\u062a\u0634\u0643\u064a\u0644\u0629 \u0641\u0644\u0641\u0644 \u062d\u0627\u0631 \u0645\u062d\u0641\u0648\u0638 \u0641\u064a \u0627\u0644\u0645\u0644\u062d \u0623\u0648 \u0627\u0644\u062e\u0644.',
        'desc_en': 'A variety of hot peppers, preserved to retain their natural heat and flavour.',
        'desc_fr': 'Une variete de piments, conserves pour garder leur chaleur et saveur naturelles.',
        'desc_ar': '\u062a\u0634\u0643\u064a\u0644\u0629 \u0645\u0646 \u0627\u0644\u0641\u0644\u0641\u0644 \u0627\u0644\u062d\u0627\u0631.',
        'preservations': ['En saumure', 'En vinaigre'],
    },
    {
        'name_en': 'Piri Piri',
        'name_fr': 'Piri piri',
        'name_ar': '\u0628\u064a\u0631\u064a \u0628\u064a\u0631\u064a',
        'slug': 'piri-piri',
        'category': 'peppers',
        'is_featured': True,
        'short_en': 'Small, fiery Piri-Piri peppers packed in vinegar.',
        'short_fr': 'Petits piments Piri-Piri ardents conserves dans le vinaigre.',
        'short_ar': '\u0641\u0644\u0641\u0644 \u0628\u064a\u0631\u064a \u0628\u064a\u0631\u064a \u0635\u063a\u064a\u0631 \u0648\u062d\u0627\u0631.',
        'desc_en': 'Fiery Piri-Piri peppers, a staple in African and Portuguese cuisines.',
        'desc_fr': 'Piments Piri-Piri ardents, un incontournable de la cuisine africaine et portugaise.',
        'desc_ar': '\u0641\u0644\u0641\u0644 \u0628\u064a\u0631\u064a \u0628\u064a\u0631\u064a \u0627\u0644\u062d\u0627\u0631.',
        'preservations': ['En saumure', 'En vinaigre'],
    },
    {
        'name_en': 'Piparra',
        'name_fr': 'Piparra',
        'name_ar': '\u0628\u064a\u0628\u0627\u0631\u0627',
        'slug': 'piparra',
        'category': 'peppers',
        'is_featured': False,
        'short_en': 'Mild Basque peppers, tangy and crisp.',
        'short_fr': 'Piments basques doux, acidules et croquants.',
        'short_ar': '\u0641\u0644\u0641\u0644 \u0627\u0644\u0628\u0627\u0633\u0643 \u0627\u0644\u062e\u0641\u064a\u0641.',
        'desc_en': 'Pickled Basque peppers, mild and tangy — a tapas essential.',
        'desc_fr': 'Piments basques marines, doux et acidules, essentiels pour les tapas.',
        'desc_ar': '\u0641\u0644\u0641\u0644 \u0627\u0644\u0628\u0627\u0633\u0643 \u0627\u0644\u0645\u062e\u0644\u0644.',
        'preservations': ['En vinaigre'],
    },
    {
        'name_en': 'Guindilla',
        'name_fr': 'Guindilla',
        'name_ar': '\u063a\u064a\u0646\u062f\u064a\u0644\u0627',
        'slug': 'guindilla',
        'category': 'peppers',
        'is_featured': False,
        'short_en': 'Spanish Guindilla peppers, mildly spicy.',
        'short_fr': 'Piments Guindilla espagnols, legerement epices.',
        'short_ar': '\u0641\u0644\u0641\u0644 \u063a\u064a\u0646\u062f\u064a\u0644\u0627 \u0627\u0644\u0625\u0633\u0628\u0627\u0646\u064a.',
        'desc_en': 'Mildly spicy Guindilla peppers, perfect with pintxos and grilled dishes.',
        'desc_fr': 'Piments Guindilla legerement epices, parfaits avec les pintxos et les grillades.',
        'desc_ar': '\u0641\u0644\u0641\u0644 \u063a\u064a\u0646\u062f\u064a\u0644\u0627 \u0645\u0639\u062a\u062f\u0644 \u0627\u0644\u062d\u0631\u0627\u0631\u0629.',
        'preservations': ['En vinaigre'],
    },
    {
        'name_en': 'Cut Red/Yellow/Green Peppers',
        'name_fr': 'Piment rouge/jaune/vert coupe',
        'name_ar': '\u0641\u0644\u0641\u0644 \u0623\u062d\u0645\u0631/\u0623\u0635\u0641\u0631/\u0623\u062e\u0636\u0631 \u0645\u0642\u0637\u0639',
        'slug': 'cut-peppers',
        'category': 'peppers',
        'is_featured': False,
        'short_en': 'Tri-colour cut peppers preserved in brine or vinegar.',
        'short_fr': 'Piments tricolores coupes, conserves en saumure ou vinaigre.',
        'short_ar': '\u0641\u0644\u0641\u0644 \u0645\u0642\u0637\u0639 \u062b\u0644\u0627\u062b\u064a \u0627\u0644\u0623\u0644\u0648\u0627\u0646.',
        'desc_en': 'Pre-cut red, yellow, and green peppers, ready for industrial and food-service use.',
        'desc_fr': 'Piments rouges, jaunes et verts pre-coupes, prets pour l\'industrie et la restauration.',
        'desc_ar': '\u0641\u0644\u0641\u0644 \u0623\u062d\u0645\u0631 \u0648\u0623\u0635\u0641\u0631 \u0648\u0623\u062e\u0636\u0631 \u0645\u0642\u0637\u0639 \u0645\u0633\u0628\u0642\u0627\u064b.',
        'preservations': ['En saumure', 'En vinaigre'],
    },
    {
        'name_en': 'Harissa',
        'name_fr': 'Harissa',
        'name_ar': '\u0647\u0631\u064a\u0633\u0629',
        'slug': 'harissa',
        'category': 'peppers',
        'is_featured': True,
        'short_en': 'Authentic North-African hot chili paste.',
        'short_fr': 'Pate de piment fort nord-africaine authentique.',
        'short_ar': '\u0645\u0639\u062c\u0648\u0646 \u0627\u0644\u0641\u0644\u0641\u0644 \u0627\u0644\u062d\u0627\u0631 \u0627\u0644\u0623\u0635\u064a\u0644.',
        'desc_en': 'Traditional harissa paste, a versatile condiment for marinades, couscous, and grills.',
        'desc_fr': 'Pate de harissa traditionnelle, condiment polyvalent pour marinades, couscous et grillades.',
        'desc_ar': '\u0645\u0639\u062c\u0648\u0646 \u0627\u0644\u0647\u0631\u064a\u0633\u0629 \u0627\u0644\u062a\u0642\u0644\u064a\u062f\u064a.',
        'preservations': [],
    },
    {
        'name_en': 'Preserved Lemons',
        'name_fr': 'Citron confit',
        'name_ar': '\u0644\u064a\u0645\u0648\u0646 \u0645\u062e\u0644\u0644',
        'slug': 'preserved-lemons',
        'category': 'pickles',
        'is_featured': True,
        'short_en': 'Salt-preserved lemons, essential for Moroccan tagines.',
        'short_fr': 'Citrons confits au sel, essentiels pour les tajines marocains.',
        'short_ar': '\u0644\u064a\u0645\u0648\u0646 \u0645\u062e\u0644\u0644 \u0628\u0627\u0644\u0645\u0644\u062d.',
        'desc_en': 'Whole lemons cured in salt, a cornerstone of Moroccan and Mediterranean cooking.',
        'desc_fr': 'Citrons entiers confits au sel, un pilier de la cuisine marocaine et mediterraneenne.',
        'desc_ar': '\u0644\u064a\u0645\u0648\u0646 \u0643\u0627\u0645\u0644 \u0645\u062e\u0644\u0644 \u0628\u0627\u0644\u0645\u0644\u062d.',
        'preservations': ['En saumure', 'En sel sec'],
    },
    {
        'name_en': 'Pearl / Silver / Silverskin Onions',
        'name_fr': 'Oignon pearl / silver / Silverskin onions',
        'name_ar': '\u0628\u0635\u0644 \u0644\u0624\u0644\u0624\u064a / \u0641\u0636\u064a',
        'slug': 'pearl-silver-onions',
        'category': 'pickles',
        'is_featured': False,
        'short_en': 'Small pickled onions, crisp and tangy.',
        'short_fr': 'Petits oignons marines, croquants et acidules.',
        'short_ar': '\u0628\u0635\u0644 \u0635\u063a\u064a\u0631 \u0645\u062e\u0644\u0644.',
        'desc_en': 'Pearl and silverskin onions, pickled for charcuterie boards, salads, and garnishes.',
        'desc_fr': 'Oignons grelots et silverskin marines pour planches de charcuterie, salades et garnitures.',
        'desc_ar': '\u0628\u0635\u0644 \u0644\u0624\u0644\u0624\u064a \u0645\u062e\u0644\u0644 \u0644\u0644\u0633\u0644\u0637\u0627\u062a \u0648\u0627\u0644\u0645\u0642\u0628\u0644\u0627\u062a.',
        'preservations': ['En vinaigre'],
    },
    {
        'name_en': 'Lampascioni',
        'name_fr': 'Lampascioni',
        'name_ar': '\u0644\u0645\u0628\u0627\u0633\u0643\u064a\u0648\u0646\u064a',
        'slug': 'lampascioni',
        'category': 'pickles',
        'is_featured': False,
        'short_en': 'Pickled Mediterranean wild onions for antipasto.',
        'short_fr': 'Oignons sauvages mediterraneens marines pour antipasti.',
        'short_ar': '\u0628\u0635\u0644 \u0628\u0631\u064a \u0645\u062a\u0648\u0633\u0637\u064a \u0645\u062e\u0644\u0644.',
        'desc_en': 'Wild Mediterranean onion bulbs, pickled in vinegar. A southern-Italian delicacy.',
        'desc_fr': 'Bulbes d\'oignons sauvages mediterraneens, marines au vinaigre. Delicatesse du sud de l\'Italie.',
        'desc_ar': '\u0628\u0635\u0644 \u0628\u0631\u064a \u0645\u062a\u0648\u0633\u0637\u064a \u0645\u062e\u0644\u0644 \u0641\u064a \u0627\u0644\u062e\u0644.',
        'preservations': ['En vinaigre'],
    },
    {
        'name_en': 'Cornichons',
        'name_fr': 'Cornichons',
        'name_ar': '\u0643\u0648\u0631\u0646\u064a\u0634\u0648\u0646',
        'slug': 'cornichons',
        'category': 'pickles',
        'is_featured': False,
        'short_en': 'French-style gherkins, crisp and tart.',
        'short_fr': 'Cornichons a la francaise, croquants et acidules.',
        'short_ar': '\u0643\u0648\u0631\u0646\u064a\u0634\u0648\u0646 \u0641\u0631\u0646\u0633\u064a.',
        'desc_en': 'Classic French-style cornichons, the ideal accompaniment for pates and charcuterie.',
        'desc_fr': 'Cornichons classiques a la francaise, accompagnement ideal pour pates et charcuterie.',
        'desc_ar': '\u0643\u0648\u0631\u0646\u064a\u0634\u0648\u0646 \u0643\u0644\u0627\u0633\u064a\u0643\u064a.',
        'preservations': ['En vinaigre'],
    },
]


class Command(BaseCommand):
    help = 'Seed preservation methods, packaging, certifications and products.'

    def handle(self, *args, **options):
        # Delete old data
        Product.objects.all().delete()
        Preservation.objects.all().delete()
        Packaging.objects.all().delete()
        Certification.objects.all().delete()
        self.stdout.write('Cleared old data.')

        # Create preservation methods
        pres_map = {}
        for name in PRESERVATIONS:
            obj, _ = Preservation.objects.get_or_create(name=name)
            pres_map[name] = obj
        self.stdout.write(f'Created {len(pres_map)} preservation methods.')

        # Create packaging options
        pkg_map = {}
        for name in PACKAGINGS:
            obj, _ = Packaging.objects.get_or_create(name=name)
            pkg_map[name] = obj
        self.stdout.write(f'Created {len(pkg_map)} packaging options.')

        # Create certifications
        cert_map = {}
        for code, name, icon in CERTIFICATIONS:
            obj, _ = Certification.objects.get_or_create(
                code=code, defaults={'name': name, 'icon': icon}
            )
            cert_map[code] = obj
        self.stdout.write(f'Created {len(cert_map)} certifications.')

        # Create products
        all_pkgs = list(pkg_map.values())
        all_certs = list(cert_map.values())

        for p in PRODUCTS:
            product = Product.objects.create(
                name_en=p['name_en'],
                name_fr=p['name_fr'],
                name_ar=p['name_ar'],
                slug=p['slug'],
                category=p['category'],
                is_featured=p.get('is_featured', False),
                short_description_en=p['short_en'],
                short_description_fr=p['short_fr'],
                short_description_ar=p['short_ar'],
                description_en=p['desc_en'],
                description_fr=p['desc_fr'],
                description_ar=p['desc_ar'],
            )
            # All products get all packaging and all certifications
            product.packaging.set(all_pkgs)
            product.certifications.set(all_certs)
            # Set preservation methods per product
            pres_objs = [pres_map[n] for n in p.get('preservations', [])]
            product.preservation.set(pres_objs)

        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {len(PRODUCTS)} products.'
        ))
