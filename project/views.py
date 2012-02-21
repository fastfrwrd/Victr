from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils import simplejson as json
from victr.models import *



def all(request, default_template="project/all.html"):

    pass


def view(request, slug, default_template="project/view.html"):

    proj = get_object_or_404(Project, slug=slug)
    data = {}
    data['project'] = proj
    return render_to_response(default_template, context_instance=RequestContext(request, data))


def edit(request, slug, default_template="project/edit.html"):

    proj = get_object_or_404(Project, slug=slug)
    data = {}
    data['project'] = proj
    return render_to_response(default_template, context_instance=RequestContext(request, data))


def new(request, default_template="project/new.html"):

    # create this model
    if request.method == 'POST':
        post = request.POST
        proj = Project(name=post['project_title'], mainUrl=post['project_site_url'], description=post['project_desc'])
        proj.save()
        return redirect('view', slug=proj.slug)

    if request.method == 'GET':
        return render_to_response(default_template, context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET','POST'])