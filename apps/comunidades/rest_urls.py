from django.urls import path
from .rest_views import ComunidadesEntryApiView

app_name = 'rest'

urlpatterns = [
    path('', ComunidadesEntryApiView.as_view(), name = 'comunidad_api')
]
