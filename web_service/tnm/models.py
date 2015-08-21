# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from nedda.staging import staging

# Create your models here.

# class Estadiamento(models.Model):
#     cid = models.CharField(max_length=50)
    # t = models.CharField(max_length=5)
    # n = models.CharField(max_length=5)
    # m = models.CharField(max_length=5)
    # dukes = models.CharField(max_length=5)
    # psa = models.CharField(max_length=5)
    # gleasson = models.CharField(max_length=5)

class Cid(models.Model):
    cid = models.CharField(max_length=5)

class Tnm(models.Model):
    cid = models.ForeignKey(Cid)
    t = models.ManyToManyField(Cid, related_name='Tnm.t+')
    n = models.ManyToManyField(Cid, related_name='Tnm.n+')
    m = models.ManyToManyField(Cid, related_name='Tnm.m+')

class Resultado(models.Model):
    # campo não precisa ser obrigatório, pois ele será preenchido a partir do estadiamento
    estagio = models.CharField(max_length=10, blank=True)

# class CidForm(ModelForm):
#     class Meta:
#         model = Cid
# class TnmForm(ModelForm):
#     class Meta:
#         model = Tnm
