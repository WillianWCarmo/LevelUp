from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Configuração do banco
DATABASE_URL = "mysql+pymysql://root:1234@localhost/catalogo_jogos"


# Cria a conexão com o banco
engine = create_engine(
    DATABASE_URL,
    echo=False
)


# Cria as sessões
Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# Base usada pelos Models
Base = declarative_base()