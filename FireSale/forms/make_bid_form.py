from django.forms import ModelForm, widgets
from django import forms

from user.models import Bid


# Forms.
class MakeBidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['id', 'StatusID', 'PaymentID']
        widgets = {
            'BidAmount': widgets.NumberInput(attrs={'class': 'form-control'}),
            'BuyerID': widgets.NumberInput(attrs={'class': 'form-control'}),
            'ProductID': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
