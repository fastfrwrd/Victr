from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from victr.event.util import EventQuery
from victr.forms import *
from victr.models import *

def project(request, slug, default_template="project/view.html"):

    if request.method == 'GET':
        project = get_object_or_404(Project, slug=slug)
        if request.user.is_authenticated() :
            current_user = UserProfile.objects.get(user=request.user)
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET'])

@login_required
def edit(request, slug, default_template="project/edit.html"):

    project = get_object_or_404(Project, slug=slug)
    current_user = UserProfile.objects.get(user = request.user)
    
    if(current_user not in project.users.all() and not request.user.is_staff):
        messages = { 'warning' : 'Access denied: you do not have permission to view this form.' }
    
    if request.method == 'GET':
        project_form = ProjectForm(instance = project)

    elif request.method == 'POST':
        project_form = ProjectForm(request.POST, instance = project, current_user=current_user)
        if form.is_valid() :
            try :
                project = form.save()
            except :
                messages = { 'error' : 'Invalid form submission. Please contact your site administrator.' }
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
            return redirect('project', project.slug)
        messages = { 'error': 'Invalid form submission. Please correct the indicated fields below before proceeding.' }
 
    else:
        return HttpResponseNotAllowed(['GET','POST'])
    
    forms = [project_form]
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    

@login_required
def new(request, default_template="project/new.html"):
    
    # grab the current event and check to see if it's actually open.
    eq = EventQuery()
    event = eq.current()
    
    if not event or not event.is_open() :
        messages = { 'warning' : 'There is currently no event open for submission.' }
        return redirect(reverse('victr.views.home'), locals())
    
    current_user = UserProfile.objects.get(user=request.user)
    
    if request.method == 'GET':
      project_form = ProjectForm(initial = {'event' : event, 'users' : [current_user]}) # the current event is preselected.
    
    elif request.method == 'POST':
        project_form = ProjectForm(request.POST, current_user=current_user)
        if form.is_valid() :
            try :
                proj = form.save()
            except :
                messages = { 'error' : 'Invalid form submission. Please contact your site administrator.' }
                return render_to_response(default_template, locals(), context_instance=RequestContext(request))
            return redirect('project', proj.slug)
        messages = { 'error': 'Invalid form submission. Please correct the indicated fields below before proceeding.' }

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    forms = [project_form]
    return render_to_response(default_template, locals(), context_instance=RequestContext(request))

def all(request, default_template="project/all.html"):

    if request.method == 'GET':
        projects = Project.objects.all()
        return render_to_response(default_template, locals(), context_instance=RequestContext(request))

    return HttpResponseNotAllowed(['GET'])