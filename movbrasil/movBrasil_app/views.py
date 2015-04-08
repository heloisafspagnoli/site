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

def dados_basicos():
    chamadas = chamada_model.objects.all()
    cursos = curso_model.objects.filter(ativo=True)
    cursos = cursos.order_by('data_inicial')
    proximos_cursos = cursos[:3]
    contato = endereco_contato_model.objects.first()

    equipe_emails = equipe_model.objects.all()
    emails_contato = []
    for endereco in equipe_emails:
        if endereco.contato:
            emails_contato.append(endereco.e_mail)

    dados_basicos = {
                                    'chamadas': chamadas, 'proximos_cursos': proximos_cursos,
                                    'contato': contato, 'cursos': cursos, 'emails': emails_contato
                                }

    return dados_basicos

def pag_inicial_view(request):
    dict_view = dados_basicos()
    parceiros = parceiros_model.objects.all()
    dict_view.update({'parceiros': parceiros})
    return render(request, 'home.html', dict_view)

def quem_somos_view(request):
    dict_view = dados_basicos()
    qms = quem_somos_model.objects.first()
    time_mvb = equipe_model.objects.all()
    palestrantes = palestrantes_model.objects.all()
    dict_view.update({'qms': qms, 'time_mvb': time_mvb, 'palestrantes': palestrantes})
    return render(request, 'quem_somos.html', dict_view)

def cursos_view(request):
    dict_view = dados_basicos()
    temas = []
    for curso in dict_view['cursos']:
        temas.append(curso.tema)

    #Divide a lista de cursos em listas menores de ate 9 elementos
    cursos = dict_view['cursos']
    pages = [cursos[i:i+9] for i in range(0, len(cursos), 9)]

    temas = list(set(temas))
    lista_temas = []
    for tema_curso in temas:
        lista_temas.append(cursos.filter(tema=tema_curso))

    x = {}
    for lista in lista_temas:
       x.update({lista[0].tema: [lista[i:i+2] for i in range(0, len(lista), 2)]})

    import pdb; pdb.set_trace()

    dict_view.update({'temas': temas})
    return render_to_response('cursos.html', dict_view)

def getCurso_view(request, cursoSlug):
    dict_view = dados_basicos()

    curso_item = get_object_or_404(curso_model, slug=cursoSlug)
    materiais = curso_item.material_incluso.order_by('nome')
    programacao = curso_item.programacao.order_by('data')
    palestrantes = curso_item.palestrantes.order_by('nome')

    equipe_emails = equipe_model.objects.all()
    email_para = []
    for endereco in equipe_emails:
        email_para.append(endereco.e_mail)

    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid() and len(request.POST['g-recaptcha-response']) > 100 :
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
    dict_view.update({
                                    'curso_item': curso_item,
                                    'materiais': materiais,
                                    'programacao': programacao,
                                    'palestrantes':palestrantes,
                                    'form': form,
                                })
    return render(request, 'curso_item.html', dict_view)

def contato_view(request):
    dict_view = dados_basicos()

    equipe_emails = equipe_model.objects.all()
    email_para = []
    for endereco in equipe_emails:
        email_para.append(endereco.e_mail)

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid() and len(request.POST['g-recaptcha-response'])>100 :
            cd = form.cleaned_data
            assunto = request.POST['assunto']
            email_de = cd.get('email')
            email_para.append(email_de)
            mensagem = cd['nome']+'\n'+ email_de+'\n\n'+cd['mensagem']
            send_mail(assunto, mensagem, email_de, email_para)
            return HttpResponseRedirect('/contato_efetuado/')
    else:
        form = ContatoForm()

    dict_view.update({'form': form})
    return render(request, 'contato.html', dict_view)

def contato_efetuado_view(request):
    dict_view = dados_basicos()
    return render(request, 'contato_efetuado.html', dict_view )