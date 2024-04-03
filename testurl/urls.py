from http import HTTPStatus
from django.urls import path, include
from . import views

app_name='testurl'

urlpatterns = [
    path('home/', views.home, name='home'),

]