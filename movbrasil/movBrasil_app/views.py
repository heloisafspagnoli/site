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

#   Dados do rodapé: 
#    chamada = chamada_model.objects.first()
#    cursos = curso_model.objects.filter(ativo=True)
#    cursos = cursos.order_by('data')
#    proximos_cursos = cursos[:3]
#    contato = endereco_contato_model.objects.first() 
    
def pag_inicial_view(request):
    chamada = chamada_model.objects.first()
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data_inicial')
    proximos_cursos = cursos[:3]
    contato = endereco_contato_model.objects.first() 
    
    equipe_emails = equipe_model.objects.all()
    emails_contato = []
    for endereco in equipe_emails:
        if endereco.contato:
            emails_contato.append(endereco.e_mail)

    parceiros = parceiros_model.objects.all()
    return render(request, 'home.html',
                    {
                        'chamada': chamada, 'proximos_cursos': proximos_cursos,
                        'contato': contato, 'cursos': cursos,
                        'parceiros': parceiros, 'emails': emails_contato, 
                    }
                )

def quem_somos_view(request):
    chamada = chamada_model.objects.first()
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data_inicial')
    proximos_cursos = cursos[:3]
    contato = endereco_contato_model.objects.first() 

    equipe_emails = equipe_model.objects.all()
    emails_contato = []
    for endereco in equipe_emails:
        if endereco.contato:
            emails_contato.append(endereco.e_mail)
    
    qms = quem_somos_model.objects.first()
    time_mvb = equipe_model.objects.all()
    palestrantes = palestrantes_model.objects.all()
    return render(request, 'quem_somos.html', 
                    {
                        'chamada': chamada, 'proximos_cursos': proximos_cursos,
                        'contato': contato, 'qms': qms, 'time_mvb': time_mvb, 
                        'palestrantes': palestrantes, 'emails': emails_contato,
                    }
                )

def cursos_view(request):
    chamada = chamada_model.objects.first()
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data_inicial')
    proximos_cursos = cursos[:3]
    contato = endereco_contato_model.objects.first() 
    
    equipe_emails = equipe_model.objects.all()
    emails_contato = []
    for endereco in equipe_emails:
        if endereco.contato:
            emails_contato.append(endereco.e_mail)
    
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

    return render_to_response('cursos.html',
                                {
                                    'chamada': chamada, 'contato': contato,
                                    'proximos_cursos': proximos_cursos,  
                                    'cursos': returned_page, 'temas': temas,
                                    'pages_number_aux': aux,
                                    'emails': emails_contato,
                                }
                            )

def getCurso_view(request, cursoSlug):
    chamada = chamada_model.objects.first()
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data_inicial')
    proximos_cursos = cursos[:3]
    contato = endereco_contato_model.objects.first() 
    
    equipe_emails = equipe_model.objects.all()
    emails_contato = []
    for endereco in equipe_emails:
        if endereco.contato:
            emails_contato.append(endereco.e_mail)
    
    curso_item = get_object_or_404(curso_model, slug=cursoSlug)
    materiais = curso_item.material_incluso.order_by('nome')
    programacao = curso_item.programacao.order_by('data')
    palestrantes = curso_item.palestrantes.order_by('nome')

    equipe_emails = equipe_model.objects.all()
    email_para = []
    emails_contato = []
    for endereco in equipe_emails:
        email_para.append(endereco.e_mail)
        if endereco.contato:
            emails_contato.append(endereco.e_mail)
    
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assunto = u"Inscrição - " + curso_item.titulo
            email_de = cd.get('email')
            email_para.append(email_de)
            duvidas = request.POST['duvidas']
            mensagem = cd['nome'] + " - " + cd['cpf'] + "\n" + \
                       cd['telefone'] + "\n" + cd['email'] + "\n\n" + \
                       cd['endereco'] + ", " + cd['nro_comp'] + "\n" + \
                       cd['bairro'] + ", " + cd['cidade'] + " -  " + \
                       cd['estado'] + "\n\n" +  cd['formacao'] + "\n\n" + \
                       duvidas
            send_mail(assunto, mensagem, email_de, email_para)
            return HttpResponseRedirect('/contato_efetuado/')
    else:
        form = InscricaoForm()
    
    return render(request, 'curso_item.html',
                                {
                                    'chamada': chamada, 'contato': contato,
                                    'proximos_cursos': proximos_cursos,  
                                    'curso_item': curso_item, 
                                    'materiais': materiais, 
                                    'programacao': programacao, 
                                    'palestrantes':palestrantes,
                                    'form': form,
                                    'emails': emails_contato,
                                })

def contato_view(request):
    chamada = chamada_model.objects.first()
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data_inicial')
    proximos_cursos = cursos[:3]
    contato = endereco_contato_model.objects.first() 
    
    equipe_emails = equipe_model.objects.all()
    emails_contato = []
    for endereco in equipe_emails:
        if endereco.contato:
            emails_contato.append(endereco.e_mail)

    equipe_emails = equipe_model.objects.all()
    email_para = []
    for endereco in equipe_emails:
        email_para.append(endereco.e_mail)

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assunto = request.POST['assunto'] 
            email_de = cd.get('email')
            email_para.append(email_de)
            mensagem = cd['nome']+'\n'+ email_de+'\n\n'+cd['mensagem']
            send_mail(assunto, mensagem, email_de, email_para)
            return HttpResponseRedirect('/contato_efetuado/')
    else:
        form = ContatoForm()
    contato = endereco_contato_model.objects.first()
    return render(request, 'contato.html', 
                    {
                        'chamada': chamada, 'proximos_cursos': proximos_cursos,  
                        'contato': contato, 'form': form,
                        'emails': emails_contato,
                    }
                )

def contato_efetuado_view(request):
    chamada = chamada_model.objects.first()
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data')
    proximos_cursos = cursos[:3]
    contato = endereco_contato_model.objects.first() 
    
    equipe_emails = equipe_model.objects.all()
    emails_contato = []
    for endereco in equipe_emails:
        if endereco.contato:
            emails_contato.append(endereco.e_mail)
    
    return render(request, 'contato_efetuado.html',
                    {
                        'chamada': chamada, 'contato': contato,
                        'proximos_cursos': proximos_cursos, 
                        'emails': emails_contato,  
                    }
                )       
