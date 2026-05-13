"""
Create the first blog post from LinkedIn content.
Run: python create_blog_post.py
"""
import os, shutil
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capersmed.settings')
import django
django.setup()

from django.utils import timezone
from core.models import BlogPost

# Delete existing blog posts (fresh start)
BlogPost.objects.all().delete()
print("Cleared old blog posts.")

# Copy caperberries image as blog image
src = os.path.join('media', 'products', 'caperberries.png')
dst = os.path.join('media', 'blog', 'caprons-linkedin.png')
if os.path.exists(src):
    shutil.copy2(src, dst)
    print(f"Copied blog image to {dst}")

post = BlogPost.objects.create(
    # --- French (original LinkedIn post) ---
    title_fr="Decouvrez les Caprons de Capersmed",

    excerpt_fr=(
        "Les caprons de Capersmed sont une veritable explosion de saveurs "
        "mediterraneennes. Cultives avec soin et recoltes a la main, nos caprons "
        "apportent une touche d'authenticite a vos plats preferes."
    ),

    content_fr=(
        "Les caprons de Capersmed sont une veritable explosion de saveurs "
        "mediterraneennes. Cultives avec soin et recoltes a la main, conserves "
        "de la main d'un expert, nos caprons apportent une touche d'authenticite "
        "a vos plats preferes.\n\n"
        "**Pourquoi choisir nos caprons ?**\n\n"
        "- Qualite superieure et fraicheur garantie.\n"
        "- Saveur intense et texture croquante.\n"
        "- Ideaux pour agrementer salades, sauces et plats mediterraneens.\n\n"
        "Essayez nos caprons des aujourd'hui et decouvrez la difference !\n\n"
        "Certifie IFS et Kosher, nous exportons nos produits vers plus de 12 pays !"
    ),

    # --- English ---
    title_en="Discover Capersmed Caperberries",

    excerpt_en=(
        "Capersmed caperberries are a true explosion of Mediterranean flavours. "
        "Carefully cultivated and hand-picked, our caperberries bring a touch "
        "of authenticity to your favourite dishes."
    ),

    content_en=(
        "Capersmed caperberries are a true explosion of Mediterranean flavours. "
        "Carefully cultivated and hand-picked, preserved by expert hands, our "
        "caperberries bring a touch of authenticity to your favourite dishes.\n\n"
        "**Why choose our caperberries?**\n\n"
        "- Superior quality and guaranteed freshness.\n"
        "- Intense flavour and crunchy texture.\n"
        "- Ideal for enhancing salads, sauces, and Mediterranean dishes.\n\n"
        "Try our caperberries today and discover the difference!\n\n"
        "IFS and Kosher certified, we export our products to over 12 countries!"
    ),

    # --- Arabic ---
    title_ar="\u0627\u0643\u062a\u0634\u0641\u0648\u0627 \u062b\u0645\u0627\u0631 \u0627\u0644\u0643\u0628\u0627\u0631 \u0645\u0646 \u0643\u0627\u0628\u0631\u0632\u0645\u064a\u062f",

    excerpt_ar=(
        "\u062b\u0645\u0627\u0631 \u0627\u0644\u0643\u0628\u0627\u0631 \u0645\u0646 \u0643\u0627\u0628\u0631\u0632\u0645\u064a\u062f \u0647\u064a \u0627\u0646\u0641\u062c\u0627\u0631 \u062d\u0642\u064a\u0642\u064a \u0645\u0646 \u0627\u0644\u0646\u0643\u0647\u0627\u062a "
        "\u0627\u0644\u0645\u062a\u0648\u0633\u0637\u064a\u0629. \u0645\u0632\u0631\u0648\u0639\u0629 \u0628\u0639\u0646\u0627\u064a\u0629 \u0648\u0645\u0642\u0637\u0648\u0641\u0629 \u064a\u062f\u0648\u064a\u0627\u064b\u060c "
        "\u062a\u0636\u064a\u0641 \u0644\u0645\u0633\u0629 \u0623\u0635\u0627\u0644\u0629 \u0625\u0644\u0649 \u0623\u0637\u0628\u0627\u0642\u0643\u0645 \u0627\u0644\u0645\u0641\u0636\u0644\u0629."
    ),

    content_ar=(
        "\u062b\u0645\u0627\u0631 \u0627\u0644\u0643\u0628\u0627\u0631 \u0645\u0646 \u0643\u0627\u0628\u0631\u0632\u0645\u064a\u062f \u0647\u064a \u0627\u0646\u0641\u062c\u0627\u0631 \u062d\u0642\u064a\u0642\u064a \u0645\u0646 \u0627\u0644\u0646\u0643\u0647\u0627\u062a "
        "\u0627\u0644\u0645\u062a\u0648\u0633\u0637\u064a\u0629. \u0645\u0632\u0631\u0648\u0639\u0629 \u0628\u0639\u0646\u0627\u064a\u0629 \u0648\u0645\u0642\u0637\u0648\u0641\u0629 \u064a\u062f\u0648\u064a\u0627\u064b\u060c "
        "\u0645\u062d\u0641\u0648\u0638\u0629 \u0628\u064a\u062f \u062e\u0628\u064a\u0631\u0629\u060c \u062a\u0636\u064a\u0641 \u0644\u0645\u0633\u0629 \u0623\u0635\u0627\u0644\u0629 \u0625\u0644\u0649 \u0623\u0637\u0628\u0627\u0642\u0643\u0645 \u0627\u0644\u0645\u0641\u0636\u0644\u0629.\n\n"
        "**\u0644\u0645\u0627\u0630\u0627 \u062a\u062e\u062a\u0627\u0631\u0648\u0646 \u062b\u0645\u0627\u0631 \u0627\u0644\u0643\u0628\u0627\u0631 \u0644\u062f\u064a\u0646\u0627\u061f**\n\n"
        "- \u062c\u0648\u062f\u0629 \u0639\u0627\u0644\u064a\u0629 \u0648\u0637\u0632\u0627\u062c\u0629 \u0645\u0636\u0645\u0648\u0646\u0629.\n"
        "- \u0646\u0643\u0647\u0629 \u0642\u0648\u064a\u0629 \u0648\u0642\u0648\u0627\u0645 \u0645\u0642\u0631\u0645\u0634.\n"
        "- \u0645\u062b\u0627\u0644\u064a\u0629 \u0644\u062a\u0632\u064a\u064a\u0646 \u0627\u0644\u0633\u0644\u0637\u0627\u062a \u0648\u0627\u0644\u0635\u0644\u0635\u0627\u062a \u0648\u0627\u0644\u0623\u0637\u0628\u0627\u0642 \u0627\u0644\u0645\u062a\u0648\u0633\u0637\u064a\u0629.\n\n"
        "\u062c\u0631\u0628\u0648\u0627 \u062b\u0645\u0627\u0631 \u0627\u0644\u0643\u0628\u0627\u0631 \u0627\u0644\u064a\u0648\u0645 \u0648\u0627\u0643\u062a\u0634\u0641\u0648\u0627 \u0627\u0644\u0641\u0631\u0642!\n\n"
        "\u062d\u0627\u0635\u0644\u0648\u0646 \u0639\u0644\u0649 \u0634\u0647\u0627\u062f\u0629 IFS \u0648Kosher\u060c \u0646\u0635\u062f\u0631 \u0645\u0646\u062a\u062c\u0627\u062a\u0646\u0627 \u0625\u0644\u0649 \u0623\u0643\u062b\u0631 \u0645\u0646 12 \u062f\u0648\u0644\u0629!"
    ),

    slug="discover-capersmed-caperberries",
    category="products",
    author="CAPERSMED Team",
    image="blog/caprons-linkedin.png",
    is_published=True,
    published_at=timezone.now(),
)

print(f"Created blog post: {post.title_en} (slug: {post.slug})")
print("Done!")
