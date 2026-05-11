"""Create 2 example blog posts with translations."""
import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'capersmed.settings'
django.setup()

from core.models import BlogPost
from django.utils import timezone

# Clear existing
BlogPost.objects.all().delete()

# Post 1: Export News
BlogPost.objects.create(
    title_en="CAPERSMED Expands Export to 15 New Markets in 2026",
    title_fr="CAPERSMED etend ses exportations a 15 nouveaux marches en 2026",
    title_ar="كابرزميد توسع صادراتها إلى 15 سوقاً جديداً في 2026",
    slug="capersmed-expands-export-2026",
    category="export",
    excerpt_en="CAPERSMED SARL announces a major expansion of its international distribution network, reaching 15 new markets across Europe, the Middle East, and North America.",
    excerpt_fr="CAPERSMED SARL annonce une expansion majeure de son reseau de distribution international, atteignant 15 nouveaux marches en Europe, au Moyen-Orient et en Amerique du Nord.",
    excerpt_ar="تعلن شركة كابرزميد عن توسع كبير في شبكة التوزيع الدولية لتصل إلى 15 سوقاً جديداً.",
    content_en=(
        "CAPERSMED SARL, Morocco's leading producer of premium capers, vinegars, "
        "and pickled condiments, has announced a significant expansion of its global "
        "footprint in 2026.\n\n"
        "The company has secured new distribution agreements in 15 additional markets, "
        "including Germany, the Netherlands, Sweden, Saudi Arabia, Kuwait, Qatar, "
        "Canada, and Japan.\n\n"
        "\"Our commitment to quality and food safety certification has been the key "
        "driver of this expansion,\" said the company's export director. \"Buyers trust "
        "our IFS, BRC, Halal, and Kosher certifications, which makes the procurement "
        "process smoother for importers worldwide.\"\n\n"
        "The expansion includes both private label partnerships and branded product "
        "lines, with particular demand for the company's signature Moroccan capers, "
        "preserved lemons, and apple cider vinegar.\n\n"
        "CAPERSMED's state-of-the-art production facility in Fes operates under strict "
        "quality control protocols and has the capacity to serve growing international "
        "demand while maintaining the artisanal quality that defines Moroccan gourmet tradition."
    ),
    content_fr=(
        "CAPERSMED SARL, le premier producteur marocain de capres, vinaigres et "
        "condiments marines premium, a annonce une expansion significative de sa "
        "presence mondiale en 2026.\n\n"
        "L'entreprise a conclu de nouveaux accords de distribution dans 15 marches "
        "supplementaires, notamment l'Allemagne, les Pays-Bas, la Suede, l'Arabie "
        "saoudite, le Koweit, le Qatar, le Canada et le Japon.\n\n"
        "\"Notre engagement envers la qualite et les certifications de securite "
        "alimentaire a ete le moteur principal de cette expansion\", a declare le "
        "directeur export. \"Les acheteurs font confiance a nos certifications IFS, "
        "BRC, Halal et Casher.\"\n\n"
        "L'expansion comprend des partenariats en marque privee et des gammes de "
        "produits de marque, avec une demande particuliere pour les capres marocaines, "
        "les citrons confits et le vinaigre de cidre de pomme.\n\n"
        "L'installation de production de CAPERSMED a Fes fonctionne sous des protocoles "
        "de controle qualite stricts tout en maintenant la qualite artisanale qui "
        "definit la tradition gastronomique marocaine."
    ),
    content_ar=(
        "أعلنت شركة كابرزميد، المنتج المغربي الرائد للكبار والخل والمخللات الفاخرة، "
        "عن توسع كبير في حضورها العالمي في عام 2026.\n\n"
        "أبرمت الشركة اتفاقيات توزيع جديدة في 15 سوقاً إضافياً، بما في ذلك ألمانيا "
        "وهولندا والسويد والمملكة العربية السعودية والكويت وقطر وكندا واليابان.\n\n"
        "يشمل التوسع شراكات العلامة الخاصة وخطوط المنتجات ذات العلامة التجارية، مع "
        "طلب خاص على الكبار المغربية والليمون المصبر وخل التفاح."
    ),
    author="CAPERSMED Team",
    is_published=True,
    published_at=timezone.now(),
)
print("Post 1 created: Export expansion")

