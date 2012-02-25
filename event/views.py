# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from victr.models import Event, Project
from victr.event.util import EventQuery

def list(request, default_template="event/list.html"):
    eq = EventQuery()
    events = eq.visible()
    return render_to_response(default_template, context_instance=RequestContext(request, { 'events' : events }))
    
def view(request, slug="", default_template="event/view.html"):
    if(slug is "") :
        eq = EventQuery()
        event = eq.current()
        projects = Project.objects.get(event=event)
    else :
        event = get_object_or_404(Event, slug=slug)
        projects = Project.objects.filter(event=event)
    return render_to_response(default_template, context_instance=RequestContext(request, { 'event' : event, 'projects' : projects }))