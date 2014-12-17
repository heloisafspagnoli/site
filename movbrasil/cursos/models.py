# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

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
    img_curso = models.ImageField(blank=True, null=True)
    resumo = models.TextField( blank=True, null=True)
    objetivos = models.TextField(blank=True, null=True)
    carga_horaria = models.CharField(max_length=100)
    publico = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)                          
    local = models.ForeignKey(local_model)
    
    def __unicode__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural="Curso"
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
