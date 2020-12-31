from django.db import models

class Pizza(models.Model):
    """Class about pizza."""
    name = models.CharField(max_length=30)
    def __str__(self):
        """Return text views of Pizza."""
        return self.name
    
    class Meta:
        verbose_name_plural = "Pizzas"

class Topping(models.Model):
    """Info about pizza's toppings"""
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    text = models.CharField(max_length=30)

    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) > 50:
            output = self.text[:50] + '...'
        else:
            output = self.text
        return output