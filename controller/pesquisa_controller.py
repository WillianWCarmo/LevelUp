from flask import Blueprint, render_template, request

from repository.jogo_repo import JogoRepository


# Cria o Blueprint
pesquisa_bp = Blueprint("pesquisa", __name__)


# Pesquisa os jogos
@pesquisa_bp.route("/pesquisar")
def pesquisar():

    # Pega o texto digitado
    termo = request.args.get("pesquisa", "")

    # Cria o repositório
    repository = JogoRepository()

    # Pesquisa no banco
    jogos = repository.pesquisar(termo)

    # Envia o resultado para a página
    return render_template(
        "pesquisa.html",
        jogos=jogos,
        termo=termo
    )