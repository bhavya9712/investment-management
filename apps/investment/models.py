from django.db import models


# Create your models here.
class Investment(models.Model):
    investmentid = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    investmenttype = models.CharField(max_length=50)
    investmentcompany = models.CharField(max_length=50)
    investment_user_id = models.CharField(max_length=50)
    investment_amount = models.CharField(max_length=50)
    investment_date = models.DateField()
    investment_due_date = models.DateField()
    investment_lastupdate_date = models.DateField(auto_now=True, blank=True)
    investment_agent_id = models.CharField(max_length=50)
    investment_description = models.CharField(max_length=50)

    def __str__(self):
        return self.investment_user_id
