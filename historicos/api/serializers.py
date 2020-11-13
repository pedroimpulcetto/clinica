from rest_framework import serializers

from historicos.models import Historicos
from imagens.api.serializers import ImagensHistoricoSerializer

class HistoricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = "__all__"

class HistoricosDetalhesSerializer(serializers.ModelSerializer):
    imagens = ImagensHistoricoSerializer(many=True, read_only=True)

    class Meta:
        model = Historicos
        fields = [
            'id_historico',
            'data',
            'id_agendamento',
            'aparecimento_sintomas',
            'duracao_sintomas',
            'local_dor',
            'nivel_dor',
            'tipo_dor',
            'detalhes',
            'conclusao',
            'imagens',
        ]