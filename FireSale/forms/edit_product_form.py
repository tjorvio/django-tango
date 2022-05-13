from django.forms import ModelForm, widgets
from django import forms

from product.models import Product


# Forms.
class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['id', 'SoldOrNot', 'CreatedAt', 'sellerID']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'condition': widgets.Select(attrs={'class': 'form-control'}),
        }
