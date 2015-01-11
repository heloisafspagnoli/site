from django import template
from django.template.defaultfilters import stringfilter
import unicodedata

register = template.Library()

@register.filter
@stringfilter
def text2list(value):
    return value.split('\n')


@register.filter
@stringfilter
def slugfy(value):
    aux_value = value.lower()
    aux_value = aux_value.replace(" ", "-")
    aux_value = unicodedata.normalize("NFKD", aux_value)
    aux_value = aux_value.encode("ascii", "ignore")    
    return aux_value
