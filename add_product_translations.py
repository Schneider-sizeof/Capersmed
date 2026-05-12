"""Add missing translations for new product categories and fields."""
import os

# New translations to add
NEW_TRANSLATIONS = {
    'fr': {
        'Capers & Caperberries': 'Câpres et Câprons',
        'Peppers & Hot Products': 'Piments et Produits Piquants',
        'Preservation': 'Conservation',
        'View →': 'Voir →',
    },
    'ar': {
        'Capers & Caperberries': 'الكبار وثمار الكبار',
        'Peppers & Hot Products': 'الفلفل والمنتجات الحارة',
        'Pickled Vegetables & Condiments': 'خضروات مخللة وتوابل',
        'Preservation': 'طريقة الحفظ',
        'Packaging Available': 'التغليف المتاح',
        'View →': 'عرض →',
        'Photo': 'صورة',
        'Product': 'منتج',
        'Certifications': 'الشهادات',
        'Details': 'تفاصيل',
        'All': 'الكل',
        'No products yet.': 'لا توجد منتجات بعد.',
        'Our Product Catalog': 'كتالوج منتجاتنا',
        'Premium': 'مميز',
    },
    'es': {
        'Capers & Caperberries': 'Alcaparras y Alcaparrones',
        'Peppers & Hot Products': 'Pimientos y Productos Picantes',
        'Pickled Vegetables & Condiments': 'Verduras Encurtidas y Condimentos',
        'Preservation': 'Conservación',
        'View →': 'Ver →',
    },
    'it': {
        'Capers & Caperberries': 'Capperi e Frutti di Cappero',
        'Peppers & Hot Products': 'Peperoni e Prodotti Piccanti',
        'Pickled Vegetables & Condiments': 'Verdure Sottaceto e Condimenti',
        'Preservation': 'Conservazione',
        'View →': 'Vedi →',
    },
}

BASE = os.path.dirname(os.path.abspath(__file__))

for lang, entries in NEW_TRANSLATIONS.items():
    po_path = os.path.join(BASE, 'locale', lang, 'LC_MESSAGES', 'django.po')
    if not os.path.exists(po_path):
        print(f"  SKIP {lang}: {po_path} not found")
        continue

    with open(po_path, 'r', encoding='utf-8') as f:
        content = f.read()

    added = 0
    for msgid, msgstr in entries.items():
        # Check if this msgid already exists
        marker = f'msgid "{msgid}"'
        if marker in content:
            continue
        # Append new entry
        content += f'\nmsgid "{msgid}"\nmsgstr "{msgstr}"\n'
        added += 1

    with open(po_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  {lang}: added {added} new translations")

print("Done! Run: python manage.py compilemessages")
