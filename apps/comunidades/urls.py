from django.urls import path, include
from .views import CreateComunidades, UpdateComunidades, ShowComunidades

app_name = 'comunidades'

urlpatterns = [
    path('crear/', CreateComunidades.as_view(), name='crear_comunidad'),
    path('editar/<int:pk>/', UpdateComunidades.as_view(), name='editar_comunidad'),
    path('ver/<int:pk>/', ShowComunidades.as_view(), name='ver_comunidad'),

    path('api/v1.0/', include('apps.comunidades.rest_urls', namespace='api_comunidades')),
]
