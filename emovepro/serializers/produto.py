from rest_framework.serializers import ModelSerializer, SlugRelatedField
from emovepro.models import Produto
# Uploader
from uploader.models import Image
from uploader.serializers import ImageSerializer

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
    capa_attachment_key = SlugRelatedField(
        source="capa", # Campo que preencherá o campo "capa"
        queryset=Image.objects.all(), # Campos que permitem manter a imagem
        slug_field="attachment_key",
        required=False, # Não é obrigatória
        write_only=True, # "somente ver" Não será exibida ao retornar dados com JSON
    )
    capa = ImageSerializer(required=False, read_only=True)

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        depth = 1

class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        #fields = ["id", "nome"]
        fields = '__all__'
    capa = ImageSerializer(required=False)