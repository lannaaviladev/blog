from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
