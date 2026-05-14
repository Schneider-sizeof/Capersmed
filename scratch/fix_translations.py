"""Add missing translations to all PO files."""
import os

# Missing strings shared across AR, ES, IT (SEO meta descriptions + a11y)
shared_missing = {
    "Browse our complete catalog of premium Moroccan capers, caperberries, peppers, harissa, and pickled vegetables for export.": {
        "ar": "تصفح كتالوجنا الكامل من الكبار والفلفل والهريسة والمخللات المغربية الفاخرة للتصدير.",
        "es": "Explore nuestro catálogo completo de alcaparras, pimientos, harissa y verduras en conserva marroquíes premium para exportación.",
        "it": "Sfoglia il nostro catalogo completo di capperi, peperoni, harissa e verdure sott'aceto marocchini premium per l'esportazione.",
        "pt": "Explore o nosso catálogo completo de alcaparras, pimentos, harissa e legumes em conserva marroquinos premium para exportação.",
    },
    "Browse premium Moroccan capers, peppers, and pickled vegetables for export.": {
        "ar": "تصفح الكبار والفلفل والمخللات المغربية الفاخرة للتصدير.",
        "es": "Explore alcaparras, pimientos y verduras en conserva marroquíes premium para exportación.",
        "it": "Sfoglia capperi, peperoni e verdure sott'aceto marocchini premium per l'esportazione.",
        "pt": "Explore alcaparras, pimentos e legumes em conserva marroquinos premium para exportação.",
    },
    "CAPERSMED holds Kosher, IFS Food, BRC Global Standard, and FDA certifications ensuring international food safety compliance.": {
        "ar": "كابرزميد حاصلة على شهادات كوشر وIFS وBRC وFDA لضمان الامتثال الدولي لسلامة الغذاء.",
        "es": "CAPERSMED cuenta con certificaciones Kosher, IFS, BRC y FDA que garantizan el cumplimiento internacional de seguridad alimentaria.",
        "it": "CAPERSMED detiene certificazioni Kosher, IFS, BRC e FDA che garantiscono la conformità internazionale alla sicurezza alimentare.",
        "pt": "A CAPERSMED possui certificações Kosher, IFS, BRC e FDA que garantem o cumprimento internacional da segurança alimentar.",
    },
    "CAPERSMED offers private label, custom label design, and custom packaging for importers and distributors.": {
        "ar": "تقدم كابرزميد خدمات العلامة الخاصة وتصميم الملصقات والتغليف المخصص للمستوردين والموزعين.",
        "es": "CAPERSMED ofrece marca privada, diseño de etiquetas y embalaje personalizado para importadores y distribuidores.",
        "it": "CAPERSMED offre marchio privato, design etichette e packaging personalizzato per importatori e distributori.",
        "pt": "A CAPERSMED oferece marca própria, design de rótulos e embalagem personalizada para importadores e distribuidores.",
    },
    "Chat on WhatsApp": {
        "ar": "تحدث عبر واتساب",
        "es": "Chatear en WhatsApp",
        "it": "Chatta su WhatsApp",
    },
    "Contact CAPERSMED for bulk orders and export inquiries.": {
        "ar": "اتصل بكابرزميد لطلبات الجملة واستفسارات التصدير.",
        "es": "Contacte con CAPERSMED para pedidos a granel y consultas de exportación.",
        "it": "Contatta CAPERSMED per ordini all'ingrosso e richieste di esportazione.",
        "pt": "Contacte a CAPERSMED para encomendas por grosso e consultas de exportação.",
    },
    "Contact CAPERSMED for wholesale pricing, private label, or export inquiries. Located in Fes, Morocco.": {
        "ar": "اتصل بكابرزميد لأسعار الجملة أو العلامة الخاصة أو استفسارات التصدير. مقرنا في فاس، المغرب.",
        "es": "Contacte con CAPERSMED para precios mayoristas, marca privada o consultas de exportación. Ubicados en Fez, Marruecos.",
        "it": "Contatta CAPERSMED per prezzi all'ingrosso, marchio privato o richieste di esportazione. Sede a Fes, Marocco.",
        "pt": "Contacte a CAPERSMED para preços de grosso, marca própria ou consultas de exportação. Localizada em Fez, Marrocos.",
    },
    "Custom branding, private label, and packaging solutions for Moroccan products.": {
        "ar": "حلول العلامة التجارية والعلامة الخاصة والتغليف للمنتجات المغربية.",
        "es": "Soluciones de branding, marca privada y embalaje para productos marroquíes.",
        "it": "Soluzioni di branding, marchio privato e packaging per prodotti marocchini.",
        "pt": "Soluções de branding, marca própria e embalagem para produtos marroquinos.",
    },
    "Export news, recipes, and product updates from CAPERSMED.": {
        "ar": "أخبار التصدير والوصفات وتحديثات المنتجات من كابرزميد.",
        "es": "Noticias de exportación, recetas y novedades de productos de CAPERSMED.",
        "it": "Notizie sull'export, ricette e aggiornamenti prodotti da CAPERSMED.",
        "pt": "Notícias de exportação, receitas e atualizações de produtos da CAPERSMED.",
    },
    "Founded in Fes, Morocco — delivering authentic Moroccan gourmet products to the world.": {
        "ar": "تأسست في فاس، المغرب — نقدم منتجات مغربية أصيلة فاخرة للعالم.",
        "es": "Fundada en Fez, Marruecos — llevando productos gourmet marroquíes auténticos al mundo.",
        "it": "Fondata a Fes, Marocco — consegniamo prodotti gourmet marocchini autentici al mondo.",
        "pt": "Fundada em Fez, Marrocos — entregando produtos gourmet marroquinos autênticos ao mundo.",
    },
    "Get in touch for wholesale, private label, or export inquiries.": {
        "ar": "تواصل معنا لاستفسارات الجملة أو العلامة الخاصة أو التصدير.",
        "es": "Póngase en contacto para consultas de mayorista, marca privada o exportación.",
        "it": "Mettiti in contatto per richieste all'ingrosso, marchio privato o esportazione.",
        "pt": "Entre em contacto para consultas de grosso, marca própria ou exportação.",
    },
    "International food safety certifications for premium Moroccan products.": {
        "ar": "شهادات سلامة غذائية دولية للمنتجات المغربية الفاخرة.",
        "es": "Certificaciones internacionales de seguridad alimentaria para productos marroquíes premium.",
        "it": "Certificazioni internazionali di sicurezza alimentare per prodotti marocchini premium.",
        "pt": "Certificações internacionais de segurança alimentar para produtos marroquinos premium.",
    },
    "Kosher, IFS, BRC, FDA certified — international food safety standards for global export.": {
        "ar": "معتمد كوشر، IFS، BRC، FDA — معايير سلامة غذائية دولية للتصدير العالمي.",
        "es": "Certificado Kosher, IFS, BRC, FDA — estándares internacionales de seguridad alimentaria para exportación global.",
        "it": "Certificato Kosher, IFS, BRC, FDA — standard internazionali di sicurezza alimentare per l'esportazione globale.",
        "pt": "Certificado Kosher, IFS, BRC, FDA — padrões internacionais de segurança alimentar para exportação global.",
    },
    "Language selector": {
        "ar": "اختيار اللغة",
        "es": "Selector de idioma",
        "it": "Selettore lingua",
    },
    "Learn about CAPERSMED — premium Moroccan gourmet producer.": {
        "ar": "تعرف على كابرزميد — منتج مغربي فاخر للأغذية.",
        "es": "Conozca CAPERSMED — productor gourmet marroquí premium.",
        "it": "Scopri CAPERSMED — produttore gourmet marocchino premium.",
        "pt": "Conheça a CAPERSMED — produtor gourmet marroquino premium.",
    },
    "Learn about CAPERSMED.SARL — a leading Moroccan producer of premium capers, preserved lemons, and gourmet condiments.": {
        "ar": "تعرف على كابرزميد — منتج مغربي رائد للكبار والليمون المصبر والتوابل الفاخرة.",
        "es": "Conozca CAPERSMED.SARL — productor marroquí líder de alcaparras, limones encurtidos y condimentos gourmet premium.",
        "it": "Scopri CAPERSMED.SARL — produttore marocchino leader di capperi, limoni conservati e condimenti gourmet premium.",
        "pt": "Conheça a CAPERSMED.SARL — produtor marroquino líder de alcaparras, limões conservados e condimentos gourmet premium.",
    },
    "Main navigation": {
        "ar": "التنقل الرئيسي",
        "es": "Navegación principal",
        "it": "Navigazione principale",
    },
    "Mobile navigation": {
        "ar": "التنقل المحمول",
        "es": "Navegación móvil",
        "it": "Navigazione mobile",
    },
    "Open menu": {
        "ar": "فتح القائمة",
        "es": "Abrir menú",
        "it": "Apri menu",
    },
    "Back to home": {
        "it": "Torna alla home",
        "es": "Volver al inicio",
        "ar": "العودة للرئيسية",
    },
    "Premium Moroccan gourmet products available in multiple packaging formats with full certification documentation for global export.": {
        "ar": "منتجات مغربية فاخرة متوفرة بأشكال تغليف متعددة مع وثائق شهادات كاملة للتصدير العالمي.",
        "es": "Productos gourmet marroquíes premium disponibles en múltiples formatos de embalaje con documentación de certificación completa para exportación global.",
        "it": "Prodotti gourmet marocchini premium disponibili in molteplici formati di packaging con documentazione di certificazione completa per l'esportazione globale.",
        "pt": "Produtos gourmet marroquinos premium disponíveis em múltiplos formatos de embalagem com documentação de certificação completa para exportação global.",
    },
    "Private Label & Branding": {
        "ar": "العلامة الخاصة والعلامة التجارية",
        "es": "Marca Privada y Branding",
        "it": "Marchio Privato e Branding",
        "pt": "Marca Própria e Branding",
    },
    "Private label and custom branding for premium Moroccan gourmet products.": {
        "ar": "علامة خاصة وعلامة تجارية مخصصة للمنتجات المغربية الفاخرة.",
        "es": "Marca privada y branding personalizado para productos gourmet marroquíes premium.",
        "it": "Marchio privato e branding personalizzato per prodotti gourmet marocchini premium.",
        "pt": "Marca própria e branding personalizado para produtos gourmet marroquinos premium.",
    },
    "Industry insights, export news, and gourmet recipes from Morocco's premier condiment producer.": {
        "ar": "رؤى صناعية وأخبار التصدير ووصفات الذواقة من المنتج المغربي الرائد للتوابل.",
        "es": "Perspectivas de la industria, noticias de exportación y recetas gourmet del principal productor marroquí de condimentos.",
        "it": "Approfondimenti del settore, notizie sull'export e ricette gourmet dal principale produttore marocchino di condimenti.",
        "pt": "Perspetivas da indústria, notícias de exportação e receitas gourmet do principal produtor marroquino de condimentos.",
    },
    "Product Catalog": {
        "pt": "Catálogo de Produtos",
    },
}

