from database import Session
from model.jogo import Jogo

class JogoRepository:
    # Cria a sessão
    def __init__(self):
        self.__session = Session()

    # Cadastra um jogo
    def cadastrar(self, jogo):

        self.__session.add(jogo)
        self.__session.commit()
        self.__session.close()

    # Lista todos os jogos
    def listar(self):

        jogos = self.__session.query(Jogo).all()
        self.__session.close()

        return jogos

    # Pesquisa pelo nome
    def pesquisar(self, termo):

        jogos = self.__session.query(Jogo).filter(
            Jogo.nome.like(f"%{termo}%")
        ).all()

        self.__session.close()

        return jogos

    # Busca um jogo pelo ID
    def buscar_por_id(self, id):

        jogo = self.__session.query(Jogo).filter(
            Jogo.id == id
        ).first()

        self.__session.close()
        return jogo