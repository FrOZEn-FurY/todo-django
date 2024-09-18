from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class TodoModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(default=timezone.now(),
                                    validators=[MinValueValidator(limit_value=timezone.now())])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["deadline"]
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
