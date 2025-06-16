from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from emovepro.models import Marca
from emovepro.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    def get_permissions(self):
        return [AllowAny()]