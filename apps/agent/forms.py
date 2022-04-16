from django import forms
from django.forms import ModelForm
from .models import agent
from ..home.models import CustomUser


class CustomMMCF(forms.ModelMultipleChoiceField):
     def label_from_instance(self, member):
         return "%s" % member.email


class add_clientForm(ModelForm):
     agent_clients = CustomMMCF(
         queryset=CustomUser.objects.filter(is_staff=False),
         widget=forms.CheckboxSelectMultiple
     )

     class Meta:
         model =agent
         fields = ['agent_clients']


class add_agent_details_Form(ModelForm):
    agent_office_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "office name :",
                "class": "form-control"
            }
        ))

    agent_office_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "office address",
                "class": "form-control"
            }
        ))
    agent_office_contact = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "office contact number",
                "class": "form-control"
            }
        ))
    agent_office_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "description",
                "class": "form-control"
            }
        ))

    class Meta:
        model = agent
        fields = ['agent_office_name',
                  'agent_office_address',
                  'agent_office_contact',
                  'agent_office_description']
