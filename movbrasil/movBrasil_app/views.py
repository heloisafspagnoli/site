from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    pages = Paginator(cursos, 2)

    page = request.GET.get('page')
    
    try:
        returned_page = pages.page(page)
    except PageNotAnInteger:
        returned_page = pages.page(1)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    return render_to_response('cursos.html', {'cursos': returned_page})

def getCurso(request, cursoSlug):
    curso = curso_model.objects.filter(slug=cursoSlug)

    # Display specified post
    return render_to_response('curso_item_apresentacao.html', { 'curso': curso})
