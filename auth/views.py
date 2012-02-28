from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils import simplejson as json
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from victr.models import *
from victr.event.util import EventQuery
from victr.forms import RegistrationForm, LoginForm
from urllib import quote, unquote


def register(request, default_template="auth/register.html"):
    form = RegistrationForm()
    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid() :
            try :
                form.save()    #user registered
            except : #IntegrityError as detail :
                messages = { 'error' : "Whoops! The email address %s is already registered. Try logging in or resetting your password." % (form.cleaned_data['email'],) }
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
            current_user = auth.authenticate(username=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
            auth.login(request, current_user)
            return redirect( reverse('victr.views.home') )
        else :
            messages = { 'warning' : 'Invalid form submission.' }
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def register_modal(request, default_template="auth/register_modal.html"):
    return register(request, default_template)



def login(request, default_template="auth/login.html"):
    redirect_path = ''
    if request.method == 'GET' :
        redirect_path = request.GET.get("next")
    form = LoginForm(initial = { 'next' : redirect_path })
    if request.method == 'POST' :
        form = LoginForm(request.POST)
        redirect_path = unquote(request.POST.get('next'))
        current_user = auth.authenticate(username=request.POST.get('email'),
            password=request.POST.get('password'))
        if current_user is not None :
            if current_user.is_active :
                auth.login(request, current_user)
                return redirect(''.join( ( reverse('victr.views.home'), redirect_path ) ))
            else :
                messages = { "warning" : "Your account has been disabled. Please contact the site administrator." }
        else :
            messages = { "error" : "Invalid username or password. Please try again, or if you are having trouble, reset your password." }
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def login_nav(request, default_template="auth/login_nav.html"):
    return login(request, default_template)


def logout(request):
    auth.logout(request)
    # add a message object to display as a notification of logout on the top part of the page
    return redirect(reverse('victr.views.home'))