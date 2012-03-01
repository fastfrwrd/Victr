from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils import simplejson as json
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from victr.models import *
from victr.event.util import EventQuery
from victr.forms import RegistrationForm, LoginForm, UserProfileForm
from victr.templatetags.victr_tags import joinand
from urllib import quote, unquote
import string

def register(request, default_template="auth/register.html"):
    form = RegistrationForm()
    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid() :
            try :
                form.save()
            except :
                messages = { 'error' : "Whoops! The email address %s is already registered. Try logging in or resetting your password." % (form.cleaned_data['email'],) }
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
            current_user = auth.authenticate(username=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
            auth.login(request, current_user)
            return redirect( reverse('victr.views.home') )
        else :
            messages = { 'error' : 'Invalid form submission.' }
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def register_modal(request, default_template="auth/register_modal.html"):
    return register(request, default_template)

def login(request, default_template="auth/login.html"):
    # todo: handle case where we shouldn't redirect if we are on a page like 'archive' after we log in.
    if request.method == 'GET' :
        redirect_path = request.GET.get("next")
        form = LoginForm(initial = { 'next' : redirect_path })
    elif request.method == 'POST' :
        form = LoginForm(request.POST)
        redirect_path = unquote(request.POST.get('next'))
        if not redirect_path:
            redirect_path = reverse('victr.views.home')
        current_user = auth.authenticate(username=request.POST.get('email'),
            password=request.POST.get('password'))
        if current_user is not None :
            if current_user.is_active :
                auth.login(request, current_user)
                return redirect( redirect_path )
            else :
                messages = { "warning" : "Your account has been disabled. Please contact the site administrator." }
        else :
            messages = { "error" : "Invalid username or password. Please try again, or if you are having trouble, reset your password." }
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def login_nav(request, default_template="auth/login_nav.html"):
    return login(request, default_template)

def logout(request):
    auth.logout(request)
    # todo: add a message object to display as a notification of logout on the top part of the page
    return redirect(reverse('victr.views.home'))

def profile(request, id=None, default_template="auth/profile.html"):
    #grab the appropriate user profile
    userprofile = False
    if id :
        print id
        userprofile = UserProfile.objects.get(pk=id)
    elif request.user.is_authenticated() :
        userprofile = UserProfile.objects.get(user=request.user)
        
    #building the displayed profile values
    if userprofile :
        dict = model_to_dict(userprofile)
        profile = []
        for key in UserProfile.profile :
            if key in dict.keys() and dict[key] :
                if isinstance(dict[key], list): #check for array values, turn into strings
                    dict[key] = joinand(dict[key], ", ")
                profile.append({'label' : string.capwords(key), 'value' : dict[key]})
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))
    return redirect(reverse('victr.auth.views.login'))

def edit(request, default_template="auth/edit.html"):
    if request.user.is_authenticated() :    
        userprofile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(request.user)
        if userprofile:
            return render_to_response(default_template, locals(), context_instance=RequestContext(request))
    return redirect(reverse('victr.auth.views.login'))
    
    