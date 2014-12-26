from django.shortcuts import render

from models import chamada_model, parceiros_model, quem_somos_model, equipe_model, endereco_contato_model, local_model, curso_model, palestrantes_model, programacao_model

def pag_inicial_view(request):
    chamada = chamada_model.objects.first().chamada
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data')
    cursos = cursos[:4]
    parceiros = parceiros_model.objects.all()
    return render(request, 'home.html',
                    {'chamada': chamada, 'cursos': cursos, 'parceiros': parceiros})

def quem_somos_view(request):
    descricao = quem_somos_model.objects.first().descricao
    time_mvb = equipe_model.objects.all()
    return render(request, 'quem_somos.html', 
                    {'descricao': descricao, 'time_mvb': time_mvb})

def cursos_view(request):
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data')
    return render(request, 'cursos.html',
                    {'cursos': cursos})
