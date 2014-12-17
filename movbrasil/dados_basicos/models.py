# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

class quem_somos_model(models.Model):
    descricao = models.TextField()

class time_mvb_model(models.Model):
    nome = models.CharField(max_length=200)
    tel = models.CharField(max_length=11) 
    e_mail= models.EmailField()
    foto = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.nome
