import re
import requests

from database import Session
from model.jogo import Jogo

# Cria a sessão
session = Session()

# Busca todos os jogos
jogos = session.query(Jogo).all()

# Percorre os jogos
for jogo in jogos:

    # Ignora jogos sem link da Steam
    if not jogo.steam:
        print(f"{jogo.nome}: não possui link da Steam")
        continue

    # Pega o AppID da URL
    resultado = re.search(r"/app/(\d+)", jogo.steam)

    if resultado is None:
        print(f"{jogo.nome}: AppID não encontrado")
        continue

    appid = resultado.group(1)

    # URL usada para consultar a Steam
    url = "https://store.steampowered.com/api/appdetails"

    parametros = {
        "appids": appid,
        "cc": "br",
        "l": "brazilian"
    }

    try:
        # Faz a requisição
        resposta = requests.get(
            url,
            params=parametros,
            timeout=10
        )
        resposta.raise_for_status()

        dados = resposta.json()

        # Pega os dados do jogo
        dados_jogo = dados.get(appid)

        if not dados_jogo or not dados_jogo.get("success"):
            print(f"{jogo.nome}: não encontrado na Steam")
            continue

        dados_jogo = dados_jogo["data"]

        # Verifica se o jogo é gratuito
        if dados_jogo.get("is_free"):
            preco_novo = 0.0

        # Verifica se existe preço
        elif "price_overview" in dados_jogo:
            preco_centavos = dados_jogo["price_overview"]["final"]
            preco_novo = preco_centavos / 100

        else:
            print(f"{jogo.nome}: preço não disponível")
            continue

        # Mostra o preço antigo
        preco_antigo = jogo.preco

        # Atualiza o preço
        jogo.preco = preco_novo

        print(
            f"{jogo.nome}: "
            f"R$ {preco_antigo:.2f} -> R$ {preco_novo:.2f}"
        )


    except Exception as erro:

        print(f"Erro ao atualizar {jogo.nome}: {erro}")

# Salva as alterações
session.commit()

# Fecha a sessão
session.close()

print("Preços atualizados!")