from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=30)
    link = models.URLField(null=True, blank=True) # Campo pode ser nulo e é opcional
    def __str__(self):
        return self.nome