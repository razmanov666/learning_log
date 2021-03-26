"""Определяет схемы URL для learning_logs"""

<<<<<<< HEAD
from django.urls import path, re_path, include
=======
from django.contrib import admin
from django.urls import include, path
>>>>>>> modifications
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница 
    path("", views.index, name="index"),
    # Вывод всех тем.
    path("topics", views.topics, name="topics"),
    # Страница с подробной информацией по отдельной теме.
    path("topic/<int:topic_id>/", views.topic, name='topic'),
    # Страница для создания новой темы.
    path("new_topic/", views.new_topic, name='new_topic'),
    # Страница для создания новых записей.
    path("new_entry/<int:topic_id>/", views.new_entry, name='new_entry'),
    # Страница для редактирования записей.
    path("edit_entry/<int:entry_id>/", views.edit_entry, 
                                                name='edit_entry'),
]