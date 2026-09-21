from database import Session, Base, engine
from model.jogo import Jogo


# Cria a tabela
Base.metadata.create_all(bind=engine)


# Cria a sessão
session = Session()


# Lista de jogos
lista_jogos = [

    Jogo(
        nome="Minecraft",
        descricao="Jogo de construção e exploração em mundo aberto.",
        sinopse="Minecraft é um jogo sandbox onde você pode explorar mundos infinitos, minerar recursos, construir estruturas e sobreviver a criaturas hostis. Com modos criativo e sobrevivência, oferece liberdade total para criar o que quiser, sozinho ou com amigos.",
        genero="Sandbox",
        plataforma="PC",
        preco=99.90,
        imagem="/static/imagens/minecraft.webp",
        steam="https://store.steampowered.com/app/1672970/Minecraft/"
    ),

    Jogo(
        nome="GTA V",
        descricao="Jogo de ação e aventura em mundo aberto.",
        sinopse="Grand Theft Auto V acompanha três criminosos — Michael, Franklin e Trevor — em Los Santos, uma cidade inspirada em Los Angeles. Com missões variadas, exploração livre e um modo online massivo, é um dos jogos mais vendidos de todos os tempos.",
        genero="Ação",
        plataforma="PC",
        preco=79.90,
        imagem="/static/imagens/gta.png",
        steam="https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/"
    ),

    Jogo(
        nome="FIFA 25",
        descricao="Jogo de futebol com diversos times e competições.",
        sinopse="EA Sports FC 25 traz partidas de futebol com diversos times, jogadores e competições. O jogo possui modos como Ultimate Team e Carreira.",
        genero="Esporte",
        plataforma="PlayStation",
        preco=299.90,
        imagem="/static/imagens/fifa.png",
        steam="https://store.steampowered.com/app/2669320/EA_SPORTS_FC_25/"
    ),

    Jogo(
        nome="God of War",
        descricao="Aventura de Kratos e seu filho Atreus pela mitologia nórdica.",
        sinopse="Após os eventos da mitologia grega, Kratos vive no reino nórdico com seu filho Atreus. Juntos, eles enfrentam deuses, monstros e seus próprios passados em uma jornada que mistura ação e exploração.",
        genero="Ação/Aventura",
        plataforma="PlayStation",
        preco=199.90,
        imagem="/static/imagens/gow.jpg",
        steam="https://store.steampowered.com/app/1593500/God_of_War/"
    ),

    Jogo(
        nome="Hogwarts Legacy",
        descricao="RPG de ação e aventura ambientado no mundo mágico de Harry Potter.",
        sinopse="Ambientado no século XIX, Hogwarts Legacy coloca você como um estudante de Hogwarts com a habilidade de manipular magia antiga. Explore o castelo, aprenda feitiços e enfrente diferentes desafios.",
        genero="RPG/Aventura",
        plataforma="PC, PlayStation, Xbox e Nintendo Switch",
        preco=249.90,
        imagem="/static/imagens/hogwarts.jpg",
        steam="https://store.steampowered.com/app/990080/Hogwarts_Legacy/"
    ),

    Jogo(
        nome="Silksong",
        descricao="Aventura de ação e exploração em que Hornet enfrenta novos desafios em um reino misterioso.",
        sinopse="Silksong é a sequência de Hollow Knight. Você controla Hornet enquanto explora um novo reino, enfrenta inimigos e descobre novos lugares e desafios.",
        genero="Metroidvania/Ação",
        plataforma="PC, Nintendo Switch, PlayStation e Xbox",
        preco=69.90,
        imagem="/static/imagens/silksong.jpg",
        steam="https://store.steampowered.com/app/1030300/Hollow_Knight_Silksong/"
    ),

    Jogo(
        nome="Valorant",
        descricao="Jogo de tiro tático em primeira pessoa com agentes que possuem habilidades únicas.",
        sinopse="Valorant é um FPS tático 5v5 da Riot Games, onde cada agente possui habilidades únicas. O jogo mistura estratégia, mira e trabalho em equipe.",
        genero="FPS/Tiro Tático",
        plataforma="PC e Console",
        preco=0.00,
        imagem="/static/imagens/vava.png",
        steam=""
    ),

    Jogo(
        nome="It Takes Two",
        descricao="Jogo cooperativo de aventura em que dois jogadores precisam trabalhar juntos para superar desafios.",
        sinopse="It Takes Two é um jogo cooperativo para dois jogadores. Cody e May são transformados em bonecos e precisam trabalhar juntos para superar diversos desafios.",
        genero="Aventura/Cooperativo",
        plataforma="PC, PlayStation e Xbox",
        preco=199.90,
        imagem="/static/imagens/ittakestwo.jpg",
        steam="https://store.steampowered.com/app/1426210/It_Takes_Two/"
    )

]


# Percorre os jogos
for jogo in lista_jogos:

    # Verifica se o jogo já existe
    jogo_existente = session.query(Jogo).filter(
        Jogo.nome == jogo.nome
    ).first()

    if jogo_existente is None:

        # Cadastra o jogo
        session.add(jogo)

        print(f"Jogo cadastrado: {jogo.nome}")

    else:

        print(f"Jogo já existe: {jogo.nome}")


# Salva as alterações
session.commit()


# Fecha a sessão
session.close()


print("Carga inicial finalizada!")