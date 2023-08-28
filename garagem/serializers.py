from rest_framework.serializers import ModelSerializer
from garagem.models import Veiculo

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1


class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "preco"]

