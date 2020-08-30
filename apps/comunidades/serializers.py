from rest_framework import serializers
from .models import ComunidadEntry


class ComunidadEntrySerializer(serializers.ModelSerializer):

    html = serializers.SerializerMethodField()

    class Meta:
        model = ComunidadEntry
        fields = ['id', 'nombre', 'photo', 'html', 'descripcion']

    def get_html(self, obj):
        return obj.get_html()
