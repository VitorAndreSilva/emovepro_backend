from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from emovepro.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ['produto', 'quantidade', 'total']
        depth = 1 # Mostra detalhes da model deste serializer; se fosse 2, por exemplo, mostraria detalhes da model da model do serializer e assim por diante
    total = SerializerMethodField() # O método indica que o campo total não existe na model
    def get_total(self, instance): # instance representa os itens da compra, por onde acessamos o livro, a quantidade e o preço; get_<nome> é o método para calcular o valor do <nome>
        return instance.quantidade * instance.produto.preco

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'itens')

class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('produto', 'quantidade', 'preco')

    def validate(self, data):
        if data["quantidade"] > data["produto"].quantidade:
            raise serializers.ValidationError(
                {"quantidade": "quantidade solicitada não disponível em estoque."}
            )
        return data
        
class CriarEditarCompraSerializer(ModelSerializer):
    #itens = ItensCompraSerializer(many=True, write_only=True)
    itens = CriarEditarItensCompraSerializer(many=True, write_only=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault()) # O usuario vai ficar oculto por ser um HiddenField()
    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'itens')
    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens_data:
            item["preco"] = item["produto"].preco #####################
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra
    def update(self, instance, validated_data):
        itens = validated_data.pop("itens_data")
        if itens:
            instance.objects.all().delete()
            for item in itens:
                item["preco"] = item["produto"].preco
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance

'''
class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('usuario', 'itens')

    def validate(self, data):
        if data["quantidade"] > data["produto"].quantidade:
            raise serializers.ValidationError(
                {"quantidade": "quantidade solicitada não disponível em estoque."}
            )
'''