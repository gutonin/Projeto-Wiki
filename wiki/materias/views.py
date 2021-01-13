# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Materia, Categoria
from .form import MateriaForm


def listagem(request):
    materias = Materia.objects.filter(categoria__id=1).order_by('-data_criacao')
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        if request.POST['botao'] != '0':
            materias = Materia.objects.filter(categoria_id = request.POST
            ['botao']).order_by('-data_criacao')
        else:
            materias = Materia.objects.all().order_by('-data_criacao')
    context={
        'titulo':'Minha Wiki',
        'titulo_pagina':'Materias',
        'materias':materias,
        'categorias':categorias,
    }
    return render(request, 'listagem.html', context)

def detalhe_materia(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    return render(request, 'detalhe_materia.html', {'materia': materia})

def adicao_materia(request):
    form = MateriaForm()
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
    # else:
    #     print("get")
    # data = {}
    #     return listagem
    # data['form'] = form
    return render(request, 'adicao_materia.html',  {'form': form})

    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = NameForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/thanks/')

    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = NameForm()

    # return render(request, 'name.html', {'form': form})
