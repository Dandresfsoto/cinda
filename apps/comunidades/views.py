#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView, UpdateView, TemplateView
from django.conf import settings
from braces.views import LoginRequiredMixin, MultiplePermissionsRequiredMixin
from .forms import ComunidadEntryForm
from .models import ComunidadEntry
from config.utils import convert_dict_breadcrums
from django.urls import reverse

# Create your views here.

class CreateComunidades(LoginRequiredMixin,MultiplePermissionsRequiredMixin, CreateView):
    """
    """
    permissions = {
        "all": [
            "users.comunidades.ver",
            "users.comunidades.crear"
        ]
    }
    login_url = settings.LOGIN_URL
    template_name = 'comunidades/crear.pug'
    form_class = ComunidadEntryForm
    model = ComunidadEntry

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Nueva entrada'
        kwargs['title_panel'] = 'Agregar entrada'
        kwargs['breadcrumbs'] = convert_dict_breadcrums([
            ('Inicio', reverse('index')),
            ('Entradas', '#'),
            ('Crear', '#'),
        ])
        return super(CreateComunidades,self).get_context_data(**kwargs)

class UpdateComunidades(LoginRequiredMixin,MultiplePermissionsRequiredMixin, UpdateView):
    """
    """
    permissions = {
        "all": [
            "users.comunidades.ver",
            "users.comunidades.editar"
        ]
    }
    login_url = settings.LOGIN_URL
    template_name = 'comunidades/editar.pug'
    form_class = ComunidadEntryForm
    model = ComunidadEntry

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Editar entrada'
        kwargs['title_panel'] = 'Editar entrada'
        kwargs['breadcrumbs'] = convert_dict_breadcrums([
            ('Inicio', reverse('index')),
            ('Entradas', '#'),
            ('Editar', '#'),
        ])
        return super(UpdateComunidades,self).get_context_data(**kwargs)

class ShowComunidades(LoginRequiredMixin, TemplateView):
    """
    """
    login_url = settings.LOGIN_URL
    template_name = 'comunidades/ver.pug'

    def get_context_data(self, **kwargs):
        comunidad = ComunidadEntry.objects.get(pk=kwargs['pk'])
        kwargs['title'] = ''
        kwargs['title_panel'] = 'Ver comunidad'
        kwargs['breadcrumbs'] = convert_dict_breadcrums([
            ('Inicio', reverse('index')),
            ('Ver', '#'),
        ])
        kwargs['comunidad'] = comunidad
        return super(ShowComunidades,self).get_context_data(**kwargs)
