from django.forms import ModelForm, widgets
from user.models import Order


class CheckOutConfirmForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['id', ]
        widget = {
            'buyer': widgets.NumberInput(attrs={'class': 'form-control'}),
            'billing_address': widgets.NumberInput(attrs={'class': 'form-control'}),
            'payment_info': widgets.NumberInput(attrs={'class': 'form-control'}),
        }