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

 
 
def _get_template_vars(template_name):
    app_name, template_name = template_name.split(":", 1)
    try:
        template_dir = abspath(join(dirname(get_app(app_name).__file__), 'templates'))
    except ImproperlyConfigured:
        raise TemplateDoesNotExist()
    
    return template_name, template_dir
 
def load_template_from_app(template_name, template_dirs=None):
    """ 
    Template loader that only serves templates from specific app's template directory.
 
    Works for template_names in format app_label:some/template/name.html
    """
    if ":" not in template_name:
        raise TemplateDoesNotExist()
 
    template_name, template_dir = _get_template_vars(template_name)
 
    if not isdir(template_dir):
        raise TemplateDoesNotExist()
    
    return load_template_source(template_name, template_dirs=[template_dir])
 
load_template_from_app.is_usable = True