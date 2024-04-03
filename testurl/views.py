from django.shortcuts import render
from restaurant import models

def home(request):
    restaurants = models.Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

# Create your views here.
