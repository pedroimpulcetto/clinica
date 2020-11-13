from django.db import models
from historicos.models import Historicos

# Create your models here.

def imagens_historico(instance, filename):
    return '/'.join(['historico', str(instance.id_historico.id_historico), filename])


class ImagensHistorico(models.Model):
    id_imagem_historico = models.AutoField(primary_key=True)
    imagem = models.ImageField(upload_to=imagens_historico, blank=True, null=True)
    id_historico = models.ForeignKey(Historicos, related_name='imagens', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'imagens_historico'