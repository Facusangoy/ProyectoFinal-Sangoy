# Generated by Django 5.2.4 on 2025-07-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='about_photos/')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
