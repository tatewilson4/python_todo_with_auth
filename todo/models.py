from django.db import models
from django.urls import reverse


class Todo(models.Model):
    item = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('item_edit', kwargs={'pk': self.pk})
