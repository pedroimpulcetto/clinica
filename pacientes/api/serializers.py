from rest_framework import serializers

from pacientes.models import Pacientes

from agendamentos.api.serializers import AgendamentosDetalhesSerializer

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'

class PacientesDetalhesSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentosDetalhesSerializer(many=True, read_only=True)

    class Meta:
        model = Pacientes
        fields = [
            'id_paciente',
            'nome',
            'data_nasc',
            'endereco',
            'num_endereco',
            'bairro_endereco',
            'cep',
            'email',
            'cel',
            'atend_unimed',
            'atend_particular',
            'atend_outros',
            'data_cadastro',
            'rg',
            'cpf',
            'sexo',
            'agendamentos',
        ]