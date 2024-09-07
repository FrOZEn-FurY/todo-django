from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(default=timezone.localtime(), validators=[MinValueValidator(limit_value=timezone.now())])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["deadline"]
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
