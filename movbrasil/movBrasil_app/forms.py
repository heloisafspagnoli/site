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
    mensage= forms.TextField(widget=forms.Textarea,
                                label="Mensagem",
                                error_messages={
                                    'required': "Por favor, escreva uma mensagem"
                                    }
                                )

class InscricaoForm(forms.Form):
    cpf = forms.CharField(label="CPF")
    nome = forms.CharField(label="Nome")
    telefone = forms.CharField(label="Telefone")
    email = forms.EmailField(label="E-mail")
    formacao = forms.CharField(label="Formação")
    endereco = forms.CharField(label="Endereço")
    cidade = forms.CharField(label="Cidade")
    duvidas = forms.TextField(label="Dúvidas")
