"""Определяет схемы URL для пользователей."""
from django.urls import path, include
from . import views

app_name='users'
urlpatterns = [
    # Страница входа
    path('', include('django.contrib.auth.urls')),
    # Страница выхода
    path('', views.mylogout, name='mylogout'),
    # Страница регистрации
    path('register/', views.register, name='register'),
]
