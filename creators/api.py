from django.http import JsonResponse
from restaurant.models import Restaurant,CategoryOfMeals,Meal
from .seriallizers import RestaurantSerializer,CategorySerializer,MealSerializer

def client_get_restaurants(request):
    restaurants=RestaurantSerializer(
        Restaurant.objects.all().order_by('-id'),
        many=True,
        context={'request':request}
    ).data
    return JsonResponse({'restaurants':restaurants})

def get_categorys(request,restaurant_name):
    categorys=CategorySerializer(
        CategoryOfMeals.objects.filter(restaurant__name=restaurant_name).order_by('-id'),
        many=True,
        context={'request': request}
    ).data
    return JsonResponse({'categorys':categorys})

def get_meal(request,category_name,restaurant_name):
    meals=MealSerializer(
        Meal.objects.filter(restaurant__name=restaurant_name,category__name=category_name).order_by('-id'),
        many=True,
        context={'request': request}
    ).data
    return JsonResponse({'meals':meals})