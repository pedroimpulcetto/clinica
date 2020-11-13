from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from pacientes.models import Pacientes
from pacientes.api.serializers import PacientesSerializer
from pacientes.api.serializers import PacientesDetalhesSerializer
from agendamentos.models import Agendamentos

class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

    @action(detail=False, methods=['get'], url_path='detalhes', url_name='detalhes')
    def detalhes(self, request, *args, **kwargs):
        queryset = Pacientes.objects.all()
        self.serializer_class = PacientesDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

class PacientesDetalhesViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all()
    serializer_class = PacientesDetalhesSerializer

