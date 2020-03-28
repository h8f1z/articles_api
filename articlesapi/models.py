# models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
