from django.db import models

class Produtos(models.Model):

    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField(default='')
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
