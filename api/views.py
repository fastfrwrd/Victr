#from django.http import HttpResponse, HttpResponseNotAllowed
#from django.shortcuts import render_to_response
#from django.template import RequestContext
#from django.utils import simplejson as json
#from django.core import serializers
#from django.core.urlresolvers import reverse
#from django.db.models.loading import get_model
#from victr.models import *
#
#MODELS = {
#    'project' : 'Project'
#}
#
#def rest(request, object):
#
#    Model = get_model('victr', MODELS[object]);
#
#    if request.method == 'POST':
#        post = request.POST
#        obj = Model()
#        print post.lists()
#        pass
#
#
#def rest_id(request, object, slug):
#
#    Model = get_model('victr', MODELS[object]);
#    obj = Model.objects.filter(slug=slug)
#
#    if request.method == 'GET':
#        print obj
#
##def project(request):
##
##    # create this model
##    if request.method == 'POST':
##        post = request.POST
##        proj = Project(name=post['project_title'], mainUrl=post['project_site_url'], description=post['project_desc'])
##        proj.save()
##        data = { 'location': reverse('view', args=(proj.slug,)) }
##        return HttpResponse(json.dumps(data))
##
##    return HttpResponseNotAllowed(['POST'])
##
##
##def project_id(request, slug):
##
##    proj = Project.objects.filter(slug=slug)
##
##    # update this model
##    if request.method == 'PUT':
##        put = request.PUT
##        proj.name = put['project_title']
##        proj.mainUrl = put['project_site_url']
##        proj.description = put['project_desc']
##        proj.save()
##        data = { 'location': reverse('view', args=(proj.slug,)) }
##        return HttpResponse(json.dumps(data))
##
##    elif request.method == 'GET':
##
##        return HttpResponse(serializers.serialize('json', proj))
##
##    elif request.method == 'DELETE':
##
##        pass
##
##    return HttpResponseNotAllowed(['PUT','GET','DELETE'])