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
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Nome", help_text="Preencha corretamente, esse será o nome que constará no certificado")
    cpf = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}), label="CPF", help_text='Será utilizado para emissão de Nota Fiscal/Recibo')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}), label="E-mail")
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Telefone")
    endereco = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}), label="Endereço", help_text="Será utilizado para emissão de Nota Fiscal/Recibo")
    nro_comp = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}), label="Número/Complemento", help_text="Será utilizado para emissão de Nota Fiscal/Recibo")
    bairro = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}), label="Bairro", help_text="Será utilizado para emissão de Nota Fiscal/Recibo")
    cidade = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}), label="Cidade", help_text="Será utilizado para emissão de Nota Fiscal/Recibo")
    estado = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}), label="Estado", help_text="Será utilizado para emissão de Nota Fiscal/Recibo")
    formacao = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}), label="Formação")
