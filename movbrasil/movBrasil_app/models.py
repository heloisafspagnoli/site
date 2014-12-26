# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


class chamada_model(models.Model):
    chamada = models.TextField(max_length=200)

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

    def __str__(self):
        return "Descrição"

    class Meta:
        verbose_name_plural="Quem somos"


class equipe_model(models.Model):
    nome = models.CharField(max_length=200)
    resumo = models.TextField(max_length=300)
    tel = models.CharField(max_length=11)
    e_mail= models.EmailField()
    foto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural="Equipe"


class endereco_contato_model(models.Model):
    endereco = models.CharField(max_length=200)
    e_mail = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return "Endereço"

    class Meta:
        verbose_name_plural="Endereço e contato da empresa"


class local_model(models.Model):
    nome_local = models.CharField(max_length=200)
    complemento = models.CharField(max_length=20, blank=True)
    numero = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome_local

    class Meta:
        verbose_name_plural="Local"


class curso_model(models.Model):
    titulo = models.CharField(max_length=254)
    data = models.DateField()
    img_curso = models.ImageField(blank=True, null=True)
    resumo = models.TextField(max_length=400)
    descricao = models.TextField( blank=True, null=True)
    material_incluso = models.TextField(blank=True, null=True)
    carga_horaria = models.CharField(max_length=100)
    publico = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    local = models.ForeignKey(local_model)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name_plural="Cursos"
        ordering = ('titulo',)


class palestrantes_model(models.Model):
    nome = models.CharField(max_length=200)
    resumo = models.TextField()
    foto = models.ImageField(blank=True, null=True)
    cursos = models.ManyToManyField(curso_model)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural="Palestrantes"
        ordering = ('nome',)


class programacao_model(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    atividade = models.CharField(max_length=200)
    curso = models.OneToOneField(curso_model, primary_key=True)
    palestrante = models.ManyToManyField(palestrantes_model)

    def __unicode__(self):
        return self.atividade

    class Meta:
        verbose_name_plural="Programação"
        ordering = ('atividade',)