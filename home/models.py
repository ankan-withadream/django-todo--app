from django.db import models

# Create your models here.

class Todos(models.Model):
    todo_name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)
    todo_desc = models.TextField(max_length=500, null=True)
