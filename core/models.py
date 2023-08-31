from django.db import models

# Create your models here.

class Reserva(models.Model):
    cnpj = models.CharField(max_length=100)
    nome_empresa= models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=100)
    quitado = models.BooleanField()

class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.FloatField()