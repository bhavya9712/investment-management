from django.db import models


# Create your models here.
from apps.home.models import CustomUser


class agent(models.Model):
    agent_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    agent_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    agent_office_name = models.CharField(max_length=50)
    agent_office_address = models.CharField(max_length=50)
    agent_office_contact = models.CharField(max_length=50)
    agent_office_description = models.CharField(max_length=50)
    agent_clients = models.ManyToManyField(CustomUser,related_name='clients')


# class agent_client(models.Model):
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
#     agent_id = models.ForeignKey(agent, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     access_request = models.CharField(max_length=50)
#     status = models.CharField(max_length=50)

    def __str__(self):
        return self.agent_id
