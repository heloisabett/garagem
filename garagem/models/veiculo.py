from django.db import models
class Veiculo(models.Model):
    ano = models.DateField(max_length=4)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    cor =models.ForeignKey(
        Cor, on_delete=models.CASCADE, related_name="veiculos",
        )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="veiculos",
    )
    marca = models.ForeignKey(
        Marca, on_delete=models.CASCADE, related_name="veiculos",
    )

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.ano} {self.cor}" 