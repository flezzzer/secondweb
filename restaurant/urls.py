
from django.urls import path, include
from restaurant import views


from django.conf.urls.static import static
from django.conf import settings



app_name='restaurant'

urlpatterns=[
    path("", views.restaurants, name='restaurants'),
    path("<str:rest_name>", views.restaurant, name='restaurant'),
    path("<str:rest_name>/<str:category_name>", views.category, name='category'),
    path("<str:rest_name>/<str:category_name>/<int:meal_id>", views.meal_detail,name='meal_detail'),

]