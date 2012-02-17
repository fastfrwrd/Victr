# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def present(request, default_template="impress/present.html"):
    return render_to_response(default_template, context_instance=RequestContext(request))
