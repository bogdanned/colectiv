from django import forms
from .models import Route
from django.forms import ModelForm


class indexForm(forms.Form):
    origin = forms.CharField(max_length=4000, required=False)
    destiny = forms.CharField(max_length=4000, required=False)


class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = (
            'destiny',
            'origin',
            'duration',
            'distance',
        )
