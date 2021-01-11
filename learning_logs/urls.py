"""Определяет схемы URL для learning_logs"""

from django.contrib import admin
from django.urls import path, re_path, include
from . import views
urlpatterns = [
    # Домашняя страница 
    re_path(r"^$", views.index, name="index"),
    
    re_path(r"^/hello$", views.hello, name="hello"),
    # Вывод всех тем.
    re_path(r"^/topics$", views.topics, name="topics")
]