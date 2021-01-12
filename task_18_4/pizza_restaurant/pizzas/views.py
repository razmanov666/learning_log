from django.shortcuts import render

from .models import Pizza
def index(request):
    """Домашняя страница приложения."""
    return render(request, "pizzas/index.html")

def pizzas(request):
    """Отображение всех пицц"""
    pizza = Pizza.objects.order_by('name')
    context = {"pizzas": pizza}
    return render(request, "pizzas/pizzas.html", context)

def pizza(request, pizza_id):
    """Отображение всех топпингов."""
    pizza = Pizza.objects.get(id=pizza_id)
    topping = pizza.topping_set.order_by('text')
    context = {"pizzas": pizza, "topping": topping}
    return render (request, 'pizzas/pizza.html', context)