"""Find strings in templates but missing from .po files."""
import re, os, polib

strings = set()
for root, dirs, files in os.walk('core/templates'):
    for fn in files:
        if fn.endswith('.html'):
            content = open(os.path.join(root, fn), encoding='utf-8').read()
            found = re.findall(r'\{%\s*trans\s+"([^"]+)"', content)
            strings.update(found)

# Also add URL strings from urls.py
url_strings = ["about/","products/","products/<slug:slug>/","certifications/",
               "blog/","blog/<slug:slug>/","branding/","services/","contact/"]
strings.update(url_strings)

for lang in ['fr','es','it','ar']:
    po_path = f'locale/{lang}/LC_MESSAGES/django.po'
    if not os.path.isfile(po_path):
        continue
    po = polib.pofile(po_path)
    existing = {e.msgid for e in po}
    missing = strings - existing
    if missing:
        print(f"\n=== {lang.upper()}: {len(missing)} missing ===")
        for s in sorted(missing):
            print(f'  "{s}"')
    else:
        print(f"{lang.upper()}: All {len(strings)} strings present!")
