from django.db import models

# Create your models here.
from django.db.models import Model


class  Blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title