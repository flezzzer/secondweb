from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Restaurant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    name = models.CharField(verbose_name='Название',max_length=20)
    description = models.TextField(verbose_name='Описание')
    email = models.EmailField(verbose_name='Email')
    rating = models.FloatField(verbose_name="Рейтинг",validators=[MaxValueValidator(5),MinValueValidator(0)])
    url = models.URLField(verbose_name='URL')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Ресторан'
        verbose_name_plural='Рестораны'
class CategoryOfMeals(models.Model):
    name = models.CharField(verbose_name='Название категории',max_length=20)
    description = models.TextField(verbose_name='Описание')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Категория ресторана'
        verbose_name_plural='Категории ресторана'
        ordering=['name']
class Meal(models.Model):
    name = models.CharField(verbose_name='Название',max_length=40)
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(CategoryOfMeals,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price=models.IntegerField(default=0, verbose_name='Цена, р.')
    weight=models.IntegerField(default=0,verbose_name='Вес, г.')
    photo=models.ImageField(verbose_name="Изображение", upload_to='restaurant/photos',default='',blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Блюдо'
        verbose_name_plural='Блюда'
        ordering = ['name']

class Order(models.Model):
    meal=models.ForeignKey(Meal,verbose_name='Блюда', on_delete=models.CASCADE)
    name=models.CharField(max_length=30,verbose_name='Имя')
    phone=models.CharField(max_length=10,verbose_name='Телефон')
    date=models.DateTimeField(auto_now_add=True, verbose_name='Дата')

