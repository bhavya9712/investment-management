from django import forms
from django.forms import ModelForm, CharField

# from apps.home.models import family
from apps.agent.forms import CustomMMCF
from apps.home.models import CustomUser

USER_GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other','Other')
]



class add_Family_Form():
    clients_family = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "family email",
                "class": "form-control"
            }
        ))


# class add_Family_Form(ModelForm):
#      clients_family = CustomMMCF(
#          queryset=CustomUser.objects.filter(is_staff=False),
#          widget=forms.CheckboxSelectMultiple
#      )
#
#      class Meta:
#          model =CustomUser
#          fields = ['clients_family']

class ProfileUpdateForm(ModelForm):
    gender = forms.ChoiceField(label='', choices=USER_GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "User Name",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        ))

    class Meta:
        model = CustomUser
        fields = ['username',
                  'first_name',
                  'address',
                  'gender',
                  'profilephoto',
                  'last_name']
