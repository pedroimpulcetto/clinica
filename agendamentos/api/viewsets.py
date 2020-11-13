from rest_framework import viewsets

from agendamentos.models import Agendamentos
from agendamentos.api.serializers import AgendamentosSerializer

class AgendamentosViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('datahora')
    serializer_class = AgendamentosSerializer

    # @action(detail=False, methods=['get'], url_path='list', url_name='list')
    # def list_agendamentos(self, request, *args, **kwargs):
    #     id_user = self.request.user
    #     id_cliente = self.request.query_params.get('id_cliente')
    #     id_agendamento = self.request.query_params.get('id_agendamento')
    #     data_agendamento = self.request.query_params.get('data_agendamento')

    #     queryset = Agendamentos.objects.filter(
    #         id_user=id_user)

    #     self.serializer_class = AgendamentosListSerializer

    #     serializer = self.get_serializer(queryset, many=True)

    #     return Response(serializer.data)

    # def get_queryset(self):
    #     id_user = self.request.user
    #     return Agendamentos.objects.filter(id_user=id_user)