from django.urls import path, include
from . import views

app_name='form'

urlpatterns=[
    path('',views.form_page),
]

