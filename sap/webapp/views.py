from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola Mundo')
def despedirse(request):
    return HttpResponse('Adiós Mundo')