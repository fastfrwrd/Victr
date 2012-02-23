from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils import simplejson as json
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from victr.models import *
from victr.forms import RegistrationForm, LoginForm

def home(request, default_template="event/open.html"):
    event = Event(name="Event name here")
    return render_to_response(default_template, context_instance=RequestContext(request, { 'event' : event }))

def register(request, default_template="auth/register_page.html"):
    form = RegistrationForm()
    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid() :
            try :
                form.save()    #user registered
            except : #IntegrityError as detail :
                messages = { 'error' : "Whoops! The email address %s is already registered. Try logging in or resetting your password." % (form.cleaned_data['email'],) }
                return render_to_response(default_template, locals(), context_instance=RequestContext(request, { 'messages' : messages }))
            current_user = auth.authenticate(username=form.cleaned_data['email'],
                                             password=form.cleaned_data['password'])
            auth.login(request, current_user)
            return redirect(''.join(reverse('victr.views.home'), 'vip'))
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def login(request, default_template="auth/login_page.html"):
    form = LoginForm()
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    # add a message object to display as a notification of logout on the top part of the page
    return redirect(reverse('victr.views.home'))

@login_required
def vip(request):
    """
    temporary placement of hypothetical page with restricted access
    """
    return HttpResponse("Secret Magical Page", {})
