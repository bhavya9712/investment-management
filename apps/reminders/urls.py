"""demo3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminderindex, name="reminders"),
    path('addClientReminder/<str:pk>', views.addClientReminderForm, name="addClientReminderForm"),
    path('addReminder/<str:pk>', views.addReminderForm, name="addReminderForm"),
    path('updateReminderForm/<str:pk>', views.updateReminderForm, name="updateReminderForm"),
    path('updateClientReminderForm/<str:pk>', views.updateClientReminderForm, name="updateClientReminderForm"),
    path('view_agent_reinder/<str:pk>',views.agentreminder,name="agentreminder"),
    path('family_reminder/<str:pk>',views.family_reminder,name="familyreminder"),
    path('emailreminder/',views.sendreminderemail,name="emailreminder"),
    path('deleteReminder/<str:pk>', views.deleteReminder, name="deleteReminder"),
    path('agentdeleteReminder/<str:pk>', views.agentdeleteReminder, name="agentdeleteReminder"),
    path("logout/", LogoutView.as_view(), name="logout")

]
