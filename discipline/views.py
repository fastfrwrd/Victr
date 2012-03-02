from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from victr.models import Discipline

def view(request, slug, default_template="discipline/view.html"):

    if request.method == 'GET':
        discipline = get_object_or_404(Discipline, slug=slug)
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET'])