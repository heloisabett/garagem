from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()    

    class Meta:
        verbose_name = "acessório"
        verbose_name_plural = "acessórios"