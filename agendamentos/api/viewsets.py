from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from agendamentos.models import Agendamentos
from agendamentos.api.serializers import AgendamentosSerializer
from agendamentos.api.serializers import AgendamentosDetalhesSerializer

class AgendamentosViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('datahora')
    serializer_class = AgendamentosSerializer

    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Agendamentos.objects.filter(pk=pk)
        self.serializer_class = AgendamentosDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)