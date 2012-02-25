from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils import simplejson as json
from victr.forms import ProjectForm
from victr.models import *


def project(request, slug, default_template="project/view.html"):

    project = get_object_or_404(Project, slug=slug)

    if request.method == 'GET':
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, instance = project)
        if project_form.is_valid() :
            try :
                project = project_form.save()
            except :
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
            return redirect('project', project.slug)
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET','POST'])


def edit(request, slug, default_template="project/edit.html"):
    
    if request.method == 'GET':
        project = Project.objects.get(slug=slug)
        project_form = ProjectForm(instance = project)
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET'])


def new(request, default_template="project/new.html"):
    
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid() :
            try :
                proj = project_form.save()
            except :
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
            return redirect('project', proj.slug)
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    if request.method == 'GET':
        project_form = ProjectForm()
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET', 'POST'])


def all(request, default_template="project/all.html"):

    if request.method == 'GET':
        projects = Project.objects.all()
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET'])