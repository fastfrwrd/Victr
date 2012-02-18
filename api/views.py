from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson as json
from django.core import serializers
from django.core.urlresolvers import reverse
from victr.models import *


def project(request):

    # create this model
    if request.method == 'POST':
        post = request.POST
        proj = Project(name=post['project_title'], mainUrl=post['project_site_url'], description=post['project_desc'])
        proj.save()
        data = { 'location': reverse('view', args=(proj.slug,)) }
        return HttpResponse(json.dumps(data))

    return HttpResponseNotAllowed()


def project_id(request, slug):

    proj = get_object_or_404(Project, slug=slug)

    # update this model
    if request.method == 'PUT':
        put = request.PUT
        proj.name = put['project_title']
        proj.mainUrl = put['project_site_url']
        proj.description = put['project_desc']
        proj.save()
        data = { 'location': reverse('view', args=(proj.slug,)) }
        return HttpResponse(json.dumps(data))

    elif request.method == 'GET':

        return HttpResponse(serializers.serialize('json', proj))

    elif request.method == 'DELETE':

        pass

    return HttpResponseNotAllowed()