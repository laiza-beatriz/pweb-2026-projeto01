from django.shortcuts import render
from .models import Jogador, Aluno  

def index(request):
    return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def equipe(request):
    jogadores_db = Jogador.objects.all()

    context = {
        'jogador': jogadores_db  
    }
    return render(request, 'equipe.html', context)

def sobre(request):
    alunos_db = Aluno.objects.all()

    descricao = """
    Somos alunos do IFRNSPP cursando Informática para internet.
    Escolhemos esse anime Haikyuu! para fazer o projeto da matéria
    programação web, onde apresentamos a equipe Karasuno.
    """

    context = {
        'alunos': alunos_db,  
        'descricao': descricao
    }
    return render(request, 'sobre.html', context)