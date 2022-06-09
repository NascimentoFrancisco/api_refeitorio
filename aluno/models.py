import email
from django.db import models
from refeicao.models import Refeicao
# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=16, unique=True)
    senha = models.CharField(max_length=16)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=50)
    email = models.EmailField()
    chave_refeicao = models.ForeignKey(Refeicao, on_delete = models.CASCADE)
    pendencias = models.IntegerField(null = True)


