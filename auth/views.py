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
from victr.forms import *
from victr.event.util import EventQuery
from victr.templatetags.victr_tags import joinand
from urllib import quote, unquote
import string

def register(request, default_template="auth/register.html"):
    registration = RegistrationForm()
    if request.method == 'POST' :
        registration = RegistrationForm(request.POST)
        if registration.is_valid() :
            try :
                registration.save()
            except :
                messages = { 'error' : "Whoops! The email address %s is already registered. Try logging in or resetting your password." % (registration.cleaned_data['email'],) }
                forms = [registration]
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
            current_user = auth.authenticate(username=registration.cleaned_data['email'], password=registration.cleaned_data['password'])
            auth.login(request, current_user)
            return redirect( reverse('victr.views.home') )
        else :
            messages = { 'error' : 'Invalid form submission.' }
    forms = [registration]
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def register_modal(request, default_template="auth/register_modal.html"):
    return register(request, default_template)

def login(request, default_template="auth/login.html"):
    if request.method == 'GET' :
        redirect_path = request.GET.get("next")
        login_form = LoginForm(initial = { 'next' : redirect_path })
    elif request.method == 'POST' :
        login_form = LoginForm(request.POST)
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
    forms = [login_form]
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

@login_required
def edit(request, default_template="auth/edit.html"):
    userprofile = UserProfile.objects.get(user=request.user)
    messages = {}
    
    if userprofile and request.method == "GET" :
        userprofile_form = UserProfileForm(instance=userprofile, prefix="userprofile")
        passwordchange_form = PasswordChangeForm(request.user, prefix="passwordchange")
        
    elif userprofile and request.method == "POST" :
        userprofile_form = UserProfileForm(request.POST, instance=userprofile, prefix='userprofile')
        if userprofile_form.is_valid() and userprofile_form.has_changed() :
            userprofile_form.cleaned_data['user'] = request.user
            try :
                userprofile = userprofile_form.save()
                messages['info'] = 'Profile information saved.'
            except :
                messages = { 'error' : 'Invalid form submission. Please contact your site administrator.' }
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
        # check to see if it's empty...
        if request.POST['passwordchange-old_password'] or request.POST['passwordchange-new_password1'] or request.POST['passwordchange-new_password2'] :
            passwordchange_form = PasswordChangeForm(user=request.user, data=request.POST, prefix="passwordchange")
            if passwordchange_form.is_valid() :
                passwordchange_form.save()
                messages['success'] = 'Password successfully changed.'
        else :
            passwordchange_form = PasswordChangeForm(request.user, prefix="passwordchange")

    else :
        return redirect(reverse('victr.views.home'))
        
    forms = [userprofile_form, passwordchange_form]
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))
    
    