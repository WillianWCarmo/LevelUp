from sqlalchemy import Column, Integer, String, Float

from database import Base


# Model dos jogos
class Jogo(Base):

    # Nome da tabela
    __tablename__ = "jogos"

    # ID do jogo
    id = Column(Integer, autoincrement=True, primary_key=True)

    # Nome do jogo
    nome = Column(String(100), nullable=False)

    # Descrição do jogo
    descricao = Column(String(250))

    # Sinopse do jogo
    sinopse = Column(String(1000))

    # Gênero do jogo
    genero = Column(String(100))

    # Plataforma do jogo
    plataforma = Column(String(100))

    # Preço do jogo
    preco = Column(Float, nullable=False, default=0.0)

    # Caminho da imagem
    imagem = Column(String(250))

    # Link da Steam
    steam = Column(String(300))

    # Construtor
    def __init__(
        self,
        nome: str,
        descricao: str,
        sinopse: str,
        genero: str,
        plataforma: str,
        preco: float,
        imagem: str,
        steam: str
    ):
        self.nome = nome
        self.descricao = descricao
        self.sinopse = sinopse
        self.genero = genero
        self.plataforma = plataforma
        self.preco = float(preco)
        self.imagem = imagem
        self.steam = steam