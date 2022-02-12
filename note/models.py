from turtle import title
from django.db import models

# Create your models here.
class noteModel(models.Model):
    note_title = models.TextField(max_length=100)
    note_content = models.TextField(max_length=150)