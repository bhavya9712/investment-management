from django import forms
from django.forms import ModelForm
from .models import Investment


class InvestmentForm(ModelForm):
    investmenttype = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Investment Type",
                "class": "form-control"
            }
        ))

    investment_amount = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Investment Amount",
                "class": "form-control"
            }
        ))
    investmentcompany = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Investment Company",
                "class": "form-control"
            }
        ))

    investment_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Investment Description",
                "class": "form-control ","style":"resize: none",
                "rows":"5",
                "cols":"35"

            }
        ))

    class Meta:
        model = Investment
        fields = ['investmenttype',
                  'investment_amount',
                  'investmentcompany',
                  'investment_date',
                  'investment_due_date',
                  'investment_description']

        widgets = {
            'investment_date': forms.DateInput(format='%Y-%m-%d',
                                               attrs={'firstDay': 1, 'lang': 'pl',
                                                      'format': 'yyyy-mm-dd', 'type': 'date'
                                                      , "class": "form-control datepicker"}),
            'investment_due_date': forms.DateInput(format='%Y-%m-%d',
                                                   attrs={'firstDay': 1, 'lang': 'pl',
                                                          'format': 'yyyy-mm-dd', 'type': 'date'
                                                       , "class": "form-control datepicker"}),
            'investment_lastupdate_date': forms.DateInput(format='%Y-%m-%d',
                                                          attrs={'firstDay': 1, 'lang': 'pl',
                                                                 'format': 'yyyy-mm-dd', 'type': 'date'
                                                              , "class": "form-control datepicker"}),
        }
