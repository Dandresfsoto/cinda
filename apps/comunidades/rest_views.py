from .models import ComunidadEntry
from .serializers import ComunidadEntrySerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import AllowAny


class ComunidadesEntryApiView(mixins.ListModelMixin,
                              generics.GenericAPIView):

    serializer_class = ComunidadEntrySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        tipo = self.request.query_params.get('tipo',None)
        return ComunidadEntry.objects.filter(tipo=tipo)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)