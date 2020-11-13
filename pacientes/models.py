from django.db import models

# Create your models here.

def imagem_paciente(instance, filename):
    return '/'.join(['imagens', f'{instance.nome}-{instance.id_paciente}', filename])


class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nasc = models.DateTimeField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    bairro_endereco = models.CharField(
        max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    cel = models.CharField(max_length=100, blank=True, null=True)
    atend_unimed = models.BooleanField(default=False)
    atend_particular = models.BooleanField(default=False)
    atend_outros = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    rg = models.CharField(
        max_length=100, blank=True, null=True)
    cpf = models.CharField(
        max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=False)
    avatar = models.ImageField(upload_to=imagem_paciente, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pacientes'
