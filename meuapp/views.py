from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def equipe(request):
    jogador = [
        {
            'nome': 'Hinata',
            'posicao': 'Central',
            'idade': '16 anos',
        },

        {
            'nome': 'Kageyama',
            'posicao': 'Levantador',
            'idade': '16 anos',
        },

        {
            'nome': 'Yamaguchi',
            'posicao': 'Central',
            'idade': '16 anos',
        },

        {
            'nome': 'Daichi',
            'posicao': 'Ponteiro',
            'idade': '18 anos',
        },

        {
            'nome': 'Nishinoya',
            'posicao': 'Líbero',
            'idade': '16 anos',
        },

        {
            'nome': 'Tsukishima',
            'posicao': 'Central',
            'idade': '16 anos',
        },

        {
            'nome': 'Asahi',
            'posicao': 'Ponteiro',
            'idade': '18 anos',
        },

        {
            'nome': 'Tanaka',
            'posicao': 'Ponteiro',
            'idade': '18 anos',
        },
    ]

    context = {
        'jogador': jogador
    }

    return render(request, 'equipe.html', context)


def sobre(request):

    alunos = [
        {
            'nome': 'Laíza',
            'curso': 'Técnica em infoweb',
            'idade': '17 anos',
        },

        {
            'nome': 'Samuel',
            'curso': 'Técnico em infoweb',
            'idade': '17 anos',
        }
    ]

    descricao = """
    Somos alunos do IFRNSPP cursando Informática para internet.
    Escolhemos esse anime Haikyuu! para fazer o projeto da matéria
    programação web, onde apresentamos a equipe Karasuno.
    """

    context = {
        'alunos': alunos,
        'descricao': descricao
    }

    return render(request, 'sobre.html', context)