from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils import simplejson as json
from victr.models import *


def default(request):

    # create this model
    if request.method == 'POST':
        post = request.POST
        proj = Project()
        proj.name = post['project_title']
        proj.description = post['project_desc']
        proj.main_url = post['project_site_url']
        proj.save()
        proj.tags.clear()
        for tag in post.getlist('project_tags[]'):
            d = Discipline.objects.filter(name=tag)
            if not d:
                d = Discipline(name=tag)
                d.save()
            else:
                d = d[0]
            if d not in proj.tags.all():
                proj.tags.add(d)
        proj.save()
        return redirect('project', slug=proj.slug)

    return HttpResponseNotAllowed(['POST'])


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
        new_tags = post.getlist('project_tags[]')
        for tag in proj.tags.all():
            if tag not in new_tags:
                proj.tags.remove(tag)
        for tag in new_tags:
            d = Discipline.objects.filter(name=tag)
            if not d:
                d = Discipline(name=tag)
                d.save()
            else:
                d = d[0]
            if d not in proj.tags.all():
                proj.tags.add(d)
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


def all(request, default_template="project/all.html"):

    if request.method == 'GET':
        proj = Project.objects.all()
        print proj.count()

    return HttpResponseNotAllowed(['GET'])