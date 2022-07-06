from django.http import HttpResponse
from django.shortcuts import render

# Create your vie here.
from webapp.models import *


def login(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration.html')

def docente(request):
    return render(request, 'docente.html')

def estudiantes(request):
    estudiant = Estudiante.objects.all()
    return render(request, 'profesorcurso.html', {'estu': estudiant})

def perfil(request):
    return render(request, 'perfil.html')