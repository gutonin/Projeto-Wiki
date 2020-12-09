# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Materia, Categoria

def listagem(request):
    materias = Materia.objects.all().order_by('-data_criacao')
    context={
        'materias':materias,
    }
    return render(request, 'materias/listagem.html', context)