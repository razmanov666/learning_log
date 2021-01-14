from django.db import models

class BlogPost(models.Model):
    """Модель поста в блоге."""
    title =  models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text