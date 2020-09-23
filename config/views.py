#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, FormView, View
from braces.views import LoginRequiredMixin
from django.conf import settings
from config.utils import convert_dict_breadcrums
from .forms import LoginForm
from django.contrib import messages
from apps.users.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect, reverse, redirect
from apps.comunidades.models import ComunidadEntry


class Login(FormView):

    template_name = 'login.pug'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_verificated:
                login(self.request, user)
                return HttpResponseRedirect(self.get_success_url())
            else:
                messages.warning(self.request, 'El usuario no se encuentra activo')
        else:
            if User.objects.filter(email=email).count() > 0:
                messages.warning(self.request, 'La contraseña no es correcta')
            else:
                messages.info(self.request, 'No existe el usuario')
        return HttpResponseRedirect(self.get_success_url())


class Logout(View):

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect(settings.LOGIN_URL)


class Index(LoginRequiredMixin, TemplateView):

    template_name = 'index.pug'
    login_url = settings.LOGIN_URL
    permissions = {
        "crear": [
            "users.comunidades.ver",
            "users.comunidades.crear"
        ]
    }

    def get_context_data(self, **kwargs):

        kwargs['title'] = 'Inicio'
        kwargs['breadcrumbs'] = convert_dict_breadcrums([
            ('Inicio', '#')
        ])
        kwargs['options'] = self.request.user.has_perms(self.permissions.get('crear'))
        kwargs['crear_comunidad'] = reverse('comunidades:crear_comunidad')
        kwargs['afros'] = ComunidadEntry.objects.filter(tipo='AFROS')
        kwargs['indigenas'] = ComunidadEntry.objects.filter(tipo='INDIGENAS')
        kwargs['costumbres'] = ComunidadEntry.objects.filter(tipo='COSTUMBRES')
        kwargs['cocina'] = ComunidadEntry.objects.filter(tipo='COCINA')
        kwargs['fotos'] = ComunidadEntry.objects.filter(tipo='FOTOS')
        kwargs['bienes'] = ComunidadEntry.objects.filter(tipo='BIENES')
        kwargs['medicina'] = ComunidadEntry.objects.filter(tipo='MEDICINA')
        return super(Index, self).get_context_data(**kwargs)


class Landing(TemplateView):

    template_name = 'landing.pug'

    def get_context_data(self, **kwargs):

        kwargs['title'] = 'CINDA'
        kwargs['usuarios_registrados'] = User.objects.all().count()
        kwargs['entradas'] = ComunidadEntry.objects.all().count()
        kwargs['servicios_ofrecidos'] = ComunidadEntry.objects.filter(tipo='BIENES').count()
        kwargs['galeria'] = ComunidadEntry.objects.filter(tipo='FOTOS').count()
        kwargs['entradas_items'] = ComunidadEntry.objects.all()
        return super(Landing, self).get_context_data(**kwargs)
