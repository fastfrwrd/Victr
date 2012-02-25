# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from victr.models import Event, Project
from victr.event.util import EventQuery

def present(request, slug="", default_template="impress/present.html"):
    if(slug is "") :
        eq = EventQuery()
        event = eq.current()
    else :
        event = get_object_or_404(Event, slug=slug)
    projects = Project.objects.filter(event=event)
    return render_to_response(default_template, context_instance=RequestContext(request, { 'event' : event, 'projects' : projects }))
