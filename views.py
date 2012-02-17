from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from victr.models import *

def home(request):
    return render_to_response('root.html', context_instance=RequestContext(request))

def project_view(request, slug):
    return render_to_response('project_view.html', context_instance=RequestContext(request))

def project_new(request):

    if request.method == 'GET':
        return render_to_response('project_new.html', context_instance=RequestContext(request))

    if request.method == 'POST':
        post = request.POST
        proj = Project(name=post['project_title'], mainUrl=post['project_site_url'])
        proj.save()
        print proj.slug
        data = { 'location': reverse('project_view', args=(proj.slug,)) }
        return HttpResponse(json.dumps(data))

    return HttpResponseNotAllowed()

def impress_present(request):
    return render_to_response('impress_present.html', context_instance=RequestContext(request))
