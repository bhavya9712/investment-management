# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user
from .forms import LoginForm, SignUpForm
from ..agent.models import agent


def login_view(request):
    user_name = get_user(request)
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    #    if agent.agent_user_id == user.id:
                    #     agent.agent_user_id=request.user.id
                    #     return redirect("/agent/update_agent_Form/",user.id)
                    # else:
                        return redirect("/agent/add_agent_detail")
                    # return redirect("/agent/add_agent_detail")
                else:
                    return redirect("/invest")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.is_staff = eval(form.cleaned_data.get("user_type"))
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            is_staff = form.cleaned_data.get("user_type")
            user = authenticate(username=username, password=raw_password)
            msg = 'User created - please <a href="/login">login</a>.'
            success = True
            result.save()

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
