from django.forms import ModelForm, widgets

from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'StreetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'Zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'City': widgets.TextInput(attrs={'class': 'form-control'}),
            'Bio': widgets.TextInput(attrs={'class': 'form-control'}),
            'CountryID': widgets.Select(attrs={'class': 'form-control'})
        }
