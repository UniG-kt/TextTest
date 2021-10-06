from django.db import models
from mdeditor.fields import MDTextField

class Articles(models.Model):
    title = models.CharField(max_length=255)
    content = MDTextField()
