"""Определяет схемы URL для пользователей."""

from django.urls import re_path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    # Страница входа
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(template_name='users/index.html'), name='logout'),
]
