from django import forms
from restaurant import models
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    email=forms.CharField(max_length=50,required=True)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password','email']

class RestaurantForm(forms.ModelForm):
    class Meta:
        model=models.Restaurant
        fields=['name','description','url','email','rating']
