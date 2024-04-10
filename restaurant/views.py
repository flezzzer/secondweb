from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Restaurant,CategoryOfMeals,Meal
from .forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
def home(request):
    return render(request, 'home.html')

def restaurants(request):
    restaurants=Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {'restaurants': restaurants})

def restaurant(request, rest_name):
    restaurant = get_object_or_404(Restaurant,name=rest_name)
    categorys = get_list_or_404(CategoryOfMeals, restaurant=restaurant)
    return render(request, 'restaurants/rest.html', {'restaurant': restaurant,'categorys':categorys})

def category(request,rest_name,category_name):
    restaurant = get_object_or_404(Restaurant, name=rest_name)
    category=get_object_or_404(CategoryOfMeals, name=category_name,restaurant=restaurant)
    meals= get_list_or_404(Meal,restaurant=restaurant,category=category)
    return render(request, 'restaurants/category.html', {'category': category, 'meals': meals, 'restaurant':restaurant})

def meal_detail(request,meal_id,rest_name,category_name):
    restaurant=get_object_or_404(Restaurant,name=rest_name)
    category = get_object_or_404(CategoryOfMeals, name=category_name, restaurant=restaurant)
    meal = get_object_or_404(Meal, restaurant=restaurant,pk=meal_id,category=category)
    form=OrderForm(request.POST or None,initial={
        'meal': meal
    })
    if (request.method=='POST'):
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('{}?sent=True'.format(reverse('restaurant:meal_detail', kwargs={'rest_name':meal.restaurant.name,'category_name':meal.category.name,'meal_id':meal.id})))
    return render(request, 'restaurants/meal_detail.html', {'category':category,'meal': meal, 'form': form, 'sent':request.GET.get('sent', False)})

