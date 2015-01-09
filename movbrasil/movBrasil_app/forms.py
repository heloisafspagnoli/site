# -*- coding: utf-8 -*-
from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome",
                            error_messages={
                                'required': "Por favor, digite seu nome"
                            }
                        )
    email = forms.EmailField(label="E-mail",
                                error_messages={
                                    'required': "Por favor, digite seu e-mail"
                                }
                            )
    mensagem= forms.CharField(widget=forms.Textarea,
                                label="Mensagem",
                                error_messages={
                                    'required': "Por favor, escreva uma mensagem"
                                    }
                                )

class InscricaoForm(forms.Form):
    nome = forms.CharField(label="Nome")
    cpf = forms.CharField(label="CPF")
    email = forms.EmailField(label="E-mail")
    telefone = forms.CharField(label="Telefone")
    endereco = forms.CharField(label="Endereço")
    nro_comp = forms.CharField(label="Número/Complemento")
    bairro = forms.CharField(label="Bairro")
    cidade = forms.CharField(label="Cidade")
    formacao = forms.CharField(label="Formação")
