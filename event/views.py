# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from victr.models import Event, Project
from victr.event.util import EventQuery
from datetime import datetime

def all(request, default_template="event/all.html"):
    eq = EventQuery()
    events = eq.visible()
    return render_to_response(default_template, context_instance=RequestContext(request, { 'events' : events }))
    
def view(request, slug="", default_template="event/view.html"):
    if(slug is "") :
        eq = EventQuery()
        event = eq.current()
    else :
        event = get_object_or_404(Event, slug=slug)
    if not event.is_visible :
        raise Http404
    projects = Project.objects.filter(event=event)
    return render_to_response(default_template, context_instance=RequestContext(request, { 'event' : event, 'projects' : projects }))