from django.shortcuts import render

from .models import Pizza
def index(request):
    """Домашняя страница приложения."""
    return render(request, "pizzas/index.html")

def pizzas(request):
    """Отображение всех пицц"""
    