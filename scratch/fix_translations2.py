"""Fix remaining FR and PT missing translations."""

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

fr = {
    "Back to home": "Retour à l'accueil",
    "Browse our complete catalog of premium Moroccan capers, caperberries, peppers, harissa, and pickled vegetables for export.": "Parcourez notre catalogue complet de câpres, câprons, piments, harissa et légumes marinés marocains premium pour l'export.",
    "Browse premium Moroccan capers, peppers, and pickled vegetables for export.": "Parcourez nos câpres, piments et légumes marinés marocains premium pour l'export.",
    "CAPERSMED holds Kosher, IFS Food, BRC Global Standard, and FDA certifications ensuring international food safety compliance.": "CAPERSMED détient les certifications Kosher, IFS, BRC et FDA garantissant la conformité internationale en sécurité alimentaire.",
    "CAPERSMED offers private label, custom label design, and custom packaging for importers and distributors.": "CAPERSMED propose la marque propre, le design d'étiquettes et l'emballage personnalisé pour importateurs et distributeurs.",
    "Chat on WhatsApp": "Discuter sur WhatsApp",
    "Contact CAPERSMED for bulk orders and export inquiries.": "Contactez CAPERSMED pour commandes en gros et demandes d'exportation.",
    "Contact CAPERSMED for wholesale pricing, private label, or export inquiries. Located in Fes, Morocco.": "Contactez CAPERSMED pour prix de gros, marque propre ou demandes d'export. Situés à Fès, Maroc.",
    "Custom branding, private label, and packaging solutions for Moroccan products.": "Solutions de branding, marque propre et emballage pour produits marocains.",
    "Export news, recipes, and product updates from CAPERSMED.": "Actualités export, recettes et nouveautés produits de CAPERSMED.",
    "Founded in Fes, Morocco — delivering authentic Moroccan gourmet products to the world.": "Fondée à Fès, Maroc — livrant des produits gastronomiques marocains authentiques au monde entier.",
    "Get in touch for wholesale, private label, or export inquiries.": "Contactez-nous pour le gros, la marque propre ou les demandes d'export.",
    "Industry insights, export news, and gourmet recipes from Morocco's premier condiment producer.": "Analyses du secteur, actualités export et recettes gastronomiques du premier producteur marocain de condiments.",
    "International food safety certifications for premium Moroccan products.": "Certifications internationales de sécurité alimentaire pour produits marocains premium.",
    "Kosher, IFS, BRC, FDA certified — international food safety standards for global export.": "Certifié Kosher, IFS, BRC, FDA — normes internationales de sécurité alimentaire pour l'export mondial.",
    "Language selector": "Sélecteur de langue",
    "Learn about CAPERSMED — premium Moroccan gourmet producer.": "Découvrez CAPERSMED — producteur marocain gastronomique premium.",
    "Learn about CAPERSMED.SARL — a leading Moroccan producer of premium capers, preserved lemons, and gourmet condiments.": "Découvrez CAPERSMED.SARL — producteur marocain leader de câpres, citrons confits et condiments gastronomiques premium.",
    "Main navigation": "Navigation principale",
    "Mobile navigation": "Navigation mobile",
    "Open menu": "Ouvrir le menu",
    "Premium Moroccan gourmet products available in multiple packaging formats with full certification documentation for global export.": "Produits gastronomiques marocains premium disponibles en plusieurs formats d'emballage avec documentation de certification complète pour l'export mondial.",
    "Private Label & Branding": "Marque Propre et Branding",
    "Private label and custom branding for premium Moroccan gourmet products.": "Marque propre et branding personnalisé pour produits gastronomiques marocains premium.",
}

