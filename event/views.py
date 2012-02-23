# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from victr.models import Event

def list(request, default_template="event/list.html"):
    event = Event(name="Event name here")
    return render_to_response(default_template, context_instance=RequestContext(request, { 'event' : event }))