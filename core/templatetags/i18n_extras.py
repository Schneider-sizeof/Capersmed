from django import template
from django.urls import translate_url as django_translate_url, reverse
from django.utils.translation import override as lang_override

register = template.Library()


@register.simple_tag(takes_context=True)
def translate_url(context, lang_code):
    """
    Returns the current page URL translated to the given language.
    For detail pages (product_detail, blog_detail), also translates the slug
    so that /ar/المنتجات/ثمار-الكبار/ becomes /es/productos/alcaparrones/
    instead of /es/productos/ثمار-الكبار/.
    """
    request = context.get('request')
    if request is None:
        return '/{}/'.format(lang_code)

    # Check if we're on a detail page with a slug
    resolver_match = getattr(request, 'resolver_match', None)
    if resolver_match and 'slug' in (resolver_match.kwargs or {}):
        url_name = resolver_match.url_name
        current_slug = resolver_match.kwargs['slug']

        try:
            if url_name == 'product_detail':
                from core.models import Product
                from django.db.models import Q
                obj = Product.objects.filter(
                    Q(slug=current_slug) | Q(slug_fr=current_slug) |
                    Q(slug_ar=current_slug) | Q(slug_es=current_slug) |
                    Q(slug_it=current_slug) | Q(slug_pt=current_slug)
                ).first()
                if obj:
                    translated_slug = _get_slug_for_lang(obj, lang_code)
                    with lang_override(lang_code):
                        return reverse('product_detail', kwargs={'slug': translated_slug})

            elif url_name == 'blog_detail':
                from core.models import BlogPost
                from django.db.models import Q
                obj = BlogPost.objects.filter(
                    Q(slug=current_slug) | Q(slug_fr=current_slug) |
                    Q(slug_ar=current_slug) | Q(slug_es=current_slug) |
                    Q(slug_it=current_slug) | Q(slug_pt=current_slug)
                ).first()
                if obj:
                    translated_slug = _get_slug_for_lang(obj, lang_code)
                    with lang_override(lang_code):
                        return reverse('blog_detail', kwargs={'slug': translated_slug})
        except Exception:
            pass  # Fall through to default translation

    # Default: translate URL path only (works for all non-detail pages)
    current_url = request.get_full_path()
    return django_translate_url(current_url, lang_code)


def _get_slug_for_lang(obj, lang_code):
    """
    Get the translated slug for a given language.
    Falls back to: slug_{lang} → slug_en → slug (base English).
    """
    # Try the target language slug
    slug = getattr(obj, f'slug_{lang_code}', None)
    if slug:
        return slug
    # Try English slug field (some models use slug_en)
    slug = getattr(obj, 'slug_en', None)
    if slug:
        return slug
    # Fall back to base slug
    return obj.slug


@register.filter
def translate_field(obj, field_name):
    """
    Returns the value of a translated field on an object.
    Usage: {{ product|translate_field:'name' }}
    Tries: field_name_LANGUAGE_CODE, then field_name_en, then field_name.
    """
    from django.utils.translation import get_language
    lang = get_language()

    # Try the current language
    val = getattr(obj, f"{field_name}_{lang}", None)
    if val:
        return val

    # Try English
    val = getattr(obj, f"{field_name}_en", None)
    if val:
        return val

    # Try the base field
    return getattr(obj, field_name, "")


@register.filter
def dict_get(dictionary, key):
    """
    Lookup a key in a dictionary.
    Usage: {{ hero_backgrounds|dict_get:'home' }}
    """
    if dictionary and hasattr(dictionary, 'get'):
        return dictionary.get(key)
    return None

