# Generated by Django 3.0.7 on 2020-09-22 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidades', '0002_comunidadentry_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunidadentry',
            name='tipo',
            field=models.CharField(choices=[('AFROS', 'AFROS'), ('INDIGENAS', 'INDIGENAS'), ('COSTUMBRES', 'COSTUMBRES'), ('COCINA', 'COCINA'), ('FOTOS', 'FOTOS'), ('BIENES', 'BIENES'), ('MEDICINA', 'MEDICINA')], max_length=100),
        ),
    ]
