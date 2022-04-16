from django.contrib import admin

# Register your models here.
from apps.agent.models import agent
from apps.home.models import CustomUser
from apps.investment.models import Investment
from apps.reminders.models import Reminders

admin.site.register(CustomUser)
admin.site.register(agent)
admin.site.register(Investment)
admin.site.register(Reminders)