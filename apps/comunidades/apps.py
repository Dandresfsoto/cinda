from django.apps import AppConfig
from django.urls import reverse


class ComunidadesConfig(AppConfig):
    name = 'apps.comunidades'

    def ready(self):
        self.index_name = 'Comunidades'
        self.disable = True
        self.icon = 'accessibility'
        self.url = ''
        self.permisos = {
            'users.comunidades'
        }
        self.menu = []

    def get_permissions_list(self):
        lista_permisos = [

            'comunidades.ver',
            'comunidades.crear',
            'comunidades.editar',
            'comunidades.eliminar',

        ]
        return lista_permisos

    def get_permissions_dict(self):
        lista_roles = [
            {
                'name': 'Comunidades, ver comunidades',
                'permisos': {
                    'comunidades.ver'
                }
            },
            {
                'name': 'Comunidades, crear comunidades',
                'permisos': {
                    'comunidades.ver',
                    'comunidades.crear'
                }
            },
            {
                'name': 'Comunidades, editar comunidades',
                'permisos': {
                    'comunidades.ver',
                    'comunidades.editar'
                }
            },
            {
                'name': 'Comunidades, eliminar comunidades',
                'permisos': {
                    'comunidades.ver',
                    'comunidades.eliminar'
                }
            }
        ]
        return lista_roles
