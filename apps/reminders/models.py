from django.db import models

from apps.home.models import CustomUser
from apps.investment.models import Investment


# Create your models here.
class Reminders(models.Model):
    Reminder_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    Reminder_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Reminder_Investment_id = models.ForeignKey(Investment, on_delete=models.CASCADE)
    Reminder_date = models.DateField()
    Reminder_description = models.CharField(max_length=50)
    Reminder_lastupdate_date = models.DateField(auto_now=True)
    Reminder_lastupdate_user_id = models.IntegerField(null=True)



    @property
    def __str__(self):
        return self.Reminder_id
