from rest_framework import serializers

from historicos.models import Historicos

class HistoricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = "__all__"
