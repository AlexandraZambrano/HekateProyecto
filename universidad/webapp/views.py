from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your vie here.
from webapp.forms import RegistroForm, RegForm
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

def estudianteNuevo(request):
    if request.method == 'POST':
        formaEstudiantes = RegistroForm(request.POST)
        if formaEstudiantes.is_valid():
            formaEstudiantes.save()
            return redirect('estudiante')

    else:
        formaEstudiantes = RegistroForm

        return render(request, 'NuevoEstudiante.html', {'forestudiante': formaEstudiantes})

def editarEstudiante(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if request.method == 'POST':
        formaEstudiantes = RegistroForm(request.POST, instance=estudiante)
        if formaEstudiantes.is_valid():
            formaEstudiantes.save()
            return redirect('estudiante')

    else:
        formaEstudiantes = RegistroForm(instance=estudiante)

    return render(request, 'editar.html', {'forestudiante': formaEstudiantes})

def eliminarEstudiante(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if estudiante:
        estudiante.delete()
        return redirect('estudiante')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

        return render(request, 'registration.html', {'formUser': form})