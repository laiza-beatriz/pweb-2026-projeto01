from django.db import models

from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=50)
    idade = models.CharField(max_length=20)  
    foto = models.ImageField(upload_to='jogadores/', null=True, blank=True)
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    idade = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='alunos/', null=True, blank=True)
    
    def __str__(self):
        return self.nome
