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
