from rest_framework import serializers

from horarios.models import Horarios

class HorariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horarios
        fields = '__all__'