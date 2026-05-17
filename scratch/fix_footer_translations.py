import polib
import os

MISSING_TRANSLATIONS = {
    "Products": {
        "ar": "المنتجات",
        "fr": "Produits",
        "es": "Productos",
        "it": "Prodotti",
        "pt": "Produtos"
    },
    "Certifications": {
        "ar": "الشهادات",
        "fr": "Certifications",
        "es": "Certificaciones",
        "it": "Certificazioni",
        "pt": "Certificações"
    },
    "Branding": {
        "ar": "العلامة التجارية",
        "fr": "Marque",
        "es": "Marca",
        "it": "Marchio",
        "pt": "Marca"
    },
    "Blog": {
        "ar": "المدونة",
        "fr": "Blog",
        "es": "Blog",
        "it": "Blog",
        "pt": "Blog"
    },
    "Contact": {
        "ar": "اتصل بنا",
        "fr": "Contact",
        "es": "Contacto",
        "it": "Contatto",
        "pt": "Contato"
    },
    "Main navigation": {
        "ar": "التنقل الرئيسي",
        "fr": "Navigation principale",
        "es": "Navegación principal",
        "it": "Navigazione principale",
        "pt": "Navegação principal"
    },
    "Back to home": {
        "ar": "العودة إلى الصفحة الرئيسية",
        "fr": "Retour à l'accueil",
        "es": "Volver al inicio",
        "it": "Torna alla home",
        "pt": "Voltar ao início"
    },
    "Language selector": {
        "ar": "محدد اللغة",
        "fr": "Sélecteur de langue",
        "es": "Selector de idioma",
        "it": "Selettore di lingua",
        "pt": "Seletor de idioma"
    },
    "Open menu": {
        "ar": "فتح القائمة",
        "fr": "Ouvrir le menu",
        "es": "Abrir menú",
        "it": "Apri menu",
        "pt": "Abrir menu"
    },
    "Mobile navigation": {
        "ar": "التنقل للجوال",
        "fr": "Navigation mobile",
        "es": "Navegación móvil",
        "it": "Navigazione mobile",
        "pt": "Navegação móvel"
    },
    "Authentic Moroccan Gourmet Products — From Our Fields to Your Table.": {
        "ar": "منتجات مغربية أصيلة فاخرة — من حقولنا إلى مائدتكم.",
        "fr": "Produits gastronomiques marocains authentiques — De nos champs à votre table.",
        "es": "Auténticos Productos Gourmet Marroquíes — De Nuestros Campos a Su Mesa.",
        "it": "Autentici Prodotti Gourmet Marocchini — Dai Nostri Campi alla Vostra Tavola.",
        "pt": "Autênticos Produtos Gourmet Marroquinos — Dos Nossos Campos para a Sua Mesa."
    },
    "Quick Links": {
        "ar": "روابط سريعة",
        "fr": "Liens rapides",
        "es": "Enlaces Rápidos",
        "it": "Link Rapidi",
        "pt": "Links Rápidos"
    },
    "Home": {
        "ar": "الرئيسية",
        "fr": "Accueil",
        "es": "Inicio",
        "it": "Home",
        "pt": "Início"
    },
    "About Us": {
        "ar": "من نحن",
        "fr": "À propos",
        "es": "Sobre Nosotros",
        "it": "Chi Siamo",
        "pt": "Sobre Nós"
    },
    "Cookie Settings": {
        "ar": "إعدادات ملفات تعريف الارتباط",
        "fr": "Paramètres des cookies",
        "es": "Configuración de cookies",
        "it": "Impostazioni cookie",
        "pt": "Configurações de cookies"
    },
    "Contact Info": {
        "ar": "معلومات الاتصال",
        "fr": "Coordonnées",
        "es": "Información de contacto",
        "it": "Informazioni di contatto",
        "pt": "Informações de contato"
    },
    "Chat on WhatsApp": {
        "ar": "دردش عبر واتساب",
        "fr": "Discuter sur WhatsApp",
        "es": "Chatear en WhatsApp",
        "it": "Chatta su WhatsApp",
        "pt": "Conversar no WhatsApp"
    }
}

LANGS = ['ar', 'fr', 'es', 'it', 'pt']
base_dir = os.path.dirname(os.path.abspath(__file__))
# Because script is in scratch/, root is one level up
root_dir = os.path.dirname(base_dir)

for lang in LANGS:
    po_path = os.path.join(root_dir, f'locale/{lang}/LC_MESSAGES/django.po')
    if not os.path.exists(po_path):
        print(f"Skipping {lang}, file not found at {po_path}")
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
    
    po.save()
    print(f"{lang.upper()}: Added {added}, Updated {updated} translations.")

print("Done updating .po files!")
