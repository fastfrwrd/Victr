from django import forms
from django.forms import ModelForm, Form
from victr.models import UserProfile
from django.contrib import auth
from django.db import models

class RegistrationForm(ModelForm):
    """
    Attributes defined here are found in RegistrationForm.fields
    It seems that the reason we have fields specified below as attributes is because
    this form has to gather information for both auth.User and victr.UserProfile
    """
    first_name = forms.fields.CharField(max_length=25)
    last_name = forms.fields.CharField(max_length=25)
    email = forms.EmailField(max_length=100)
    password = forms.fields.CharField(max_length=50, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
    class Meta:
        model = UserProfile
        """
        exclude = ('')
        """
        fields = ('first_name', 'last_name', 'email')
    def save(self):
        if self.is_valid():
            au = auth.models.User.objects.create_user(username=self.cleaned_data['email'],
                                                      email=self.cleaned_data['email'],
                                                      password=self.cleaned_data['password'])
            self.instance.user = au
            self.instance.user.first_name = self.cleaned_data['first_name']
            self.instance.user.last_name = self.cleaned_data['last_name']
            self.instance.user.save()
            print "self.instance: " + str(self.instance)
            ModelForm.save(self)
            print "should have just saved\n"
