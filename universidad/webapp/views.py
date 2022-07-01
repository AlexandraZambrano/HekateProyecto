from django.http import HttpResponse
from django.shortcuts import render

# Create your vie here.
def login(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration.html')

def docente(request):
    return render(request, 'docente.html')