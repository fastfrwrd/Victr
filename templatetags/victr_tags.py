from os.path import dirname, join, abspath, isdir
from django.db.models import get_app
from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from datetime import datetime
from victr.config import Config as config
import re

 
# from django.template import TemplateDoesNotExist
# from django.template.loaders.filesystem import load_template_source

register = template.Library()

""" tags! """

@register.simple_tag
def victr_base():
    """ returns base URL for victr. Available as Victr.base in JS. """
    return reverse('victr.views.home')
    
@register.simple_tag
def victr_keyword(key):
    """ returns language set in config.py """
    return config.keyword(key)

@register.simple_tag
def victr_stylesheet():
    return ''.join([ '<link href="'+url+'" rel="stylesheet">\n' for url in config.stylesheet()])

@register.simple_tag
def victr_brand():
    return '<img src="'+config.brand()+'" />'

@register.simple_tag
def active(request, view, class1, class2=None):
    if path(request) == reverse(view):
        return class1
    if class2:
        return class2

@register.simple_tag
def next(request):
    return getattr(getattr(request,request.method),'next','')

@register.simple_tag
def path(request):
    return request.path


""" filters! """

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
def joinand(value, delimiter):
    """ 
    Joins and formats a list of items with Oxford commas, "and"s,
    the whole shebang.
    """
    last = value.pop()
    result = delimiter.join(value)
    if len(value) > 1 : 
        result = "%s," % result  #oxford comma
    if result : 
        result = "%s and %s" % (result, last) #2 or more
    else : 
        result = last #all by myself
    return result

@register.filter
def multiply(value, multiplier):
    """multiplies tag value by multiplier."""
    return value * multiplier

@register.filter
def past(value):
    """returns true if scheduled event is in the past."""
    return value <= datetime.now()