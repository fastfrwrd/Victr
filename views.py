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
import calendar

def home(request, default_template="event/view.html"):
    """
    very similar to victr.event.views.view, but we need this to reverse back properly to use {% victr_base %}
    """
    eq = EventQuery()
    event = eq.current()
    projects = []
    if(event):
        projects = Project.objects.filter(event=event)
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def archive(request, default_template="archive.html"):
    eq = EventQuery()
    events = eq.visible()
    grouped_events = {}
    
    for event in events:
        date = event.open.date()
        year = date.year
        month = date.month
        if year not in grouped_events:
            grouped_events[year] = {}
        if month not in grouped_events[year]:
            grouped_events[year][month] = { 'month': calendar.month_name[month], 'events': [] }
        print grouped_events[year][month]
        grouped_events[year][month]['events'].append(event)
    
    print grouped_events
        
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))
