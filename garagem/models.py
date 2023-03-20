from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.nome.upper()
