# Generated by Django 5.2.4 on 2025-07-15 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0003_reserva_personas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='personas',
        ),
    ]
