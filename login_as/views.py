from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404

def chooser(request):
    if not request.user.is_superuser:
        raise Http404
    return render_to_response('login_as/chooser.html',
        {'users': User.objects.all().order_by('username')})

def login(request, username):
    if not request.user.is_superuser:
        raise Http404
    authed = authenticate(from_user=request.user, to_username=username)
    if not authed:
        raise Http404
    auth_login(request, authed)
    return HttpResponseRedirect('/')