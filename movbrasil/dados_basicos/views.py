# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import quem_somos_model, equipe_model

def quem_somos_view(request):
    descricao = quem_somos_model.objects.first().descricao
    time_mvb = equipe_model.objects.all()
    return render(request, 'quem_somos.html', 
                    {'descricao': descricao, 'time_mvb': time_mvb})

