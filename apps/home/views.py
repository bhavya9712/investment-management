# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect

from apps.home.forms import ProfileUpdateForm
from apps.home.models import CustomUser


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def view_family(request):
    try:
        article = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        article = None
    if article:
        data = CustomUser.objects.get(username=request.user).clients_family
        user_name = get_user(request)
        # client_id = agent_client.objects.filter(agent_id=request.user.id).select_related()
        return render(request, "home/viewfamily.html", {'clients': data})
    else:
        return redirect("add_agent_detail")


def add_family(request):
    if request.method == 'POST':
        user_name = get_user(request)

        user_name.clients_family.add(CustomUser.objects.get(email=request.POST.get("clients_family")))
        user_name.save()


        return redirect('/viewfamily')

    return render(request, "home/addfamily.html")


def profile(request):
    return render(request, "home/profile.html")


def updateProfileForm(request):
    try:
        article = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        article = None
    # article = agent.objects.get(agent_user_id_id=request.user.id)
    if article:
        if request.method == 'POST':
            file_data=request.FILES or None

            form = ProfileUpdateForm(request.POST, file_data, request.FILES,instance=article)
            if form.is_valid():
                result = form.save(commit=False)
                result.id = request.user.id
                result.save()
                return redirect('/profile')
        else:
            form = ProfileUpdateForm(instance=article)
        return render(request, "home/profile.html", {'form': form})
    else:
        if request.method == 'POST':
            user_name = get_user(request)
            form = ProfileUpdateForm(request.POST, user_name)
            if form.is_valid():
                result = form.save(commit=False)
                result.id = request.user.id

                result.save()
                return redirect('/profile')
        else:
            form = ProfileUpdateForm()
        return render(request, "home/profile.html", {'form': form})


# def updateProfileForm(request):
#     article = CustomUser.objects.get(pk=request.user.id)
#
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, instance=article)
#         if form.is_valid():
#             form.save()
#             return redirect('home/profile.html')
#     else:
#         form = ProfileUpdateForm(instance=article)
#     return render(request, "home/profile.html", {'form': form})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
