from django.forms import ModelForm, widgets
from django import forms

from product.models import Product, Picture


# Forms.
class ProductCreateForm(ModelForm):
    # picture = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    picture = Picture()

    class Meta:
        model = Product
        exclude = ['id', 'SoldOrNot', 'CreatedAt']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'condition': widgets.Select(attrs={'class': 'form-control'}),
            'sellerID': widgets.HiddenInput(),
            # 'CreatedAt': forms.DateTimeField(default=datetime.now)
        }
