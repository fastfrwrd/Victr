from django import forms
from django.forms import ModelForm, Form
from django.contrib import auth
from django.db import models
from django.core.urlresolvers import reverse
from victr import config
from victr.models import UserProfile, Project, Event
from victr.event.util import EventQuery
from victr.widgets import SelectWithDisabled
import string

class RegistrationForm(ModelForm):
    """
    Attributes defined here are found in RegistrationForm.fields
    It seems that the reason we have fields specified below as attributes is because
    this form has to gather information for both auth.User and victr.UserProfile
    """
    first_name  = forms.fields.CharField(
                    max_length = 25, 
                    widget = forms.TextInput(attrs={'placeholder':'Victr'}), )
    last_name   = forms.fields.CharField(
                    max_length = 25, 
                    widget = forms.TextInput(attrs={'placeholder':'Appleseed'}), )
    email       = forms.EmailField(
                    max_length = 100, 
                    widget = forms.TextInput(attrs={'placeholder':'victr@email.com'}), )
    password    = forms.fields.CharField(
                    max_length = 50, 
                    widget = forms.PasswordInput(attrs={'placeholder':'password'}), )
                    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = UserProfile
        title = "Register"
        description = "Registration is required for at least one team member for entry into the contest. All team members are encouraged to sign up, however, so they can be attributed and show off their work."
        fields = ('first_name', 'last_name', 'email')
        
    def save(self):
        if self.is_valid():
            au = auth.models.User.objects.create_user(username=self.cleaned_data['email'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])
            self.instance.user = au
            self.instance.user.first_name = self.cleaned_data['first_name']
            self.instance.user.last_name = self.cleaned_data['last_name']
            self.instance.user.save()
            ModelForm.save(self)

class LoginForm(ModelForm):
    email       = forms.EmailField(
                    max_length = 100, 
                    widget = forms.TextInput(attrs={'placeholder':'victr@email.com'}), )
    password    = forms.fields.CharField(
                    max_length = 50, 
                    widget = forms.PasswordInput(attrs={'placeholder':'password'}), )
    next        = forms.fields.CharField(
                    max_length=400, 
                    widget=forms.HiddenInput(), )
                    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = UserProfile
        title = "Login"
        description = "Login to add or edit projects."
        fields = ['email']

class ProjectForm(ModelForm):
    #event choices
    eq = EventQuery()
    visible_events = eq.visible()
    events = []
    if visible_events :
        for e in visible_events :
            label = e
            if not e.is_open() :
                label = "%s (CLOSED)" % e
            events.append( (e.pk, { 'label': label, 'disabled': not e.is_open() }) )
    
    #user choices
    users = []
    user_results = UserProfile.objects.filter()
    for userprofile in user_results : 
        users.append( (userprofile, "%s %s - %s" % (userprofile.user.first_name, userprofile.user.last_name, userprofile.user.email)) )
    
    title       = forms.fields.CharField(
                    label = string.capwords(config.keyword('Project.title')),
                    max_length = 100, 
                    widget = forms.TextInput(attrs={ 'placeholder': 'be creative..'}), )
    description = forms.fields.CharField(
                    label = string.capwords(config.keyword('Project.description')),
                    widget = forms.Textarea(attrs={ 'placeholder': 'details..'}), )
    url         = forms.fields.URLField(
                    label = string.capwords(config.keyword('Project.url')),
                    widget = forms.TextInput(attrs={ 'placeholder': 'http://hacks4you.com'}), )
    event       = forms.fields.ChoiceField(
                    label = string.capwords(config.keyword('Event')),
                    choices = events,
                    widget = SelectWithDisabled(), )
    users       = forms.fields.MultipleChoiceField(
                    label = string.capwords(config.keyword('Users')),
                    choices = users,
                    widget = forms.SelectMultiple(attrs={ 'data-placeholder': 'search for %s by name or email' % (config.keyword('Users'),) }), )
    
    def __init__(self, *args, **kwargs):
        # load current user
        self.current_user = kwargs.pop('current_user', None)
        super(ProjectForm, self).__init__(*args, **kwargs)
    
    def clean_event(self):
        """ turns int into Event entity for ze processing """
        return Event.objects.get(pk=int(self.cleaned_data['event']))
        
    def clean_users(self):
        """ makes sure currently logged in user is part of this list """
        data = self.cleaned_data['users']
        if str(self.current_user) not in data:
            self._errors["users"] = self.error_class(["Make sure to include yourself in the %s list!" % config.keyword('Users')])
        return data
    
    class Meta:
        model = Project
        title = "%s Information" % string.capwords(config.keyword('Project'))
        description = "Basic info about your %s, such as title, description, and the involved %s." % (config.keyword('Project'), config.keyword('Users'))
        exclude = ('slug', 'rank', 'award')
        
class PasswordChangeForm(auth.forms.PasswordChangeForm):
    class Meta:
        title = "Password Change"
        description = "Change your password."
