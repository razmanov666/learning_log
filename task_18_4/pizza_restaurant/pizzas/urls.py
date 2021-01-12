"""Определяет схемы Pizzas"""
from django.urls import re_path
from . import views

urlpatterns = [
    # Домашняя страница.
    re_path(r"^$", views.index, name='index'),
    re_path(r"^pizzas$", views.pizzas, name='pizzas'),
    re_path(r"^pizza/(?P<pizza_id>\d+)$", views.pizza, name="pizza")
]