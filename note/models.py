from turtle import title
from django.db import models

# Create your models here.
class noteModel(models.Model):
    title = models.TextField(max_length=100)
    note = models.TextField(max_length=150)