pt = {
    "All branded products come with full certification documentation (HALAL, KOSHER, IFS, BRC, FDA) ready for import clearance in your target country.": "Todos os produtos de marca vêm com documentação de certificação completa (HALAL, KOSHER, IFS, BRC, FDA) pronta para desalfandegamento no seu país de destino.",
    "Apply your brand name, logo, and design to our product range. Full private label production with your artwork on our certified Moroccan gourmet products.": "Aplique o nome da sua marca, logotipo e design à nossa gama de produtos. Produção completa de marca própria com a sua arte nos nossos produtos gourmet marroquinos certificados.",
    "CAPERSMED offers complete branding and private label solutions for importers, distributors, and retailers. From custom labels to full packaging design — we help you launch your own line of premium Moroccan gourmet products.": "A CAPERSMED oferece soluções completas de branding e marca própria para importadores, distribuidores e retalhistas. De rótulos personalizados ao design completo de embalagem — ajudamos a lançar a sua própria linha de produtos gourmet marroquinos premium.",
    "Describe your brand vision, target market, or any specific requirements...": "Descreva a sua visão de marca, mercado-alvo ou quaisquer requisitos específicos...",
    "Fill in the form below and our branding team will contact you within 48 hours with a tailored proposal.": "Preencha o formulário abaixo e a nossa equipa de branding contactá-lo-á em 48 horas com uma proposta personalizada.",
    "Founded in the heart of Morocco, CAPERSMED.SARL was established with a vision to bring the authentic flavors of Moroccan agriculture to the world. We specialize in the meticulous processing and packaging of premium capers, vinegars, and a variety of traditional condiments.": "Fundada no coração de Marrocos, a CAPERSMED.SARL foi estabelecida com a visão de levar os sabores autênticos da agricultura marroquina ao mundo. Especializamo-nos no processamento e embalagem meticulosos de alcaparras, vinagres e condimentos tradicionais premium.",
    "Industry insights, export news, gourmet recipes, and product updates from CAPERSMED.": "Perspetivas da indústria, notícias de exportação, receitas gourmet e novidades de produtos da CAPERSMED.",
    "Industry insights, export news, gourmet recipes, and updates from Morocco's premier condiment producer.": "Perspetivas da indústria, notícias de exportação, receitas gourmet e atualizações do principal produtor marroquino de condimentos.",
    "Insights & Updates": "Perspetivas e Atualizações",
    "Need a specific brine strength, spice level, or size? We work with you to develop a custom recipe or adjust existing products to meet your buyers' exact specifications.": "Precisa de um nível específico de salmoura, picante ou tamanho? Trabalhamos consigo para desenvolver uma receita personalizada ou ajustar produtos existentes às especificações exatas dos seus compradores.",
    "Our design team creates professional label artwork tailored to your brand identity — colors, typography, multilingual text, and regulatory compliance for your target market.": "A nossa equipa de design cria arte profissional para rótulos adaptada à identidade da sua marca — cores, tipografia, texto multilingue e conformidade regulatória para o seu mercado-alvo.",
    "Our mission is to deliver the highest quality gourmet food products while supporting local farmers and sustainable agricultural practices. We value integrity, authenticity, and uncompromising quality.": "A nossa missão é entregar produtos alimentares gourmet da mais alta qualidade, apoiando os agricultores locais e as práticas agrícolas sustentáveis. Valorizamos a integridade, autenticidade e qualidade sem compromissos.",
    "Physical samples are produced and shipped for your review.": "As amostras físicas são produzidas e enviadas para a sua avaliação.",
    "Premium Moroccan gourmet products. Each item is available in multiple packaging formats with full certification documentation for global export.": "Produtos gourmet marroquinos premium. Cada artigo está disponível em múltiplos formatos de embalagem com documentação de certificação completa para exportação global.",
    "Select from our full range of packaging formats — 200ml, 500ml, 2L, 7L, 1000L IBC — and we'll produce them under your brand specifications.": "Selecione da nossa gama completa de formatos de embalagem — 200ml, 500ml, 2L, 7L, 1000L IBC — e produziremos segundo as especificações da sua marca.",
    "Subscribe to receive export news, product updates, and gourmet insights from CAPERSMED.": "Subscreva para receber notícias de exportação, atualizações de produtos e perspetivas gourmet da CAPERSMED.",
    "We assist with export documentation, freight coordination, and customs compliance to ensure smooth delivery of your branded goods to any destination worldwide.": "Auxiliamos com documentação de exportação, coordenação de frete e conformidade aduaneira para garantir a entrega fluida dos seus produtos de marca para qualquer destino mundial.",
    "We create label artwork and packaging mockups for your approval.": "Criamos arte para rótulos e maquetes de embalagem para a sua aprovação.",
    "We offer custom labeling, private label production, and flexible packaging formats for importers and distributors worldwide.": "Oferecemos rotulagem personalizada, produção de marca própria e formatos de embalagem flexíveis para importadores e distribuidores em todo o mundo.",
    "We provide full certification documentation upon request for importers, distributors, and compliance officers. Contact us to receive official certificates for your procurement process.": "Fornecemos documentação de certificação completa mediante pedido para importadores, distribuidores e responsáveis de conformidade. Contacte-nos para receber os certificados oficiais para o seu processo de aquisição.",
    "You share your brand vision, target market, and product selection.": "Partilhe a sua visão de marca, mercado-alvo e seleção de produtos.",
}

append_to_po('fr', fr)
append_to_po('pt', pt)
print("\nDone!")
