# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now
from django.utils import timezone


class Pessoa(models.Model):
    nome = models.CharField(max_length=80)
    sobrenome = models.CharField(max_length=100)
    redator = models.CharField(max_length=100)
    data_de_inicio = models.DateField(default=timezone.now)
    email = models.CharField(max_length=254)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='usuario')

    def __str__(self):
        return self.redator
    