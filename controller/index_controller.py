from flask import Blueprint, render_template

from repository.jogo_repo import JogoRepository


# Cria o Blueprint
index_bp = Blueprint("index", __name__)


# Página inicial
@index_bp.route("/")
def index():

    # Cria o repositório
    repository = JogoRepository()

    # Busca os jogos no banco
    lista_jogos = repository.listar()

    # Pega os 3 primeiros jogos
    jogos_destaque = lista_jogos[:3]

    # Envia os jogos para a página
    return render_template(
        "index.html",
        jogos=jogos_destaque
    )