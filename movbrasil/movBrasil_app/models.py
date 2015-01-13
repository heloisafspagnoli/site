# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class chamada_model(models.Model):
    chamada = models.TextField(max_length=200)
    img_chamada = models.ImageField()

    def __str__(self):
        return "Chamada"

    class Meta:
        verbose_name_plural="Chamada"


class parceiros_model(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural="Parceiros"


class quem_somos_model(models.Model):
    descricao = models.TextField()
    nossa_missao = models.TextField()
    nossa_visao = models.TextField()
    somos_bons = models.TextField()
    img = models.ImageField()
    
    def __str__(self):
        return "Descrição"

    class Meta:
        verbose_name_plural="Quem somos"


class equipe_model(models.Model):
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=100)
    resumo = models.TextField(max_length=300)
    tel = models.CharField(max_length=11)
    e_mail= models.EmailField()
    foto = models.ImageField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural="Equipe"


class local_model(models.Model):
    nome = models.CharField(max_length=200)
    complemento = models.CharField(max_length=20, blank=True)
    numero = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural="Locais"


class endereco_contato_model(models.Model):
    texto_inicial = models.TextField()
    assuntos = models.TextField()
    e_mail = models.EmailField()
    telefone = models.CharField(max_length=30)
    local = models.ForeignKey(local_model)
    
    def __str__(self):
        return "Contato e endereço"

    class Meta:
        verbose_name_plural="Dados da empresa"


class material_incluso_model(models.Model):
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural="Materias inclusos"


class palestrantes_model(models.Model):
    nome = models.CharField(max_length=200)
    resumo = models.TextField()
    foto = models.ImageField()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural="Palestrantes"
        ordering = ('nome',)


class programacao_model(models.Model):
    data = models.DateField()
    atividade = models.TextField()

    def __unicode__(self):
        return self.data.strftime('%d-%m-%Y')

    class Meta:
        verbose_name_plural="Programação"
        ordering = ('data', 'atividade')


class curso_model(models.Model):
    titulo = models.CharField(max_length=254)
    data = models.DateField()
    img = models.ImageField()
    tema = models.CharField(max_length=254)
    descricao = models.TextField()
    carga_horaria = models.CharField(max_length=100)
    publico = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    slug = models.SlugField(max_length=40, unique=True)
    preco = models.CharField(max_length=300)
    botao_pagSeguro = models.TextField()

    local = models.ForeignKey(local_model)
    material_incluso = models.ManyToManyField(material_incluso_model)
    programacao = models.ManyToManyField(programacao_model)
    palestrantes = models.ManyToManyField(palestrantes_model)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name_plural="Cursos"
        ordering = ('titulo',)
