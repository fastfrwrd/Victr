from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def home(request):
    return render_to_response('root.html', context_instance=RequestContext(request))

def project_new(request):
    return render_to_response('project_new.html', context_instance=RequestContext(request))