# PT-only missing strings (common UI strings)
pt_only = {
    "< 1,000 units": "< 1.000 unidades",
    "1,000 – 10,000 units": "1.000 – 10.000 unidades",
    "10,000 – 50,000 units": "10.000 – 50.000 unidades",
    "> 50,000 units": "> 50.000 unidades",
    "All": "Todos",
    "Back to Blog": "Voltar ao Blog",
    "Brand Creation Inquiry": "Consulta de Criação de Marca",
    "Brand Project Type": "Tipo de Projeto de Marca",
    "Brief": "Resumo",
    "Bulk pricing": "Preços por grosso",
    "Capers": "Alcaparras",
    "Caperberries": "Frutos de Alcaparra",
    "Certified Halal": "Certificado Halal",
    "Coming Soon": "Em Breve",
    "Competitive pricing.": "Preços competitivos.",
    "Comprehensive solutions for wholesale, export, and private label.": "Soluções completas para grosso, exportação e marca própria.",
    "Consultation": "Consulta",
    "Contact Person": "Pessoa de Contacto",
    "Cornichons": "Cornichões",
    "Create your brand with our expertise.": "Crie a sua marca com a nossa experiência.",
    "Custom Packaging Format": "Formato de Embalagem Personalizado",
    "Custom label design": "Design de rótulo personalizado",
    "Custom recipes": "Receitas personalizadas",
    "Delivery": "Entrega",
    "Discuss your requirements.": "Discuta os seus requisitos.",
    "Email Address": "Endereço de Email",
    "Estimated Annual Volume": "Volume Anual Estimado",
    "Experience Moroccan Quality": "Experimente a Qualidade Marroquina",
    "Export Standards": "Padrões de Exportação",
    "Export docs": "Documentos de exportação",
    "Export documentation": "Documentação de exportação",
    "Export-ready delivery to your door or port of choice.": "Entrega pronta para exportação à sua porta ou porto de escolha.",
    "Flexible packaging": "Embalagem flexível",
    "Flexible quantities": "Quantidades flexíveis",
    "Food Production": "Produção Alimentar",
    "Food Safety Management": "Gestão de Segurança Alimentar",
    "Food safety certified": "Certificado de segurança alimentar",
    "Full Brand Creation": "Criação Completa de Marca",
    "Full production run with your branding applied.": "Produção completa com o seu branding aplicado.",
    "Get in Touch": "Entre em Contacto",
    "Halal": "Halal",
    "Halal Certified": "Certificado Halal",
    "Harissa": "Harissa",
    "Hazard Analysis": "Análise de Riscos",
    "High-quality production with modern facilities.": "Produção de alta qualidade com instalações modernas.",
    "Industry": "Indústria",
    "International shipping": "Envio internacional",
    "Kosher": "Kosher",
    "Kosher Certified": "Certificado Kosher",
    "Large-scale capacity": "Capacidade em larga escala",
    "Logistics": "Logística",
    "Low MOQ": "MOQ Baixo",
    "Mission & Values": "Missão e Valores",
    "Need Custom Packaging or a Bulk Quote?": "Precisa de Embalagem Personalizada ou Orçamento por Grosso?",
    "News": "Notícias",
    "No products yet.": "Ainda sem produtos.",
    "On-time delivery": "Entrega pontual",
    "Other": "Outro",
    "Our Process": "O Nosso Processo",
    "Our Product Catalog": "O Nosso Catálogo de Produtos",
    "Our Services": "Os Nossos Serviços",
    "Our Story": "A Nossa História",
    "Our first articles are being prepared. Check back soon.": "Os nossos primeiros artigos estão a ser preparados. Volte em breve.",
    "Packaging Available": "Embalagem Disponível",
    "Packaging Format(s)": "Formato(s) de Embalagem",
    "Pickled Peppers": "Pimentos em Conserva",
    "Preserved Lemons": "Limões Conservados",
    "Private Label (my brand on your products)": "Marca Própria (a minha marca nos vossos produtos)",
    "Products of Interest": "Produtos de Interesse",
    "Quality manufacturing.": "Fabrico de qualidade.",
    "Quality-controlled": "Controlo de qualidade",
    "Quotation": "Orçamento",
    "Read More": "Ler Mais",
    "Related Articles": "Artigos Relacionados",
    "Reliable delivery worldwide.": "Entrega fiável em todo o mundo.",
    "Sample": "Amostra",
    "Secure packaging": "Embalagem segura",
    "Shipped to your location.": "Enviado para a sua localização.",
    "Start Your Project": "Inicie o Seu Projeto",
    "Stay in the Loop": "Mantenha-se Informado",
    "Supply restaurants, retailers, distributors worldwide.": "Abasteça restaurantes, retalhistas e distribuidores em todo o mundo.",
    "Temperature-controlled": "Temperatura controlada",
    "The CAPERSMED Journal": "O Jornal CAPERSMED",
    "View": "Ver",
    "View All Products": "Ver Todos os Produtos",
    "View Our Products": "Ver os Nossos Produtos",
    "We respond within 48 business hours.": "Respondemos em 48 horas úteis.",
    "Your brand our quality": "A sua marca, a nossa qualidade",
    "Your company or brand name": "A sua empresa ou nome de marca",
    "Your full name": "O seu nome completo",
    "e.g. France, USA, UAE": "ex. França, EUA, EAU",
    "— Select —": "— Selecionar —",
    "Recipes": "Receitas",
    "Export": "Exportação",
    "Vinegars": "Vinagres",
    "Other / Custom": "Outro / Personalizado",
    "Certifications Required": "Certificações Necessárias",
    "Design": "Design",
    "Production": "Produção",
    "Verified Quality": "Qualidade Verificada",
    "Our Certifications": "As Nossas Certificações",
    "Premium Vinegars": "Vinagres Premium",
    "Hot & Spicy": "Picante",
    "Quick Links": "Links Rápidos",
    "Premium Moroccan Gourmet": "Gourmet Marroquino Premium",
}

def append_to_po(lang, entries):
    path = f'locale/{lang}/LC_MESSAGES/django.po'
    content = open(path, encoding='utf-8').read()
    new_entries = []
    for msgid, msgstr in entries.items():
        escaped_id = msgid.replace('"', '\\"')
        if f'msgid "{escaped_id}"' not in content and escaped_id[:40] not in content:
            new_entries.append(f'\nmsgid "{escaped_id}"\nmsgstr "{msgstr}"')
    if new_entries:
        with open(path, 'a', encoding='utf-8') as f:
            f.write('\n# ─── Auto-added missing translations ───')
            for e in new_entries:
                f.write(e)
            f.write('\n')
        print(f"  {lang}: Added {len(new_entries)} translations")
    else:
        print(f"  {lang}: Nothing to add")

# Process shared strings
for lang in ['ar', 'es', 'it', 'pt']:
    entries = {}
    for msgid, translations in shared_missing.items():
        if lang in translations:
            entries[msgid] = translations[lang]
    append_to_po(lang, entries)

# Process PT-only strings
append_to_po('pt', pt_only)

print("\nDone! Run compile_messages.py to compile.")
