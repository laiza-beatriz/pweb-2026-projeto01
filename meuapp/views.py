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
            'imagem': 'img/hinata.png.jpeg',
        },

        {
            'nome': 'Kageyama',
            'posicao': 'Levantador',
            'idade': '16 anos',
            'imagem': 'img/kageyama.png.jpeg',
        },

        {
            'nome': 'Yamaguchi',
            'posicao': 'Central',
            'idade': '16 anos',
            'imagem': 'img/yamaguchi.png.jpeg',
        },

        {
            'nome': 'Daichi',
            'posicao': 'Ponteiro',
            'idade': '18 anos',
            'imagem': 'img/daichi.png.jpeg',
        },

        {
            'nome': 'Nishinoya',
            'posicao': 'Líbero',
            'idade': '16 anos',
            'imagem': 'img/nishinoya.png.jpeg',
        },

        {
            'nome': 'Tsukishima',
            'posicao': 'Central',
            'idade': '16 anos',
            'imagem': 'img/tsukishima.png.jpeg',
        },

        {
            'nome': 'Asahi',
            'posicao': 'Ponteiro',
            'idade': '18 anos',
            'imagem': 'img/asahi.png.jpeg',
        },

        {
            'nome': 'Tanaka',
            'posicao': 'Ponteiro',
            'idade': '18 anos',
            'imagem': 'img/tanaka.png.jpeg',
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
            'imagem': 'img/laiza.png.jpeg',
        },

        {
            'nome': 'Samuel',
            'curso': 'Técnico em infoweb',
            'idade': '17 anos',
            'imagem': 'img/samuel.png.jpeg',
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