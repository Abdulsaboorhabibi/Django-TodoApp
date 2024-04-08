from django.db import models


class TodoModel(models.Model):
    task = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
