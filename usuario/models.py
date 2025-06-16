from django.contrib.auth.models import AbstractUser
from django.db import models
from uploader.models import Image
from django.utils.translation import gettext_lazy as _
import requests
from .managers import CustomUserManager


class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )
    class Perfil(models.IntegerChoices):
        CLIENTE = 1, "cliente"
        VENDEDOR = 2, "vendedor"
    perfil = models.IntegerField(choices=Perfil.choices, default=Perfil.CLIENTE)
    seller_id = models.CharField(max_length=50, null=True, blank=True)
    access_token = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
