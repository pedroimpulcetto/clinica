# Generated by Django 3.1.3 on 2020-11-12 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamentos', '0002_auto_20201112_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historicos',
            fields=[
                ('id_historico', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('aparecimento_sintomas', models.CharField(blank=True, max_length=100, null=True)),
                ('duracao_sintomas', models.CharField(blank=True, max_length=100, null=True)),
                ('local_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('nivel_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('detalhes', models.TextField(blank=True, null=True)),
                ('conclusao', models.TextField(blank=True, null=True)),
                ('id_agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico', to='agendamentos.agendamentos')),
            ],
            options={
                'db_table': 'historicos',
                'managed': True,
            },
        ),
    ]
