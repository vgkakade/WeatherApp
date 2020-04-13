from django import forms
from django.forms import TextInput

class CityForm(forms.Form):
    # city = forms.CharField(widget=forms.(attrs={'class':'input','placeholder':'City Name'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}))
