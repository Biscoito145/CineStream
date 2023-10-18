from .models import Filme


def lista_filmes_recentes(reqquest):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filmes_destaque = lista_filmes[0]
    else:
        filmes_destaque = None
    return {'lista_filmes_recentes': lista_filmes, 'filme_destaque': filmes_destaque}

def lista_filmes_emalta(reqquest):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {'lista_filmes_emalta': lista_filmes}

