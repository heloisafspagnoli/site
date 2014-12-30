from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import chamada_model, parceiros_model, quem_somos_model,\
                   equipe_model, endereco_contato_model, local_model,\
                   curso_model, palestrantes_model, programacao_model,\
                   material_incluso_model

def pag_inicial_view(request):
    chamada = chamada_model.objects.first().chamada
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data')
    cursos = cursos[:4]
    parceiros = parceiros_model.objects.all()
    return render(request, 'home.html',
                    {'chamada': chamada, 'cursos': cursos,
                        'parceiros': parceiros})

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
    
    aux = []
    i = 1
    while i <= pages.num_pages:
        aux.append(pages.page(i))
        i = i + 1

    return render_to_response('cursos.html', {'cursos': returned_page,
                                                'pages_number_aux': aux})

def getCurso_view(request, cursoSlug):
    curso_item = curso_model.objects.filter(slug=cursoSlug).first()
    materiais = curso_item.material_incluso.order_by('nome')
    programacao = curso_item.programacao.order_by('data', 'hora')
    
    palestrantes = []
    for programa in programacao:    
        palestrantes_aux = programa.palestrantes.all()
        for palestrante in palestrantes_aux:
            palestrantes.append(palestrante)

    palestrantes = list(set(palestrantes))
    
    return render_to_response('curso_item.html',
                                {
                                    'curso_item': curso_item, 
                                    'materiais': materiais, 
                                    'programacao': programacao, 
                                    'palestrantes':palestrantes
                                })
