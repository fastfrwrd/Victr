from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils import simplejson as json
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from victr.models import *
from victr.forms import RegistrationForm

def home(request, default_template="event/open.html"):
    event = Event(name="Event name here")
    return render_to_response(default_template, context_instance=RequestContext(request, { 'event' : event }))

def register(request, default_template="auth/register_page.html"):
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
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def login(request, default_template="auth/login_page.html"):
    """
    temporary placement of login view function.
    username handling code goes here
    ?next get variable handling can also go here
    """
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

@login_required
def logout(request):
    auth.logout(request)
    # add a message object to display as a notification of logout on the top part of the page
    return HttpResponseRedirect(reverse('victr.views.home'), {})

@login_required
def vip(request):
    """
    temporary placement of hypothetical page with restricted access
    """
    return HttpResponse("Secret Magical Page", {})
