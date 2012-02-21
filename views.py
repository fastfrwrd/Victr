from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson as json
from django.core import serializers
from django.core.urlresolvers import reverse
from victr.models import *
from django.contrib.auth.decorators import login_required

@login_required
def vip(request):
    """
    temporary placement of hypothetical page with restricted access
    """
    return HttpResponse("Secret Magical Page", {})

def login(request):
    """
    temporary placement of login view function.
    username handling code goes here
    ?next get variable handling can also go here
    """
    return HttpResponse("Login Please", {})
