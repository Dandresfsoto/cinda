from django.urls import path
from .rest_views import PermisosListApi, RolesListApi, CuentasListApi

app_name = 'rest'

urlpatterns = [
    path('cuentas/', CuentasListApi.as_view(), name = 'lista_cuentas'),
    path('permisos/', PermisosListApi.as_view(), name = 'lista_permisos'),
    path('roles/', RolesListApi.as_view(), name = 'lista_roles'),
]
