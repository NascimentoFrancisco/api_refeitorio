from django.db import models

# Create your models here.
class DiaLetivo(models.Model):
    nome = models.CharField(max_length=50)
    letivo = models.BooleanField()