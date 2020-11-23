from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import LoginForm


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            uname = form.cleaned_data['username']
            pword = form.cleaned_data['password']
            userexist = User.objects.filter(
                username=uname, password=pword).exists()
            if userexist:
                user = User.objects.get(
                    username=uname)
                request.session.flush()
                request.session['id'] = str(user.userid)
                return HttpResponseRedirect('/link')
            else:
                messages.error(request, "Invalid Username or Password!")
        else:
            messages.error(request, "Invalid Username or Password!")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form.as_p})


def logout(request):

    if request.method == 'GET':
        request.session.flush()
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/login')


def link(request):
    if (request.session.has_key('id')):
        uid = int(request.session['id'])
        user = User.objects.get(
            userid=uid)
        if user.userrole == 'SUPERUSER':
            rows = Link.objects.filter().order_by("linkid")
        else:
            rows = Link.objects.filter(
                userrole=user.userrole).order_by("linkid")
        data = []
        for row in rows:
            link = {'id': row.linkid, "appname": row.appname,
                    "url": row.url, "category": row.category}
            data.append(link)

        if request.method == 'GET':
            return render(request, 'link.html', {'data': data, 'loginuser': user.username})
    else:
        return HttpResponseRedirect('/login')


def help(request):
    if (request.session.has_key('id')):
        uid = int(request.session['id'])
        user = User.objects.get(
            userid=uid)
        if user and request.method == 'GET':
            return render(request, 'help.html', {'loginuser': user.username})
    else:
        return HttpResponseRedirect('/login')
