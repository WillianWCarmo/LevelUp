from flask import Flask

# Importa os controllers
from controller.index_controller import index_bp
from controller.sobre_controller import sobre_bp
from controller.contato_controller import contato_bp
from controller.jogos_controller import jogos_bp
from controller.detalhes_controller import detalhes_bp
from controller.pesquisa_controller import pesquisa_bp

# Importa o banco de dados
from database import Base, engine

# Importa o Model
from model.jogo import Jogo

# Cria a aplicação Flask
app = Flask(__name__)

# Chave usada pelo flash()
app.secret_key = "level-up-catalogo-jogos-2025"

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Registra os controllers
app.register_blueprint(index_bp)
app.register_blueprint(sobre_bp)
app.register_blueprint(contato_bp)
app.register_blueprint(jogos_bp)
app.register_blueprint(detalhes_bp)
app.register_blueprint(pesquisa_bp)


# Inicia o servidor
if __name__ == "__main__":
    app.run(port=9000, debug=True)