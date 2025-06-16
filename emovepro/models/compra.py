from django.db import models

from usuario.models import Usuario
from emovepro.models import Produto

class Compra(models.Model):
    class status(models.IntegerChoices): # Select com os números e os valores de cada status
        CARRINHO = 1, 'Carrinho',
        REALIZADO = 2, 'Realizado',
        PAGO = 3, 'Pago',
        ENTREGUE = 4, 'Entregue',
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=status.choices, default=status.CARRINHO)
    @property # Indica que o seguinte campo (total) não existe na model de compra, mas será calculado pelo método
    def total(self):
        total = 0
        for item in self.itens.all():
            total += item.preco * item.quantidade
        return total
        #return sum(item.produto.preco * item.quantidade for item in self.itens.all())

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens") # Ao deletar uma compra, a classe inteira vai pelo ralo
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)