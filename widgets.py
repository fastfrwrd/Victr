from django.forms.widgets import Select, SelectMultiple
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from victr.models import Discipline
from django import forms

class SelectWithDisabled(Select):
    """
    Subclass of Django's select widget that allows disabling options.
    To disable an option, pass a dict instead of a string for its label,
    of the form: {'label': 'option label', 'disabled': True}
    """
    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_unicode(option_value)
        if (option_value in selected_choices):
            selected_html = u' selected="selected"'
        else:
            selected_html = ''
        disabled_html = ''
        if isinstance(option_label, dict):
            if dict.get(option_label, 'disabled') and option_value not in selected_choices:
                disabled_html = u' disabled="disabled"'
            option_label = option_label['label']
        return u'<option value="%s"%s%s>%s</option>' % (
            escape(option_value), selected_html, disabled_html,
            conditional_escape(force_unicode(option_label)))
    
    
class Tagger(forms.fields.MultipleChoiceField):
    
    def __init__(self, type, *args, **kwargs):
        self.Type = type
        super(self.__class__, self).__init__(*args, **kwargs);
    
    def clean(self, values):
        return map(self.clean_value, values)

    def clean_value(self, value):
        if value.isdigit():
            obj = self.Type.objects.filter(pk=int(value))
        else:
            obj = self.Type.objects.filter(title=value)

        if obj:
            obj = obj[0]
        else:
            obj = self.Type(title=value)
            obj.save()
            self._choices.append((obj.pk, obj))
        return obj.pk
        