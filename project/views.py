from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils import simplejson as json
from victr.models import *


def default(request):

    # create this model
    if request.method == 'POST':
        post = request.POST
        proj = Project(name=post['project_title'], mainUrl=post['project_site_url'], description=post['project_desc'])
        proj.save()
        return redirect('project', slug=proj.slug)

    return HttpResponseNotAllowed(['POST'])


def all(request, default_template="project/all.html"):

    if request.method == 'GET':
        pass

    return HttpResponseNotAllowed(['GET'])


def project(request, slug, default_template="project/view.html"):

    proj = get_object_or_404(Project, slug=slug)

    if request.method == 'GET':
        data = {}
        data['project'] = proj
        return render_to_response(default_template, context_instance=RequestContext(request, data))

    if request.method == 'POST':
        post = request.POST
        proj.name = post['project_title']
        proj.mainUrl = post['project_site_url']
        proj.description = post['project_desc']
        proj.save()
        return redirect('project', slug=proj.slug)

    return HttpResponseNotAllowed(['GET','POST'])


def edit(request, slug, default_template="project/edit.html"):

    proj = get_object_or_404(Project, slug=slug)
    data = {}
    data['project'] = proj
    return render_to_response(default_template, context_instance=RequestContext(request, data))


def new(request, default_template="project/new.html"):

    if request.method == 'GET':
        return render_to_response(default_template, context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET'])