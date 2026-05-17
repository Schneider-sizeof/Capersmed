import polib
import os

MISSING_TRANSLATIONS = {
    "CAPERSMED Team": {
        "ar": "فريق كابرزِميد",
        "fr": "Équipe CAPERSMED",
        "es": "Equipo CAPERSMED",
        "it": "Team CAPERSMED",
        "pt": "Equipe CAPERSMED"
    }
}

LANGS = ['ar', 'fr', 'es', 'it', 'pt']
base_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(base_dir)

for lang in LANGS:
    po_path = os.path.join(root_dir, f'locale/{lang}/LC_MESSAGES/django.po')
    if not os.path.exists(po_path):
        continue
        
    po = polib.pofile(po_path)
    existing = {e.msgid: e for e in po}
    added = 0
    updated = 0
    
    for msgid, translations in MISSING_TRANSLATIONS.items():
        if lang in translations:
            if msgid not in existing:
                entry = polib.POEntry(msgid=msgid, msgstr=translations[lang])
                po.append(entry)
                added += 1
            else:
                if not existing[msgid].msgstr:
                    existing[msgid].msgstr = translations[lang]
                    updated += 1
    
    if added > 0 or updated > 0:
        po.save()
        po.save_as_mofile(po_path.replace('.po', '.mo'))
        print(f"{lang.upper()}: Added/Updated 'CAPERSMED Team'. Compiled .mo")

print("Done updating .po files for team name!")
