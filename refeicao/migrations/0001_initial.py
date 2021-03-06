# Generated by Django 4.0.5 on 2022-06-09 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diasletivo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cardapio', models.TextField()),
                ('quantidade_disponivel', models.IntegerField()),
                ('quantidade_reservadas', models.IntegerField()),
                ('horario_inicio_reserva', models.TimeField()),
                ('horario_fim_reserva', models.TimeField()),
                ('tempo_oferta', models.TimeField()),
                ('dia_oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diasletivo.dialetivo')),
            ],
        ),
    ]
