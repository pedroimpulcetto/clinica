from rest_framework import serializers

from imagens.models import ImagensHistorico

class ImagensHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagensHistorico
        fields = '__all__'