from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm,RestaurantForm
from django.contrib.auth.models import User

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