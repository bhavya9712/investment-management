from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from apps.agent.forms import add_clientForm, add_agent_details_Form
from apps.agent.models import agent
from apps.home.forms import ProfileUpdateForm
from apps.home.models import CustomUser


@login_required(login_url="/login/")
def view_clients(request):
    try:
        article = agent.objects.get(agent_user_id_id=request.user.id)
    except agent.DoesNotExist:
        article = None
    if article:
        data = agent.objects.get(agent_user_id=request.user).agent_clients
        user_name = get_user(request)
         # client_id = agent_client.objects.filter(agent_id=request.user.id).select_related()
        return render(request, "agent/viewclients.html", {'clients': data})
    else:
        return redirect("add_agent_detail")


def updateProfileForm(request):
    try:
        article = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        article = None
    if article:
        if request.method == 'POST':
            file_data = request.FILES or None
            form = ProfileUpdateForm(request.POST, file_data, request.FILES,instance=article)
            if form.is_valid():
                result = form.save(commit=False)
                result.id = request.user.id
                result.save()
                return redirect('/agent/agentprofile')
        else:
            form = ProfileUpdateForm(instance=article)
        return render(request, "agent/profile.html", {'form': form})
    else:
        if request.method == 'POST':
            user_name = get_user(request)
            form = ProfileUpdateForm(request.POST, user_name)
            if form.is_valid():
                result = form.save(commit=False)
                result.id = request.user.id
                result.save()
                return redirect('/agent/agentprofile')
        else:
            form = ProfileUpdateForm()
        return render(request, "agent/profile.html", {'form': form})

@login_required(login_url="/login/")
def add_client(request):
    if request.method == 'POST':
        user_name = get_user(request)
        form = add_clientForm(request.POST, instance=agent.objects.get(agent_user_id=request.user))
        if form.is_valid():
            form.save()

            return redirect('/agent')
    else:
        form = add_clientForm(instance=agent.objects.get(agent_user_id=request.user))
    return render(request, "agent/addclient.html", {'form': form})


@login_required(login_url="/login/")
def add_agent_details(request):

    try:
        article = agent.objects.get(agent_user_id_id=request.user.id)
    except agent.DoesNotExist:
        article = None
    # article = agent.objects.get(agent_user_id_id=request.user.id)
    if article:
        if request.method == 'POST':
            form = add_agent_details_Form(request.POST, instance=article)
            if form.is_valid():
                result = form.save(commit=False)
                result.agent_user_id = request.user
                result.save()
                return redirect('/agent/add_agent_detail')
        else:
            form = add_agent_details_Form(instance=article)
        return render(request, "agent/addagent.html", {'form': form})
    else:
        if request.method == 'POST':
            user_name = get_user(request)
            form = add_agent_details_Form(request.POST, user_name)
            if form.is_valid():
                result = form.save(commit=False)
                result.agent_user_id = request.user
                result.save()
                return redirect('/agent')
        else:
            form = add_agent_details_Form()
        return render(request, "agent/addagent.html", {'form': form})


def profile(request):
    return render(request, "agent/profile.html")


@login_required(login_url="/login/")
def update_agent_Form(request):
    article = agent.objects.get(pk=request.user.id)

    if request.method == 'POST':
        form = add_agent_details_Form(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/agent')
    else:
        form = add_agent_details_Form(instance=article)
    return render(request, "/agent/addagent.html", {'form': form})