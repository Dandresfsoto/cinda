from django.db import models
from config.extrafields import ContentTypeRestrictedFileField
from markdown import markdown
import random
import string
# Create your models here.

def upload_dinamic_dir(instance, filename):
    return '/'.join(['Comunidades', str(instance.id), filename])


class ComunidadEntry(models.Model):
    nombre = models.CharField(max_length=100)
    photo = ContentTypeRestrictedFileField(
        upload_to=upload_dinamic_dir,
        content_types=['image/jpg', 'image/jpeg', 'image/png'],
        max_upload_size=1048576
    )
    markdown = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=100, choices=[
        ('AFROS','AFROS'),
        ('INDIGENAS','INDIGENAS'),
        ('COSTUMBRES','COSTUMBRES'),
        ('COCINA','COCINA'),
        ('FOTOS','FOTOS'),
        ('BIENES','BIENES'),
        ('MEDICINA','MEDICINA')
    ])
    descripcion = models.TextField()

    def get_html(self):
        return markdown(self.markdown)


def upload_dinamic_imagenes(instance, filename):
    chars = string.ascii_uppercase
    random_str = ''.join(random.choice(chars) for _ in range(20))
    return '/'.join(['Imagenes', random_str, filename])


class Imagenes(models.Model):
    file = ContentTypeRestrictedFileField(
        upload_to=upload_dinamic_imagenes,
        content_types=['image/jpg', 'image/jpeg', 'image/png'],
        max_upload_size=1048576
    )
