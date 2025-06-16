from rest_framework.serializers import ModelSerializer, SlugRelatedField
from django.contrib.auth import get_user_model

from .models import Usuario
from uploader.serializers import ImageSerializer
from uploader.models import Image


class UsuarioSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source = 'foto',
        queryset = Image.objects.all(),
        slug_field = 'attachment_key',
        required = False,
        write_only = True
    )
    foto = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Usuario
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)  # 🔐 Criptografa a senha corretamente!
        user.save()
        return user