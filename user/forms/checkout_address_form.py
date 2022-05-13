from django import forms
from django.forms import ModelForm, widgets
from user.models import BillingAddress, PaymentInfo, Order


class CheckOutAddressForm(ModelForm):
    class Meta:
        model = BillingAddress
        exclude = ['id']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'City': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'CountryID': widgets.Select(attrs={'class': 'form-control'})
        }

