from django.db import models
#from .categoria import Categoria
#from .marca import Marca
from uploader.models import Image
from emovepro.models import Categoria, Marca

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    cor = models.CharField(max_length=20)
    idade = models.IntegerField(null=True, blank=True)
    tamanho = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produtos")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="produtos")
    descricao = models.CharField(max_length=200, null=True, blank=True)
    #foto = models.ImageField(upload_to="/produtos")
    capa = models.ForeignKey(
        Image, 
        related_name="+", 
        on_delete=models.CASCADE, # Se a imagem for excluída, o produto inteiro vai
        null=True,
        blank=True,
        default=None
        )

    def __str__(self):
        return f'{self.marca} {self.nome}'