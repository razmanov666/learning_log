"""Определяет схемы URL для learning_logs"""

from django.contrib import admin
from django.urls import path, re_path, include
from . import views
urlpatterns = [
    # Домашняя страница 
    re_path(r"^$", views.index, name="index"),
    # Вывод всех тем.
    re_path(r"^topics$", views.topics, name="topics"),
    # MY TEST
    re_path(r"^hello$", views.hello, name="hello"),
    # Страница с подробной информацией по отдельной теме.
    re_path(r"^topic/(?P<topic_id>\d+)/$", views.topic, name='topic'),
    # Страница для создания новой темы.
    re_path(r"^new_topic/$", views.new_topic, name='new_topic'),
    # Страница для создания новых записей.
    re_path(r"^new_entry/(?P<topic_id>\d+)/$", views.new_entry, name='new_entry'),
    # Страница для редактирования записей.
    re_path(r"^edit_entry/(?P<entry_id>\d+)/$", views.edit_entry, 
                                                name='edit_entry'),
]