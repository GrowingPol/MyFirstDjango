from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    no_personas = Persona.objects.count()
    return render(request, 'bienvenido.html',{"no_personas":no_personas})#busca en templates / e tercer parámetro es para valores
def despedirse(request):
    return HttpResponse('Adiós Mundo')