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

def home(request, default_template="event/view.html"):
    """
    very similar to victr.event.views.view, but we need this to reverse back properly to use {% victr_base %}
    """
    eq = EventQuery()
    event = eq.current()
    projects = []
    if(event):
        projects = Project.objects.filter(event=event)
    return render_to_response(default_template, context_instance=RequestContext(request, { 'event' : event, 'projects' : projects }))




@login_required
def projects(request, default_template="auth/projects.html"):
    """
    Grab all projects associated with a user, list them with their event
    """
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))
    
@login_required
def account(request, default_template="auth/account.html"):
    """
    the account of a user. if user is currently logged in user, should return
    a form. should respond to POST and GET.
    """
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))
    
