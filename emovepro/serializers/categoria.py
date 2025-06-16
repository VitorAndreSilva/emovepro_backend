from rest_framework.serializers import ModelSerializer
from emovepro.models import Categoria

class CategoriaSerializer(ModelSerializer): # Serializer é o que transforma o objeto do DB em um objeto de JSON
    class Meta: # Metadados; configurações da classe principal
        model = Categoria # Define a model (o objeto do DB) que será serializada
        fields = '__all__'