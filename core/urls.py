# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include  # add this

from core import settings

urlpatterns = [
    path("", include("apps.home.urls")),  # UI Kits Html files
    path("", include("apps.home.urls")),  # UI Kits Html files
    path('admin/', admin.site.urls),  # Django admin route
    path("invest/", include("apps.investment.urls")),
    path("", include("apps.authentication.urls")),  # Auth routes - login / register
    path("reminders/", include("apps.reminders.urls")),
    path("agent/", include("apps.agent.urls"))
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
