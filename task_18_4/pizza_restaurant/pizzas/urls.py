"""Определяет схемы Pizzas"""
from django.urls import re_path
from . import views

urlpatterns = [
    # Домашняя страница.
    re_path(r"^$", views.index, name='index')
]