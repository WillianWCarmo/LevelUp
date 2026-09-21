from database import Session
from model.jogo import Jogo


# Cria a sessão
session = Session()


# Busca o Minecraft
minecraft = session.query(Jogo).filter(
    Jogo.nome == "Minecraft"
).first()

if minecraft:
    minecraft.steam = "https://www.minecraft.net/en-us/store/minecraft-java-bedrock-edition-pc"


# Busca o Valorant
valorant = session.query(Jogo).filter(
    Jogo.nome == "Valorant"
).first()

if valorant:
    valorant.steam = "https://playvalorant.com/pt-br/platform-selection/"


# Salva as alterações
session.commit()


# Fecha a sessão
session.close()


print("Links atualizados!")