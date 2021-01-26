"""Определяет схемы URL для blogs."""

from django.urls import path, re_path, include
from . import views
urlpatterns = [
    # Домашняя страница.
    re_path(r"^$", views.blogposts, name='blogposts')
]
