# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from forms import ContatoForm, InscricaoForm
from models import chamada_model, parceiros_model, quem_somos_model,\
                   equipe_model, endereco_contato_model, local_model,\
                   curso_model, palestrantes_model, programacao_model,\
                   material_incluso_model

import unicodedata

def pag_inicial_view(request):
    chamada = chamada_model.objects.first()
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data')
    cursos = cursos[:4]
    parceiros = parceiros_model.objects.all()
    return render(request, 'home.html',
                    {'chamada': chamada, 'cursos': cursos,
                        'parceiros': parceiros})

def quem_somos_view(request):
    descricao = quem_somos_model.objects.first().descricao
    imgs = quem_somos_model.objects.first().img
    imgs = imgs.all()
    first_img = imgs.first()
    num_imagens = len(imgs) - 1
    time_mvb = equipe_model.objects.all()
    return render(request, 'quem_somos.html', 
                    {'descricao': descricao, 'time_mvb': time_mvb, 'imgs': imgs,
                        'first_img': first_img, 'num_imagens': range(num_imagens)})

def cursos_view(request):
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data')
    temas = []
    for curso in cursos:
        temas.append(curso.tema)
    temas = list(set(temas))

    pages = Paginator(cursos, 9)

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

    return render_to_response('cursos.html', {'cursos': returned_page, 'temas': temas,
                                                'pages_number_aux': aux})

def getCurso_view(request, cursoSlug):
    curso_item = get_object_or_404(curso_model, slug=cursoSlug)
    materiais = curso_item.material_incluso.order_by('nome')
    programacao = curso_item.programacao.order_by('data')
    palestrantes = curso_item.palestrantes.order_by('nome')
    
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assunto = u"Inscrição - " + curso_item.titulo
            email_de = cd.get('email')
            email_para = 'heloisafspagnoli@gmail.com'
            duvidas = request.POST['duvidas']
            mensagem = cd['nome'] + " - " + cd['cpf'] + "\n" + \
                       cd['telefone'] + "\n" + cd['email'] + "\n\n" + \
                       cd['endereco'] + ", " + cd['nro_comp'] + "\n" + \
                       cd['bairro'] + "  " + cd['cidade'] + "\n\n" + \
                       cd['formacao'] + "\n\n" + duvidas
            send_mail(assunto, mensagem, email_de,[email_para, email_de])
            return HttpResponseRedirect('/contato_efetuado/')
    else:
        form = InscricaoForm()
    
    return render(request, 'curso_item.html',
                                {
                                    'curso_item': curso_item, 
                                    'materiais': materiais, 
                                    'programacao': programacao, 
                                    'palestrantes':palestrantes,
                                    'form': form,
                                })

def contato_view(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assunto = request.POST['assunto'] 
            email_de = cd.get('email')
            email_para = 'heloisafspagnoli@gmail.com'
            mensagem = cd['nome']+'\n'+ email_de+'\n\n'+cd['mensagem']
            send_mail(assunto, mensagem, email_de,[email_para, email_de])
            return HttpResponseRedirect('/contato_efetuado/')
    else:
        form = ContatoForm()
    contato = endereco_contato_model.objects.first()
    return render(request, 'contato.html', {'contato': contato, 'form': form})

def contato_efetuado_view(request):
    return render(request, 'contato_efetuado.html')
