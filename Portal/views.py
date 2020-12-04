from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import LoginForm, RegisterForm


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
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


def register(request):
    if (request.session.has_key('id')):
        uid = int(request.session['id'])
        user = User.objects.get(
            userid=uid)
        if user.userrole == 'SUPERUSER':
            if request.method == 'POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                    uname = form.cleaned_data['username']
                    pword = form.cleaned_data['password']
                    cword = form.cleaned_data['confirm_password']
                    urole = form.cleaned_data['userrole']
                    if pword == cword:
                        userexist = User.objects.filter(
                            username=uname).exists()
                        if userexist:
                            messages.error(request, "Username already exists!")
                        else:
                            User(username=uname, password=pword,
                                 userrole=urole).save()
                            return HttpResponseRedirect('/register')
                    else:
                        messages.error(request, "Password did not match!")
                else:
                    messages.error(request, "Invalid Input data!")
            else:
                form = RegisterForm()

        return render(request, 'register.html', {'form': form.as_p, 'loginuser': user.username, 'userrole': user.userrole})

    else:
        return HttpResponseRedirect('/login')


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
            return render(request, 'link.html', {'data': data, 'loginuser': user.username, 'userrole': user.userrole})
    else:
        return HttpResponseRedirect('/login')


def help(request):
    if (request.session.has_key('id')):
        uid = int(request.session['id'])
        user = User.objects.get(
            userid=uid)
        if user and request.method == 'GET':
            return render(request, 'help.html', {'loginuser': user.username, 'userrole': user.userrole})
    else:
        return HttpResponseRedirect('/login')
