from database import Session
from model.jogo import Jogo


# Cria a sessão
session = Session()


# Busca o Minecraft
minecraft = session.query(Jogo).filter(
    Jogo.nome == "Minecraft"
).first()


if minecraft:

    # Coloque aqui o preço correto
    minecraft.preco = 99.00

    session.commit()

    print("Preço do Minecraft atualizado!")

else:

    print("Minecraft não encontrado.")


# Fecha a sessão
session.close()
