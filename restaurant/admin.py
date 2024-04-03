from django.contrib import admin
from .models import Restaurant, CategoryOfMeals, Meal, Order

admin.site.register(Restaurant)
admin.site.register(CategoryOfMeals)
admin.site.register(Meal)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['meal', 'name', 'phone', 'date']
# Register your models here.
