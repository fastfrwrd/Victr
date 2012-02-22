from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils import simplejson as json
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from victr.models import *
from victr.forms import RegistrationForm

def register(request):
    registration_form = RegistrationForm()
    if request.method == 'POST' :
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid() :
            try :
                registration_form.save()    #user registered
            except : #IntegrityError as detail :
                print "username already registered we need to handle that gracefully"
                return render_to_response("register.html", locals(), context_instance=RequestContext(request))
            current_user = auth.authenticate(username=registration_form.cleaned_data['email'],
                                             password=registration_form.cleaned_data['password'])
            auth.login(request, current_user)
            return redirect('/vip')
    return render_to_response("register.html", locals(), context_instance=RequestContext(request))

def login(request):
    """
    temporary placement of login view function.
    username handling code goes here
    ?next get variable handling can also go here
    """
    return HttpResponse("Login Please", {})

def logout(request):
    auth.logout(request)
    return HttpResponse("Logged out.", {})

@login_required
def vip(request):
    """
    temporary placement of hypothetical page with restricted access
    """
    return HttpResponse("Secret Magical Page", {})
