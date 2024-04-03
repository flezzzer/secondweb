from django import forms
from django.core import validators

class NameForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(5),])
