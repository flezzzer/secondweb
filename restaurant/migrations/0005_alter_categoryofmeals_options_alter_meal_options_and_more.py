# Generated by Django 4.1 on 2024-03-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_categoryofmeals_options_alter_meal_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryofmeals',
            options={'ordering': ['name'], 'verbose_name': 'Категория ресторана', 'verbose_name_plural': 'Категории ресторана'},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['name'], 'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AddField(
            model_name='meal',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='restaurant/photos', verbose_name='Изображение'),
        ),
    ]
