from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def equipe(request):
    return render(request, 'equipe.html')

def sobre(request):
    return render(request, 'sobre.html')
