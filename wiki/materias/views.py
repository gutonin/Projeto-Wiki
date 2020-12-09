# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Materia, Categoria

def listagem(request):
    materias = Materia.objects.all().order_by('-data_criacao')
    print(request.user.redator)
    context={
        'titulo':'Minha Wiki',
        'titulo_pagina':'Materias',
        'materias':materias,
    }
    return render(request, 'listagem.html', context)