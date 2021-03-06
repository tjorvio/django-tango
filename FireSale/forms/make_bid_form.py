from django.forms import ModelForm, widgets
from django import forms

from user.models import Bid


# Forms.
class MakeBidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['id', 'StatusID']
        widgets = {
            'BidAmount': widgets.NumberInput(attrs={'class': 'form-control'}),
            'UserID': widgets.HiddenInput(),
            'PaymentID': widgets.Select(attrs={'class': 'form-control'}),
            'ProductID': forms.HiddenInput(),
        }
