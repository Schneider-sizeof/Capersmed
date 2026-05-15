import polib
import os

NEW_TRANSLATIONS = {
    "From the fertile lands of Morocco to the tables of the world, CAPERSMED brings you the finest gourmet ingredients.": {
        "fr": "Des terres fertiles du Maroc aux tables du monde entier, CAPERSMED vous apporte les meilleurs ingrédients gastronomiques.",
        "es": "Desde las tierras fértiles de Marruecos hasta las mesas del mundo, CAPERSMED le ofrece los mejores ingredientes gourmet.",
        "it": "Dalle terre fertili del Marocco alle tavole di tutto il mondo, CAPERSMED vi offre i migliori ingredienti gourmet.",
        "ar": "من الأراضي الخصبة في المغرب إلى موائد العالم، تقدم لكم كابرزميد أجود المكونات الغذائية الفاخرة.",
        "pt": "Das terras férteis de Marrocos para as mesas de todo o mundo, a CAPERSMED traz-lhe os melhores ingredientes gourmet."
    },
    "What started as a family passion for Moroccan heritage has grown into a leading export operation, serving gourmet markets across Europe, North America, and the Middle East.": {
        "fr": "Ce qui a commencé comme une passion familiale pour le patrimoine marocain est devenu une opération d'exportation de premier plan, desservant les marchés gastronomiques d'Europe, d'Amérique du Nord et du Moyen-Orient.",
        "es": "Lo que comenzó como una pasión familiar por la herencia marroquí se ha convertido en una operación de exportación líder, que sirve a los mercados gourmet de Europa, América del Norte y Oriente Medio.",
        "it": "Quella che era iniziata come una passione di famiglia per il patrimonio marocchino è diventata un'operazione di esportazione leader, servendo i mercati gourmet in Europa, Nord America e Medio Oriente.",
        "ar": "ما بدأ كشغف عائلي بالتراث المغربي تطور ليصبح عملية تصدير رائدة، تخدم الأسواق الفاخرة في أوروبا وأمريكا الشمالية والشرق الأوسط.",
        "pt": "O que começou como uma paixão familiar pelo património marroquino tornou-se uma operação de exportação líder, servindo mercados gourmet em toda a Europa, América do Norte e Médio Oriente."
    },
    "Our commitment to quality starts at the source, working closely with local farmers to ensure only the finest raw materials are selected for our production.": {
        "fr": "Notre engagement envers la qualité commence à la source, en travaillant en étroite collaboration avec les agriculteurs locaux pour garantir que seules les meilleures matières premières sont sélectionnées pour notre production.",
        "es": "Nuestro compromiso con la calidad comienza en la fuente, trabajando estrechamente con los agricultores locales para garantizar que solo se seleccionen las mejores materias primas para nuestra producción.",
        "it": "Il nostro impegno per la qualità inizia alla fonte, lavorando a stretto contatto con gli agricoltori locali per garantire che solo le migliori materie prime siano selezionate per la nostra produzione.",
        "ar": "يبدأ التزامنا بالجودة من المصدر، حيث نعمل عن كثب مع المزارعين المحليين لضمان اختيار أفضل المواد الخام فقط لإنتاجنا.",
        "pt": "O nosso compromisso com a qualidade começa na origem, trabalhando em estreita colaboração com os agricultores locais para garantir que apenas as melhores matérias-primas são selecionadas para a nossa produção."
    },
    "Integrity": {
        "fr": "Intégrité",
        "es": "Integridad",
        "it": "Integrità",
        "ar": "النزاهة",
        "pt": "Integridade"
    },
    "We maintain the highest standards of honesty and transparency in every step of our process, from sourcing to shipping.": {
        "fr": "Nous maintenons les normes les plus élevées d'honnêteté et de transparence à chaque étape de notre processus, de l'approvisionnement à l'expédition.",
        "es": "Mantenemos los más altos estándares de honestidad y transparencia en cada paso de nuestro proceso, desde el abastecimiento hasta el envío.",
        "it": "Manteniamo i più alti standard di onestà e trasparenza in ogni fase del nostro processo, dall'approvvigionamento alla spedizione.",
        "ar": "نحافظ على أعلى معايير الأمانة والشفافية في كل خطوة من عمليتنا، من التوريد إلى الشحن.",
        "pt": "Mantemos os mais elevados padrões de honestidade e transparência em cada etapa do nosso processo, desde o fornecimento até ao envio."
    },
    "Excellence": {
        "fr": "Excellence",
        "es": "Excelencia",
        "it": "Eccellenza",
        "ar": "التميز",
        "pt": "Excelência"
    },
    "Uncompromising quality control ensures that only the most premium products reach our international partners.": {
        "fr": "Un contrôle qualité sans compromis garantit que seuls les produits les plus premium parviennent à nos partenaires internationaux.",
        "es": "Un control de calidad sin compromisos garantiza que solo los productos más premium lleguen a nuestros socios internacionales.",
        "it": "Il controllo qualità senza compromessi garantisce che solo i prodotti più pregiati raggiungano i nostri partner internazionali.",
        "ar": "تضمن مراقبة الجودة الصارمة وصول المنتجات الأكثر تميزاً فقط إلى شركائنا الدوليين.",
        "pt": "O controlo de qualidade intransigente garante que apenas os produtos mais premium cheguem aos nossos parceiros internacionais."
    },
    "Our recipes are rooted in Moroccan tradition, preserving the true taste and heritage of our culinary culture.": {
        "fr": "Nos recettes sont ancrées dans la tradition marocaine, préservant le vrai goût et l'héritage de notre culture culinaire.",
        "es": "Nuestras recetas están arraigadas en la tradición marroquí, preservando el verdadero sabor y la herencia de nuestra cultura culinaria.",
        "it": "Le nostre ricette sono radicate nella tradizione marocchina, preservando il vero gusto e l'eredità della nostra cultura culinaria.",
        "ar": "وصفاتنا متجذرة في التقاليد المغربية، مما يحافظ على المذاق الحقيقي وتراث ثقافتنا في الطهي.",
        "pt": "As nossas receitas estão enraizadas na tradição marroquina, preservando o verdadeiro sabor e herança da nossa cultura culinária."
    },
    "Global Standards": {
        "fr": "Normes Mondiales",
        "es": "Estándares Globales",
        "it": "Standard Globali",
        "ar": "معايير عالمية",
        "pt": "Padrões Globais"
    },
    "Our production facilities meet the most stringent international food safety and quality standards, ensuring trust and reliability for our global clients.": {
        "fr": "Nos installations de production répondent aux normes internationales de sécurité alimentaire et de qualité les plus strictes, garantissant confiance et fiabilité à nos clients mondiaux.",
        "es": "Nuestras instalaciones de producción cumplen con los estándares internacionales de seguridad alimentaria y calidad más estrictos, lo que garantiza la confianza y confiabilidad de nuestros clientes globales.",
        "it": "I nostri impianti di produzione soddisfano i più severi standard internazionali di sicurezza alimentare e qualità, garantendo fiducia e affidabilità ai nostri clienti globali.",
        "ar": "تبي مرافق الإنتاج لدينا أكثر معايير سلامة الأغذية والجودة الدولية صرامة، مما يضمن الثقة والموثوقية لعملائنا العالميين.",
        "pt": "As nossas instalações de produção cumprem os mais rigorosos padrões internacionais de segurança alimentar e qualidade, garantindo confiança e fiabilidade aos nossos clientes globais."
    },
    "Export Ready Standards": {
        "fr": "Normes Prêtes pour l'Exportation",
        "es": "Estándares Listos para la Exportación",
        "it": "Standard Pronti per l'Esportazione",
        "ar": "معايير جاهزة للتصدير",
        "pt": "Padrões Prontos para Exportação"
    },
    "Explore our full catalog of premium products and discover the authentic taste of Morocco.": {
        "fr": "Explorez notre catalogue complet de produits premium et découvrez le goût authentique du Maroc.",
        "es": "Explore nuestro catálogo completo de productos premium y descubra el auténtico sabor de Marruecos.",
        "it": "Esplora il nostro catalogo completo di prodotti premium e scopri il gusto autentico del Marocco.",
        "ar": "استكشف كتالوجنا الكامل للمنتجات المميزة واكتشف المذاق الأصيل للمغرب.",
        "pt": "Explore o nosso catálogo completo de produtos premium e descubra o sabor autêntico de Marrocos."
    },
    "Authenticity": {
        "fr": "Authenticité",
        "es": "Autenticidad",
        "it": "Autenticità",
        "ar": "الأصالة",
        "pt": "Autenticidade"
    },
    "Contact Us": {
        "fr": "Contactez-nous",
        "es": "Contáctenos",
        "it": "Contattaci",
        "ar": "اتصل بنا",
        "pt": "Contacte-nos"
    }
}

LANGS = ['ar', 'fr', 'es', 'it', 'pt']

for lang in LANGS:
    po_path = f'locale/{lang}/LC_MESSAGES/django.po'
    if not os.path.exists(po_path):
        print(f"Skipping {lang}, file not found.")
        continue
        
    po = polib.pofile(po_path)
    existing = {e.msgid: e for e in po}
    added = 0
    updated = 0
    
    for msgid, translations in NEW_TRANSLATIONS.items():
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
    # Compile to .mo
    mo_path = po_path.replace('.po', '.mo')
    po.save_as_mofile(mo_path)
    print(f"{lang.upper()}: Added {added}, Updated {updated} translations. Compiled .mo")

print("Done!")
