from django.db import models
from personal_organ import settings


# Create your models here.

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=150)
    email = models.TextField(max_length=200)
    senha = models.TextField(max_length=12)