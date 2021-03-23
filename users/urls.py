"""Определяет схемы URL для пользователей."""
from django.urls import path, include

from . import views

app_name='users'
urlpatterns = [
    # Страница входа
    path('', include('django.contrib.auth.urls')),
    # path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # # Страница выхода
    # Страница регистрации
    path('register/', views.register, name='register'),
    # path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico'))
]
