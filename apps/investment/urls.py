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
    path('', views.invest),
    path('add', views.addInvestForm, name="addInvestForm"),
    path('venue_pdf', views.users_investment_pdf_view, name="venue_pdf"),
    path('investment_pdf/<str:pk>', views.agent_client_investment_pdf_view, name="investment_pdf"),
    path('familyinvestments/<str:pk>', views.viewfamilyinvestments, name="familyinvestments"),
    path('viewclientinv/<str:pk>', views.viewclientInvestment, name="viewclientInvestment"),
    path('addclientinv/<str:pk>', views.addclientInvestForm, name="addclientInvestForm"),
    path('delete/<str:pk>', views.deleteInvest, name="deleteInvestment"),
    path('agentdeleteinvest/<str:pk>', views.agentdeleteInvest, name="agentdeleteinvest"),
    path('viewInvestment', views.invest, name="invest"),
    path('updateClientInvestForm/<str:pk>', views.updateClienytInvestForm, name="updateClientInvestForm"),
    path('updateInvestForm/<str:pk>', views.updateInvestForm, name="updateInvestForm"),
    path("logout/", LogoutView.as_view(), name="logout")

]
