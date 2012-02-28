from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from datetime import datetime
from victr import config
import re

register = template.Library()

#tags
@register.simple_tag
def victr_base():
    """ returns base URL for victr. Available as Victr.base in JS. """
    return reverse('victr.views.home')
    
@register.simple_tag
def victr_keyword(key):
    """ returns language set in config.py """
    return config.keyword(key)

#filters
class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')
@register.filter
def add_class(value, css_class):
    """adds class to element."""
    string = unicode(value)
    match = class_re.search(string)
    if match:
        m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (css_class, css_class,
                                                    css_class, css_class),
            match.group(1))
        print match.group(1)
        if not m:
            return mark_safe(class_re.sub(match.group(1) + " " + css_class,
                string))
    else:
        return mark_safe(string.replace('>', ' class="%s">' % css_class))
    return value
    
@register.filter
def multiply(value, multiplier):
    """multiplies tag value by multiplier."""
    return value * multiplier
    
@register.filter
def past(value):
    """returns true if scheduled event is in the past."""
    return value <= datetime.now()