# Post 2: Recipes
BlogPost.objects.create(
    title_en="5 Ways to Use Moroccan Preserved Lemons in Your Kitchen",
    title_fr="5 facons d'utiliser les citrons confits marocains dans votre cuisine",
    title_ar="5 طرق لاستخدام الليمون المصبر المغربي في مطبخك",
    slug="5-ways-preserved-lemons",
    category="recipes",
    excerpt_en="Discover how Moroccan preserved lemons can transform your dishes, from tagines to salad dressings, pasta, and cocktails.",
    excerpt_fr="Decouvrez comment les citrons confits marocains peuvent transformer vos plats, des tagines aux vinaigrettes, pates et cocktails.",
    excerpt_ar="اكتشف كيف يمكن لليمون المصبر المغربي أن يحول أطباقك من الطاجين إلى صلصات السلطة والمعكرونة.",
    content_en=(
        "Preserved lemons are one of Morocco's most iconic culinary ingredients, "
        "and they're far more versatile than most people realize.\n\n"
        "Here are 5 delicious ways to incorporate them into your cooking:\n\n"
        "1. Classic Moroccan Tagine\n"
        "The most traditional use. Dice preserved lemon rind and add it to chicken "
        "or lamb tagine with olives. The bright, salty-sour flavor is unmistakable.\n\n"
        "2. Elevated Salad Dressings\n"
        "Blend preserved lemon pulp into vinaigrettes for an instant flavor upgrade. "
        "Mix with olive oil, fresh herbs, and a touch of honey for a Mediterranean "
        "dressing that transforms any salad.\n\n"
        "3. Pasta and Risotto\n"
        "Finely chop preserved lemon rind and toss it into pasta with capers, olive oil, "
        "and parmesan. The combination of salty, citrusy, and umami flavors is extraordinary.\n\n"
        "4. Grilled Fish and Seafood\n"
        "Stuff whole fish with preserved lemon slices before grilling, or blend into a "
        "compound butter for seafood. The preserved lemon adds depth that fresh lemon "
        "simply cannot match.\n\n"
        "5. Cocktails and Beverages\n"
        "Muddle small pieces of preserved lemon into gin and tonics, martinis, or even "
        "lemonade. The fermented complexity adds a sophisticated twist to any drink.\n\n"
        "All CAPERSMED preserved lemons are made from Moroccan Eureka lemons, salt-cured "
        "for a minimum of 30 days, and available in 370g jars, 720g jars, and 5L bulk "
        "containers for food service."
    ),
    content_fr=(
        "Les citrons confits sont l'un des ingredients culinaires les plus "
        "emblematiques du Maroc, et ils sont bien plus polyvalents que la plupart "
        "des gens ne le pensent.\n\n"
        "Voici 5 facons delicieuses de les integrer dans votre cuisine :\n\n"
        "1. Tagine Marocain Classique\n"
        "L'utilisation la plus traditionnelle. Coupez l'ecorce de citron confit en "
        "des et ajoutez-la au tagine de poulet ou d'agneau avec des olives.\n\n"
        "2. Vinaigrettes Elevees\n"
        "Mixez la pulpe de citron confit dans des vinaigrettes pour une amelioration "
        "instantanee de la saveur. Melangez avec de l'huile d'olive et des herbes fraiches.\n\n"
        "3. Pates et Risotto\n"
        "Hachez finement l'ecorce de citron confit et melangez-la aux pates avec des "
        "capres, de l'huile d'olive et du parmesan.\n\n"
        "4. Poisson Grille et Fruits de Mer\n"
        "Farcissez le poisson entier avec des tranches de citron confit avant de griller.\n\n"
        "5. Cocktails et Boissons\n"
        "Melez de petits morceaux de citron confit dans des gin tonics ou des martinis.\n\n"
        "Tous les citrons confits CAPERSMED sont fabriques a partir de citrons Eureka "
        "marocains, sales pendant un minimum de 30 jours."
    ),
    content_ar=(
        "الليمون المصبر هو أحد أكثر المكونات الطهوية شهرة في المغرب، وهو أكثر "
        "تنوعاً مما يدركه معظم الناس.\n\n"
        "إليك 5 طرق لذيذة لدمجه في طبخك:\n\n"
        "1. الطاجين المغربي التقليدي\n"
        "قطع قشر الليمون المصبر وأضفه إلى طاجين الدجاج أو اللحم مع الزيتون.\n\n"
        "2. صلصات السلطة\n"
        "امزج لب الليمون المصبر في صلصات الخل لتحسين فوري للنكهة.\n\n"
        "3. المعكرونة والريزوتو\n"
        "اقطع قشر الليمون المصبر ناعماً وامزجه مع المعكرونة والكبار وزيت الزيتون.\n\n"
        "4. السمك المشوي والمأكولات البحرية\n"
        "احشُ السمك الكامل بشرائح الليمون المصبر قبل الشوي.\n\n"
        "5. الكوكتيلات والمشروبات\n"
        "امزج قطعاً صغيرة من الليمون المصبر في مشروبات الجن تونيك أو المارتيني."
    ),
    author="CAPERSMED Team",
    is_published=True,
    published_at=timezone.now(),
)
print("Post 2 created: Preserved lemons recipes")
print("Done! 2 blog posts created with EN/FR/AR translations.")
