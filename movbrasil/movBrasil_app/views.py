from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from forms import ContatoForm, InscricaoForm
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
    curso_item = get_object_or_404(curso_model, slug=cursoSlug)
    materiais = curso_item.material_incluso.order_by('nome')
    programacao = curso_item.programacao.order_by('data')
    palestrantes = curso_item.palestrantes.order_by('nome')
    
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assunto = "Inscrição - " + curso_item.nome
            email_de = cd.get('email')
            email_para = 'heloisafspagnoli@gmail.com'
            #import pdb; pdb.set_trace()
            #send_mail(assunto, mensagem, email_de,[email_para, email_de])
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
            #import pdb; pdb.set_trace()
            #send_mail(assunto, mensagem, email_de,[email_para, email_de])
            return HttpResponseRedirect('/contato_efetuado/')
    else:
        form = ContatoForm()
    contato = endereco_contato_model.objects.first()
    return render(request, 'contato.html', {'contato': contato, 'form': form})

def thanks_view(request):
    return render(request, 'thanks.html')
