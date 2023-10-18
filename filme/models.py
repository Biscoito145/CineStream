from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

LISTA_CATEGORIA = (
    ('ACAO', 'Ação'),
    ('COMEDIA', 'Comédia'),
    ('TERROR', 'Terror'),
    ('SUSPENSE', 'Suspense'),
    ('DRAMA', 'Drama'),
    ('ANIMACAO', 'Animações'),
    ('DOCUMENTARIO', 'Documentário')
)

# criar filme


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# criar espisodio
class Episodio(models.Model):
    filme = models.ForeignKey('Filme', related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()


    def __str__(self):
        return self.filme.titulo + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')