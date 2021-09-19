from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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

PersonaForm = modelform_factory(Persona, exclude=[]) #Objeto de formulario relacionado al objeto del modelo
def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()

    return render(request,'personas/nuevo.html',{'formaPersona':formaPersona})

# def despedirse(request):
#     return HttpResponse('Adiós Mundo')