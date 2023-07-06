from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'DEN'
    })  # no caso acima render recebe 3 parametros. A request, o caminho e o CONTEXT que é um parametro que ele entrega para o HTML


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return HttpResponse('contato')
