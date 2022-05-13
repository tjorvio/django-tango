from django.forms import ModelForm, widgets
from user.models import PaymentInfo


class CheckOutCCForm(ModelForm):

    class Meta:
        model = PaymentInfo
        exclude = ['id',]
        widget = {
            'cardholder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expire_month': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'MM'}),
            'expire_year': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'YY'}),
            'card_cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
            'bid': widgets.HiddenInput(),
        }
