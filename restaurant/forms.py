from django import forms
from . import models
from .models import Meal

class OrderForm(forms.ModelForm):
    meal=forms.ModelChoiceField(queryset=Meal.objects.all(),widget=forms.HiddenInput)
    class Meta:
        model=models.Order
        fields=('meal','name','phone')