from django.db import models
from diasletivo.models import DiaLetivo

# Create your models here.

class Refeicao(models.Model):
    nome = models.CharField(max_length=255)
    cardapio = models.TextField()
    quantidade_disponivel = models.IntegerField()
    quantidade_reservadas = models.IntegerField()
    horario_inicio_reserva = models.TimeField()
    horario_fim_reserva = models.TimeField()
    tempo_oferta = models.TimeField()
    dia_oferta = models.ForeignKey(DiaLetivo,on_delete=models.CASCADE)
    
