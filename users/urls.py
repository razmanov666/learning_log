"""Определяет схемы URL для пользователей."""
from django.urls import re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # Страница входа
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(template_name='learning_logs/index.html'), name='logout'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico'))
]
