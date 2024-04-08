import uuid

from django.db import models
from django.template.defaultfilters import slugify


class TodoModel(models.Model):
    task = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.task)

        while TodoModel.objects.filter(slug = self.slug).exists():
            self.slug = f"{slugify(self.task)}-{uuid.uuid4().hex[:8]}"
        super(TodoModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
