from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'DEN'
    })  # 3 parametros, context é passado ao html


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return HttpResponse('contato')
