from django.forms import ModelForm, widgets
from django import forms

from product.models import Picture


# Forms.
class PictureForm(ModelForm):

    class Meta:
        model = Picture
        exclude = ['id', 'picture', 'product']
        widgets = {

        }

