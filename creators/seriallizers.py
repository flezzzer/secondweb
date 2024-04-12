from rest_framework import serializers
from restaurant.models import Restaurant,CategoryOfMeals,Meal
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields=['id','name','description','email','url']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryOfMeals
        fields=['id','name','description']

class MealSerializer(serializers.ModelSerializer):
    photo=serializers.SerializerMethodField()
    def get_photo(self,meal):
        request=self.context.get('request')
        photo_url=meal.photo.url
        return request.build_absolute_uri(photo_url)
    class Meta:
        model=Meal
        fields=['id','name','description','price','weight','photo']
