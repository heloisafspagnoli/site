from django.shortcuts import render

from .models import quem_somos_model, time_mvb_model

def quem_somos_view(request):
    descricao = quem_somos_model.objects.first().descricao
    return render(request, 'quem_somos.html', {'descricao': descricao})

def time_mvb_view(request):
    time = time_mvb_model.objects.all()
    return render(request, 'time_mvb.html', {'time_mvb': time})
