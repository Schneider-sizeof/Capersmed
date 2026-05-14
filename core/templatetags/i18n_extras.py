from django import template
from django.urls import translate_url as django_translate_url

register = template.Library()


@register.simple_tag(takes_context=True)
def translate_url(context, lang_code):
    """
    Returns the current page URL translated to the given language.
    Usage: {% translate_url 'fr' %}
    E.g. if current page is /en/products/, returns /fr/produits/
    """
    request = context.get('request')
    if request is None:
        return '/{}/'.format(lang_code)
    current_url = request.get_full_path()
    translated = django_translate_url(current_url, lang_code)
    return translated
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
