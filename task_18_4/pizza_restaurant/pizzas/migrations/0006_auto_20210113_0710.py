# Generated by Django 3.1.4 on 2021-01-13 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_auto_20210113_0705'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='Topping',
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'toppings'},
        ),
    ]
