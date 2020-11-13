from django.db import models

# Create your models here.

class Horarios(models.Model):
    id_horario = models.AutoField(primary_key=True)
    horario = models.IntegerField(unique=True)
    disponivel = models.BooleanField(null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'horarios'