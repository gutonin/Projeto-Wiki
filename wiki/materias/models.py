# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from pessoas.models import Pessoa
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.nome
    

class Materia(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.titulo
    
