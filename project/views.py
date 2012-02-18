from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from victr.models import *

def view(request, slug, default_template="project/view.html"):
    return render_to_response(default_template, context_instance=RequestContext(request))

def new(request, default_template="project/new.html"):

    if request.method == 'GET':
        return render_to_response(default_template, context_instance=RequestContext(request))

    if request.method == 'POST':
        post = request.POST
        proj = Project(name=post['project_title'], mainUrl=post['project_site_url'])
        proj.save()
        data = { 'location': reverse('view', args=(proj.slug,)) }
        return HttpResponse(json.dumps(data))

    return HttpResponseNotAllowed()