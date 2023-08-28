from rest_framework.serializers import ModelSerializer
from garagem.models import Veiculo

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"