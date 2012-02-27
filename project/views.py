from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from victr.event.util import EventQuery
from victr.forms import ProjectForm
from victr.models import *

def project(request, slug, default_template="project/view.html"):

    if request.method == 'GET':
        project = get_object_or_404(Project, slug=slug)
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET'])

@login_required
def edit(request, slug, default_template="project/edit.html"):

    project = get_object_or_404(Project, slug=slug)
    
    if request.method == 'GET':
        form = ProjectForm(instance = project)
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid() :
            try :
                project = project_form.save()
            except :
                messages = { 'error' : 'Invalid form submission. Please contact your site administrator.' }
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
            return redirect('project', project.slug)
        messages = { 'error': 'Invalid form submission. Please correct the indicated fields below before proceeding.' }
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET','POST'])

@login_required
def new(request, default_template="project/new.html"):
    
    # grab the current event and check to see if it's actually open.
    eq = EventQuery()
    event = eq.current()
    if not event or not event.is_open() :
        messages = { 'warning' : 'There is currently no event open for submission.' }
        return redirect(reverse('victr.views.home'), locals())
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid() :
            try :
                proj = form.save()
            except :
                messages = { 'error' : 'Invalid form submission. Please contact your site administrator.' }
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
            return redirect('project', proj.slug)
        messages = { 'error': 'Invalid form submission. Please correct the indicated fields below before proceeding.' }
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    if request.method == 'GET':
        form = ProjectForm(initial = {'event' : event}) # the current event is preselected.
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET', 'POST'])


def all(request, default_template="project/all.html"):

    if request.method == 'GET':
        projects = Project.objects.all()
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET'])