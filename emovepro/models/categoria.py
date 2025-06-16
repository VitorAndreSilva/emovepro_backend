from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=200)
    def __str__(self): # Define como a classe Categoria será exibida em lugares como o Django Admin
        return self.descricao # self representa a classe atual; poderia ser escrito como Categoria.descricao