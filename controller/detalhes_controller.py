from flask import Blueprint, render_template

from repository.jogo_repo import JogoRepository


# Cria o Blueprint
detalhes_bp = Blueprint("detalhes", __name__)


# Página de detalhes do jogo
@detalhes_bp.route("/jogo/<int:id>")
def detalhes(id):

    # Cria o repositório
    repository = JogoRepository()

    # Busca o jogo pelo ID
    jogo_encontrado = repository.buscar_por_id(id)

    # Envia o jogo para o HTML
    return render_template(
        "detalhes.html",
        jogo=jogo_encontrado
    )