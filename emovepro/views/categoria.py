from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from emovepro.models import Categoria
from emovepro.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet): # ViewSet é o que permite executar um CRUD
    queryset = Categoria.objects.all() # Define os dados a serem utilizados para o CRUD
    serializer_class = CategoriaSerializer
    #permission_classes = [IsAuthenticated] # O usuário deve ter permissão para acessá-las
    def get_permissions(self):
        return [AllowAny()]
    # Linha comentada para ativar a permissão no arquivo settings.py