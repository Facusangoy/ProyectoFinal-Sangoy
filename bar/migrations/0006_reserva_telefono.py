# Generated by Django 5.2.4 on 2025-07-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0005_alter_reserva_options_comentario_respuesta_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='telefono',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
