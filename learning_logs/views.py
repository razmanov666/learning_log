from django.shortcuts import render
from .models import Topic

def index(request):
    """Домашняя страница приложения Learning log."""
    return render(request, "learning_logs/index.html")

def topics(request):
    """Выводит список тем."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, 'learning_logs/topics.html', context)

def hello(request):
    """Test"""
    return render(request, "learning_logs/hello.html")