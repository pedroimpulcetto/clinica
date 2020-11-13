from rest_framework import viewsets

from horarios.models import Horarios
from horarios.api.serializers import HorariosSerializer


class HorariosViewSet(viewsets.ModelViewSet):
    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializer

    # @action(detail=False, methods=['get'], url_path='disponivel', url_name='disponivel')
    # def list_horarios(self, request, *args, **kwargs):

    #     id_user = self.request.user.id_user
    #     id_cliente = self.request.query_params.get('id_cliente')
    #     queryset = User.objects.filter(id_user=id_user, id_cliente=id_cliente)
    #     self.serializer_class = UserHorariosSerializer

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)