# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path,include
from apps.home import views
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('viewfamily', views.view_family, name='viewfamily'),
    path('profile', views.updateProfileForm, name='profile'),
    path('addfamily', views.add_family, name="addfamily"),

    path('update_profile', views.updateProfileForm, name='update_profile'),


    # Matches any html file
   # re_path(r'^.*\.*', views.pages, name='pages'),

]
