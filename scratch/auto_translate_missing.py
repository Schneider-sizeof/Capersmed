import re, os, polib
import time
from deep_translator import GoogleTranslator

# 1. Find all strings in templates
strings = set()
for root, dirs, files in os.walk('core/templates'):
    for fn in files:
        if fn.endswith('.html'):
            try:
                content = open(os.path.join(root, fn), encoding='utf-8').read()
                # Extract {% trans "..." %}
                found = re.findall(r'\{%\s*trans\s+"([^"]+)"', content)
                strings.update(found)
                # Extract {% trans '...' %}
                found2 = re.findall(r"\{%\s*trans\s+'([^']+)'", content)
                strings.update(found2)
            except Exception as e:
                pass

# Exclude URL-like strings
exclude = {
    "about/", "products/", "products/<str:slug>/", "certifications/",
    "blog/", "blog/<str:slug>/", "branding/", "services/", "contact/",
    "products/<slug:slug>/", "blog/<slug:slug>/"
}
strings = {s for s in strings if s not in exclude}

LANGS = ['ar', 'fr', 'es', 'it', 'pt']

print(f"Total translatable strings extracted from templates: {len(strings)}")

for lang in LANGS:
    po_path = f'locale/{lang}/LC_MESSAGES/django.po'
    if not os.path.isfile(po_path):
        continue
    
    po = polib.pofile(po_path)
    existing = {e.msgid for e in po}
    missing = strings - existing
    
    if not missing:
        print(f"{lang.upper()}: All strings translated.")
        continue
        
    print(f"Translating {len(missing)} strings for {lang.upper()}...")
    
    translator = GoogleTranslator(source='en', target=lang)
    
    added = 0
    for i, s in enumerate(missing):
        if not s.strip(): continue
        try:
            trans = translator.translate(s)
            entry = polib.POEntry(msgid=s, msgstr=trans)
            po.append(entry)
            added += 1
            if i % 10 == 0:
                print(f"  ... {i}/{len(missing)} translated")
            # Rate limiting to prevent Google Translate blocks
            time.sleep(0.05)
        except Exception as e:
            print(f"Failed to translate '{s}': {e}")
            
    if added > 0:
        po.save()
        po.save_as_mofile(po_path.replace('.po', '.mo'))
        print(f"✅ Saved {added} new translations for {lang.upper()} and compiled .mo")

print("Done! All translations up to date.")
