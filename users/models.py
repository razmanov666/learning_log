from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    """Тема которую изучает пользователь."""
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    date_added = models.DateTimeField(auto_now_add=True)
    # id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.name