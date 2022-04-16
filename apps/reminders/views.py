from datetime import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Subquery
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from core import settings
from .forms import ReminderForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Reminders
from ..home.models import CustomUser
from ..investment.models import Investment


@login_required(login_url="/login/")
def reminderindex(request):
    data = Reminders.objects.filter(Reminder_user_id=request.user.id)
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "Reminder/Reminder.html", {'reminders': page_obj})


@login_required(login_url="/login/")
def agentreminder(request, pk):
    data = Reminders.objects.filter(Reminder_user_id_id=pk)
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "Reminder/ClientReminder.html", {'reminders': page_obj})


def family_reminder(request, pk):
    data = Reminders.objects.filter(Reminder_user_id=pk)
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "Reminder/FamilyReminder.html", {'reminders': page_obj})


# def reminderindex(request):
#
#     # data = Reminders.objects.filter(Reminder_user_id=Subquery(users.values('id')))
#     data = Reminders.objects.filter(Reminder_user_id=request.user.id)
#     return render(request, "Reminder/Reminder.html", {'reminders': data})
#


@login_required(login_url="/login/")
def addReminderForm(request, pk):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.Reminder_Investment_id = Investment.objects.get(pk=pk)
            result.Reminder_user_id = request.user
            result.save()
            return redirect('/invest')
    else:
        form = ReminderForm()
    return render(request, "Reminder/addReminder.html", {'form': form})


from celery.schedules import crontab
from celery.task import periodic_task

from celery.schedules import crontab


@periodic_task(run_every=(crontab(minute='*/1')), name="every_monday_morning", ignore_result=True)  # Runs every 5 minute
def every_monday_morning():
    print("This is run every Monday morning at 7:30")


def sendreminderemail(request):
    every_monday_morning()
    myreminder = Reminders.objects.filter(Reminder_date=datetime.now()).all()
    for reminders in myreminder:
        print(reminders.Reminder_user_id.email)
        subject = "Reminder"
        message = "Hello " + reminders.Reminder_user_id.username+"your investment type : " + reminders.Reminder_Investment_id.investmenttype + "\n Investment Company : "+reminders.Reminder_Investment_id.investmentcompany + "\n Amount :"+reminders.Reminder_Investment_id.investment_amount+"\n reminder : "+reminders.Reminder_description
        from_email = settings.EMAIL_HOST_USER
        to_list = [reminders.Reminder_user_id.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

    print("email sent")
    return redirect('/agent/')


@login_required(login_url="/login/")
def addClientReminderForm(request, pk):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.Reminder_Investment_id = Investment.objects.filter(investmentid=pk).first()

            result.Reminder_user_id =CustomUser.objects.get(id__in =Investment.objects.filter(investmentid=pk).values('investment_user_id'))
            print(result.Reminder_user_id)
            result.save()
            return redirect('/agent/')
    else:
        form = ReminderForm()
    return render(request, "Reminder/addClientReminder.html", {'form': form})


@login_required(login_url="/login/")
def updateReminderForm(request, pk):
    article = Reminders.objects.get(pk=pk)

    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/reminders')
    else:
        form = ReminderForm(instance=article)
    return render(request, "Reminder/addReminder.html", {'form': form})

@ login_required(login_url="/login/")
def updateClientReminderForm(request, pk):
    article = Reminders.objects.get(pk=pk)

    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/agent/')
    else:
        form = ReminderForm(instance=article)
    return render(request, "Reminder/addClientReminder.html", {'form': form})


@login_required(login_url="/login/")
def deleteReminder(request, pk):
    article = Reminders.objects.get(pk=pk)
    article.delete()
    return redirect('/reminders')

@login_required(login_url="/login/")
def agentdeleteReminder(request, pk):
    article = Reminders.objects.get(pk=pk)
    article.delete()
    return redirect('/agent')