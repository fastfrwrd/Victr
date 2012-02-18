from django import template
from django.core.urlresolvers import reverse

register = template.Library()
@register.simple_tag(name='victr_base')
def victr_base():
    return reverse('victr.views.home')