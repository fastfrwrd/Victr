# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from victr.models import Event, Project
from victr.event.util import EventQuery
from datetime import datetime
    
def view(request, slug="", default_template="event/view.html"):
    if(slug is "") :
        eq = EventQuery()
        event = eq.current()
    else :
        event = get_object_or_404(Event, slug=slug)
    if not event.is_visible :
        raise Http404
    if event.show_results :
        try: 
            top_projects = Project.objects.filter(event=event, rank__isnull=False).order_by('rank')[:3]
        except IndexError :
            top_projects = False
        try:
            winner = Project.objects.filter(event=event, rank__isnull=False).order_by('rank')[0]
        except IndexError:
            winner = False
        awards = Project.objects.filter(award__isnull=False).exclude(award='')
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))