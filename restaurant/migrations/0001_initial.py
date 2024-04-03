# Generated by Django 4.1 on 2024-03-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SushiShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(verbose_name='text')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('url', models.URLField(verbose_name='URL')),
            ],
        ),
    ]
