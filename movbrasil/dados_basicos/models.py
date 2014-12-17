# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

class quem_somos_model(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return "Descrição"

    class Meta:
        verbose_name_plural="Quem somos"

class equipe_model(models.Model):
    nome = models.CharField(max_length=200)
    tel = models.CharField(max_length=11) 
    e_mail= models.EmailField()
    foto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural="Equipe"
