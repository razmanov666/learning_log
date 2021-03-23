"""Определяет схемы URL для learning_logs"""

from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница 
    path("", views.index, name="index"),
    # Вывод всех тем.
    path("topics", views.topics, name="topics"),
    # MY TEST
    path("hello", views.hello, name="hello"),
    # Страница с подробной информацией по отдельной теме.
    path(r"^topic/(?P<topic_id>\d+)/$", views.topic, name='topic'),
    # Страница для создания новой темы.
    path(r"^new_topic/$", views.new_topic, name='new_topic'),
    # Страница для создания новых записей.
    path(r"^new_entry/(?P<topic_id>\d+)/$", views.new_entry, name='new_entry'),
    # Страница для редактирования записей.
    path(r"^edit_entry/(?P<entry_id>\d+)/$", views.edit_entry, 
                                                name='edit_entry'),
]