from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserForm,RestaurantForm,UserFormForEdit,CategoryForm,MealForm
from django.contrib.auth.models import User
from restaurant.models import Restaurant,CategoryOfMeals,Meal
from django import forms


from django.contrib.auth import authenticate,login

def home(request):
    return redirect(auth_home)

@login_required(login_url='/creators/login')
def auth_home(request):
    return render(request, 'creators/home.html',{'user-is-authenticated':request.user.is_authenticated})
# Create your views here.
def sign_up(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()
    if (request.method=='POST'):
        user_form=UserForm(request.POST)
        restaurant_form=RestaurantForm(request.POST,request.FILES)
        if user_form.is_valid() and restaurant_form.is_valid():

            new_user=User.objects.create_user(**user_form.cleaned_data)
            new_restaurant=restaurant_form.save(commit=False)
            new_restaurant.owner=new_user
            new_restaurant.save()
            user=authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password'],
            )
            login(request,user)

            return redirect(auth_home)
    return render(request, 'creators/sign_up.html', {
        'userform':user_form,
        'restaurantform':restaurant_form,
    })
def profile(request):
    user_form=UserFormForEdit(instance=request.user)
    request_user_restaurant=Restaurant.objects.get(owner=request.user)
    restaurant_form=RestaurantForm(instance=request_user_restaurant)
    if (request.method=="POST"):
        user_form = UserFormForEdit(request.POST,instance=request.user)
        restaurant_form = RestaurantForm(request.POST,instance=request_user_restaurant)
        if user_form.is_valid() and restaurant_form.is_valid():
            user_form.save()
            restaurant_form.save()
    return render(request,'creators/profile.html',{"user_form":user_form,'restaurant_form':restaurant_form})

@login_required(login_url='/creators/login')
def list_category(request):
    request_user_restaurant = Restaurant.objects.get(owner=request.user)
    categorys = get_list_or_404(CategoryOfMeals,restaurant=request_user_restaurant)
    return render(request, 'creators/list_category.html', {'categorys':categorys})

@login_required(login_url='/creators/login')
def list_meal(request):
    request_user_restaurant = Restaurant.objects.get(owner=request.user)
    meals=get_list_or_404(Meal,restaurant=request_user_restaurant)
    return render(request, 'creators/list_meal.html',{'meals':meals})

@login_required(login_url='/creators/login')
def edit_category(request, category_name):
    category=get_object_or_404(CategoryOfMeals,name=category_name)
    category_form=CategoryForm(instance=category)
    if (request.method=='POST'):
        category_form = CategoryForm(request.POST,instance=category)
        if(category_form.is_valid()):
            category_form.save()
            return redirect(list_category)
    return render(request,'creators/edit_category.html',{'category_form':category_form})

@login_required(login_url='/creators/login')
def edit_meal(request,meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    meal_form = MealForm(instance=meal)
    if (request.method=='POST'):
        meal_form = MealForm(request.POST,request.FILES,instance=meal)
        if(meal_form.is_valid()):
            meal_form.save()
            return redirect(list_meal)
    return render(request, 'creators/edit_meal.html', {'meal_form': meal_form})

def add_meal(request):
    meal_form = MealForm()
    if (request.method == 'POST'):
        meal_form = MealForm(request.POST,request.FILES)
        request_user_restaurant = Restaurant.objects.get(owner=request.user)
        categorys = get_list_or_404(CategoryOfMeals, restaurant=request_user_restaurant)
        if meal_form.is_valid():
            new_meal = meal_form.save(commit=False)
            request_user_restaurant = Restaurant.objects.get(owner=request.user)
            category=get_list_or_404(CategoryOfMeals,restaurant=request_user_restaurant)
            new_meal.restaurant=request_user_restaurant
            new_meal.save()

            return redirect(list_meal)
    return render(request, 'creators/add_meal.html',{'meal_form':meal_form})

def add_category(request):
    category_form=CategoryForm()
    if (request.method == 'POST'):
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            new_category = category_form.save(commit=False)
            request_user_restaurant = Restaurant.objects.get(owner=request.user)
            new_category.restaurant =request_user_restaurant
            new_category.save()

            return redirect(list_category)
    return render(request, 'creators/add_category.html',{'category_form':category_form})
