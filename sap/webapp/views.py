from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html',{"no_personas":no_personas,
                                              "personas":personas})#busca en templates / e tercer parámetro es para valores

def detallePersona(request,id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request,'personas/detalle.html', {"persona": persona})

# def despedirse(request):
#     return HttpResponse('Adiós Mundo')