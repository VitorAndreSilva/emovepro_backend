from rest_framework.serializers import ModelSerializer
from emovepro.models import Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'