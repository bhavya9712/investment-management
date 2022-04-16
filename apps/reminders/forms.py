from django import forms
from django.forms import ModelForm
from .models import Reminders


class ReminderForm(ModelForm):
    class Meta:
        model = Reminders
        fields = ['Reminder_date',
                  'Reminder_description']
        widgets = {
            'Reminder_date': forms.DateInput(format='%Y-%m-%d',
                                             attrs={'firstDay': 1, 'lang': 'pl',
                                                    'format': 'yyyy-mm-dd', 'type': 'date'
                                                    ,"class": "form-control datepicker"}),
            'Reminder_description': forms.TextInput(

                attrs={
                    "placeholder": "Reminder Description",
                    "class": "form-control"
                }
            )

        }
