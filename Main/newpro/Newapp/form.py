from django import forms

class _City(forms.Form):
    Cityname = forms.CharField(max_length=100)