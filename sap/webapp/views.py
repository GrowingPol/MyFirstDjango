from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    messages = {'msg1': 'Mensaje 1', 'msg2': 'Mensaje 2'}
    return render(request, 'bienvenido.html',messages)#busca en templates / e tercer parámetro es para valores
def despedirse(request):
    return HttpResponse('Adiós Mundo')