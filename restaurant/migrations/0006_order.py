# Generated by Django 4.1 on 2024-03-18 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_categoryofmeals_options_alter_meal_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=10, verbose_name='Телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.meal', verbose_name='Блюда')),
            ],
        ),
    ]
