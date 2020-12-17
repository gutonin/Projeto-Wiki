# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Materia, Categoria

def listagem(request):
    materias = Materia.objects.all().order_by('-data_criacao')
    context={
        'titulo':'Minha Wiki',
        'titulo_pagina':'Materias',
        'materias':materias,
    }
    return render(request, 'listagem.html', context)

def detalhe_materia(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    return render(request, 'detalhe_materia.html', {'materia': materia})
        