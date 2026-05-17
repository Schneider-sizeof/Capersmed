import polib
import os

URLS = {
    "products/": {"fr": "produits/", "es": "productos/", "it": "prodotti/", "pt": "produtos/", "ar": "منتجات/"},
    "products/<str:slug>/": {"fr": "produits/<str:slug>/", "es": "productos/<str:slug>/", "it": "prodotti/<str:slug>/", "pt": "produtos/<str:slug>/", "ar": "منتجات/<str:slug>/"},
    "blog/": {"fr": "blog/", "es": "blog/", "it": "blog/", "pt": "blog/", "ar": "مدونة/"},
    "blog/<str:slug>/": {"fr": "blog/<str:slug>/", "es": "blog/<str:slug>/", "it": "blog/<str:slug>/", "pt": "blog/<str:slug>/", "ar": "مدونة/<str:slug>/"},
}

base_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(base_dir)

for lang in ['fr', 'es', 'it', 'pt', 'ar']:
    po_path = os.path.join(root_dir, f'locale/{lang}/LC_MESSAGES/django.po')
    if not os.path.exists(po_path): continue
    po = polib.pofile(po_path)
    existing = {e.msgid: e for e in po}
    added = 0
    
    for msgid, trans in URLS.items():
        val = trans.get(lang)
        if not val: continue
        if msgid not in existing:
            po.append(polib.POEntry(msgid=msgid, msgstr=val))
            added += 1
        else:
            existing[msgid].msgstr = val
            added += 1
            
    po.save()
    po.save_as_mofile(po_path.replace('.po', '.mo'))
    print(f"{lang} updated {added} URLs")
