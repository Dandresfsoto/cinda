from .models import ComunidadEntry
from .serializers import ComunidadEntrySerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import AllowAny


class ComunidadesEntryApiView(mixins.ListModelMixin,
                              generics.GenericAPIView):
    queryset = ComunidadEntry.objects.all()
    serializer_class = ComunidadEntrySerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)