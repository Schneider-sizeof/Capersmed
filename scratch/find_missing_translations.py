import re, os, glob

# Find all {% trans "..." %} and {% trans '...' %} strings in templates
patterns = [
    r'\{%\s*trans\s*"((?:[^"\\]|\\.)*)"\s*%\}',
    r"\{%\s*trans\s*'((?:[^'\\]|\\.)*)'\s*%\}",
]

strings = set()
template_dirs = ['core/templates']
for td in template_dirs:
    for f in glob.glob(os.path.join(td, '**', '*.html'), recursive=True):
        content = open(f, encoding='utf-8').read()
        for p in patterns:
            strings.update(re.findall(p, content))

# Filter out URL slugs and very short strings
strings = {s for s in strings if len(s) > 2 and '/' not in s and '<' not in s}

print(f"Found {len(strings)} translatable strings in templates\n")

# Check each language PO file
for lang in ['fr', 'ar', 'es', 'it', 'pt']:
    po_path = f'locale/{lang}/LC_MESSAGES/django.po'
    if not os.path.exists(po_path):
        print(f"--- {lang}: FILE NOT FOUND ---")
        continue
    
    po_content = open(po_path, encoding='utf-8').read()
    
    missing = []
    for s in sorted(strings):
        # Check if msgid exists in PO file
        escaped = s.replace('"', '\\"')
        if f'msgid "{escaped}"' not in po_content:
            # Also check multi-line msgid (first line)
            first_words = s[:40]
            if first_words not in po_content:
                missing.append(s)
    
    if missing:
        print(f"--- {lang.upper()}: {len(missing)} MISSING ---")
        for m in missing:
            print(f"  - {m[:80]}")
        print()
    else:
        print(f"--- {lang.upper()}: All good! ---\n")
