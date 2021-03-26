"""Определяет схемы URL для blogs."""

from django.urls import path, path, include
from . import views

app_name = 'blogs'
urlpatterns = [
    # Домашняя страница.
    path("", views.blogposts, name='blogposts'),
    path("new_post/", views.new_post, name='new_post'),
    path("edit_post/<int:blogposts_id>/", views.edit_post, name='edit_post')
]
