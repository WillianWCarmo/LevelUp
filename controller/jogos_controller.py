from flask import Blueprint, render_template
from repository.jogo_repo import JogoRepository

# Cria o Blueprint
jogos_bp = Blueprint("jogos", __name__)

# Página de jogos
@jogos_bp.route("/jogos")
def jogos():

    # Cria o repositório
    repository = JogoRepository()

    # Busca os jogos no banco
    lista_jogos = repository.listar()

    # Envia os jogos para o HTML
    return render_template(
        "jogos.html",
        jogos=lista_jogos
    )