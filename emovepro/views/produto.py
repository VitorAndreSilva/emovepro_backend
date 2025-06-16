from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from emovepro.models import Produto
from emovepro.serializers import ProdutoSerializer, ProdutoDetailSerializer, ProdutoListSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    #serializer_class = ProdutoSerializer
    def get_serializer_class(self):
        #if self.action in ["list", "retrieve"]: # Se a ação da classe ProdutoViewSet estiver entre uma dessas duas
        if self.action == "list":
            return ProdutoDetailSerializer # Retorna este serializer mais detalhado
        elif self.action == "retrieve":
            return ProdutoListSerializer
        return ProdutoSerializer
    def get_permissions(self):
        return [AllowAny()]
    #permission_classes = [AllowAny()]