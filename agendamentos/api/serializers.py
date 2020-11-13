from rest_framework import serializers

from agendamentos.models import Agendamentos
from historicos.api.serializers import HistoricosDetalhesSerializer


class AgendamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'

class AgendamentosDetalhesSerializer(serializers.ModelSerializer):
    historicos = HistoricosDetalhesSerializer(many=True, read_only=True)

    class Meta:
        model = Agendamentos
        fields = [
            'id_agendamento',
            'datahora',
            'data_criacao',
            'cancelado',
            'obs',
            'tipo',
            'historicos',
        ]