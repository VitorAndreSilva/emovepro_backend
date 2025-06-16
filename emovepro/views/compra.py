from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from emovepro.models import Compra
from emovepro.serializers import CompraSerializer, CriarEditarCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CriarEditarCompraSerializer
        return CompraSerializer
    
    def get_queryset(self):
        usuario = self.request.user # Usuário autenticação
        if usuario.is_superuser:
            return Compra.objects.all()
        elif usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
    
    @action(detail=True, methods=['get'])
    def total(self, request, pk=None):
        compra = self.get_object()
        return Response({"total": compra.total})