from django.forms import ModelForm, widgets
from django import forms
from user.models import User


# Forms
class UserCreateForm(ModelForm):

    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'streetname': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'picture': widgets.TextInput(attrs={'class': 'form-control'}),
            'preferredpaymentid': widgets.Select(attrs={'class': 'form-control'}),
            'countryid': widgets.Select(attrs={'class': 'form-control'}),
        }
