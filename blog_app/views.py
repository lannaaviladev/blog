from django.shortcuts import render
from .models import Curso, Interesse

def home(request):
    cursos = Curso.objects.all()
    interesses = Interesse.objects.all()
    return render(request, 'home.html', {'cursos': cursos, 'interesses': interesses})


def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')
