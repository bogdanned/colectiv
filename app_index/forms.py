from django import forms

class indexForm(forms.Form):
    origin = forms.CharField(max_length=4000)
    destiny = forms.CharField(max_length=4000)
