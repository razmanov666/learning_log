"""Определяет схемы URL для learning_logs"""

from django.contrib import admin
from django.urls import path, re_path
from . import views
urlpatterns = [
    # Домашняя страница
    re_path(r"^$", views.index, name="index"),
]