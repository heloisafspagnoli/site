# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import quem_somos_model, equipe_model

def quem_somos_view(request):
    descricao = quem_somos_model.objects.first().descricao
    return render(request, 'quem_somos.html', {'descricao': descricao})

def equipe_view(request):
    time_mvb = equipe_model.objects.all()
    return render(request, 'time_mvb.html', {'time_mvb': time_mvb})
