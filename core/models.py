from django.db import models

# Create your models here.

class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.FloatField()

class Reserva(models.Model):
    cnpj = models.CharField(max_length=100)
    nome_empresa= models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=100)
    quitado = models.BooleanField()
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)  # Define automaticamente a data no momento da reserva

    class Meta:
        ordering = ['data_reserva']  # Ordena as reservas por ordem crescente de data

