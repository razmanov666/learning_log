from django.shortcuts import render

def index(request):
    """Домашняя страница приложения."""
    return render(request, "pizzas/index.html")