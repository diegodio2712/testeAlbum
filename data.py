# ============================================================
# DATA.PY — Dados da Turma (Mock)
# ============================================================
# COMO SUBSTITUIR PELOS DADOS REAIS:
# 1. Troque as entries em STUDENTS com nomes, apelidos, posicoes e fotos reais.
#    - "photo_url": coloque a URL de uma foto ou caminho local
#    - "number": número da figurinha
#    - "position": "cargo" ou função da pessoa
#    - "fun_fact": curiosidade sobre a pessoa
#    - "group": agrupamento (ex: "Diretoria", "Marketing", etc.)
# 2. Ajuste TEAM_NAME, TEAM_MOTTO e TEAM_COLORS.
# 3. As fotos mock usam iniciais geradas por SVG, então não precisa de URL.
# ============================================================

TEAM_NAME = "Turma 2026"
TEAM_MOTTO = "Coleção Oficial de Figurinhas"

# Cores do tema — inspiradas no álbum Panini Copa 2026
TEAM_COLORS = {
    "primary": "#0a1628",       # azul escuro de fundo
    "secondary": "#a8d8ea",     # baby blue (cor principal do sticker 2026)
    "accent": "#d4a843",        # dourado
    "sticker_bg": "#c9e7f2",    # fundo do sticker (baby blue claro)
    "sticker_bar": "#1a3a5c",   # barra azul escura do nome (como no Panini 2026)
    "sticker_text": "#ffffff",  # texto na barra
    "sticker_number_bg": "#d4a843",  # fundo do número
}

# ============================================================
# ALUNOS / MEMBROS DA TURMA (Mock - 30 pessoas)
# ============================================================
# Cada entrada:
#   "id_unico": {
#       "name": "Nome Completo",
#       "nickname": "Apelido",
#       "number": N,            # Número da figurinha
#       "position": "Função",   # Ex: "Atacante", "Designer", "CEO"
#       "fun_fact": "Curiosidade",
#       "group": "Grupo",       # Agrupamento no álbum
#       "photo_url": ""         # URL da foto (vazio = usa iniciais)
#   }

STUDENTS = {
    "STU001": {
        "name": "Lucas Oliveira",
        "nickname": "Lukinha",
        "number": 1,
        "position": "Líder de Turma",
        "fun_fact": "Faz o melhor café da sala",
        "group": "Diretoria",
        "photo_url": "",
    },
    "STU002": {
        "name": "Mariana Santos",
        "nickname": "Mari",
        "number": 2,
        "position": "Vice-Líder",
        "fun_fact": "Já visitou 12 países",
        "group": "Diretoria",
        "photo_url": "",
    },
    "STU003": {
        "name": "Pedro Henrique Costa",
        "nickname": "PH",
        "number": 3,
        "position": "Tesoureiro",
        "fun_fact": "Campeão de xadrez da escola",
        "group": "Diretoria",
        "photo_url": "",
    },
    "STU004": {
        "name": "Ana Beatriz Lima",
        "nickname": "Bia",
        "number": 4,
        "position": "Secretária",
        "fun_fact": "Coleciona adesivos desde os 5 anos",
        "group": "Diretoria",
        "photo_url": "",
    },
    "STU005": {
        "name": "Gabriel Souza",
        "nickname": "Gabi",
        "number": 5,
        "position": "Artilheiro",
        "fun_fact": "Sonha em jogar no Barça",
        "group": "Atletas",
        "photo_url": "",
    },
    "STU006": {
        "name": "Isabela Ferreira",
        "nickname": "Bela",
        "number": 6,
        "position": "Goleira",
        "fun_fact": "Treina muay thai nas férias",
        "group": "Atletas",
        "photo_url": "",
    },
    "STU007": {
        "name": "Rafael Almeida",
        "nickname": "Rafa",
        "number": 7,
        "position": "Meia",
        "fun_fact": "Toca violão desde os 8",
        "group": "Atletas",
        "photo_url": "",
    },
    "STU008": {
        "name": "Juliana Rodrigues",
        "nickname": "Ju",
        "number": 8,
        "position": "Zagueira",
        "fun_fact": "Melhor nota em matemática",
        "group": "Atletas",
        "photo_url": "",
    },
    "STU009": {
        "name": "Thiago Barbosa",
        "nickname": "Thi",
        "number": 9,
        "position": "Atacante",
        "fun_fact": "Come pizza todo fim de semana",
        "group": "Atletas",
        "photo_url": "",
    },
    "STU010": {
        "name": "Camila Nascimento",
        "nickname": "Cami",
        "number": 10,
        "position": "Lateral",
        "fun_fact": "Fã de anime desde criança",
        "group": "Atletas",
        "photo_url": "",
    },
    "STU011": {
        "name": "Bruno Martins",
        "nickname": "Brunão",
        "number": 11,
        "position": "Nerd Oficial",
        "fun_fact": "Já leu Harry Potter 7 vezes",
        "group": "Acadêmicos",
        "photo_url": "",
    },
    "STU012": {
        "name": "Letícia Araújo",
        "nickname": "Lê",
        "number": 12,
        "position": "Monitora de Física",
        "fun_fact": "Quer ser astronauta",
        "group": "Acadêmicos",
        "photo_url": "",
    },
    "STU013": {
        "name": "Matheus Cardoso",
        "nickname": "Math",
        "number": 13,
        "position": "Monitor de Matemática",
        "fun_fact": "Resolve cubo mágico em 30s",
        "group": "Acadêmicos",
        "photo_url": "",
    },
    "STU014": {
        "name": "Fernanda Lopes",
        "nickname": "Fer",
        "number": 14,
        "position": "Monitora de Biologia",
        "fun_fact": "Tem 3 gatos e 2 cachorros",
        "group": "Acadêmicos",
        "photo_url": "",
    },
    "STU015": {
        "name": "Vinícius Pereira",
        "nickname": "Vini",
        "number": 15,
        "position": "Monitor de Química",
        "fun_fact": "Cozinha melhor que muitos chefs",
        "group": "Acadêmicos",
        "photo_url": "",
    },
    "STU016": {
        "name": "Sofia Melo",
        "nickname": "Sô",
        "number": 16,
        "position": "Artista",
        "fun_fact": "Desenha mangá nas aulas vagas",
        "group": "Criativos",
        "photo_url": "",
    },
    "STU017": {
        "name": "Enzo Ribeiro",
        "nickname": "Enzinho",
        "number": 17,
        "position": "Fotógrafo",
        "fun_fact": "Tem um canal no YouTube",
        "group": "Criativos",
        "photo_url": "",
    },
    "STU018": {
        "name": "Valentina Castro",
        "nickname": "Val",
        "number": 18,
        "position": "Designer",
        "fun_fact": "Já fez figurino de peça",
        "group": "Criativos",
        "photo_url": "",
    },
    "STU019": {
        "name": "Arthur Gonçalves",
        "nickname": "Arthurzão",
        "number": 19,
        "position": "DJ da Turma",
        "fun_fact": "Mixou no festival da escola",
        "group": "Criativos",
        "photo_url": "",
    },
    "STU020": {
        "name": "Laura Duarte",
        "nickname": "Laurinha",
        "number": 20,
        "position": "Atriz",
        "fun_fact": "Ganhou prêmio de teatro",
        "group": "Criativos",
        "photo_url": "",
    },
    "STU021": {
        "name": "Davi Moreira",
        "nickname": "Davizão",
        "number": 21,
        "position": "Comediante",
        "fun_fact": "Faz todo mundo rir no intervalo",
        "group": "Entretenimento",
        "photo_url": "",
    },
    "STU022": {
        "name": "Maria Eduarda Teixeira",
        "nickname": "Duda",
        "number": 22,
        "position": "Influencer",
        "fun_fact": "10k seguidores no TikTok",
        "group": "Entretenimento",
        "photo_url": "",
    },
    "STU023": {
        "name": "Felipe Azevedo",
        "nickname": "Felipão",
        "number": 23,
        "position": "Gamer",
        "fun_fact": "Ranqueado Diamante no LoL",
        "group": "Entretenimento",
        "photo_url": "",
    },
    "STU024": {
        "name": "Giovanna Pinto",
        "nickname": "Gi",
        "number": 24,
        "position": "Cantora",
        "fun_fact": "Canta no coral da igreja",
        "group": "Entretenimento",
        "photo_url": "",
    },
    "STU025": {
        "name": "Henrique Fonseca",
        "nickname": "Riq",
        "number": 25,
        "position": "Mestre de RPG",
        "fun_fact": "Narra campanhas épicas de D&D",
        "group": "Entretenimento",
        "photo_url": "",
    },
    "STU026": {
        "name": "Beatriz Correia",
        "nickname": "Bia C.",
        "number": 26,
        "position": "Representante",
        "fun_fact": "Conhece todo mundo da escola",
        "group": "Líderes",
        "photo_url": "",
    },
    "STU027": {
        "name": "João Victor Nunes",
        "nickname": "JV",
        "number": 27,
        "position": "Organizador",
        "fun_fact": "Planilha para tudo na vida",
        "group": "Líderes",
        "photo_url": "",
    },
    "STU028": {
        "name": "Alice Mendes",
        "nickname": "Licinha",
        "number": 28,
        "position": "Mediadora",
        "fun_fact": "Nunca se atrasa para nada",
        "group": "Líderes",
        "photo_url": "",
    },
    "STU029": {
        "name": "Miguel Campos",
        "nickname": "Migué",
        "number": 29,
        "position": "Orador",
        "fun_fact": "Ganhou concurso de debate",
        "group": "Líderes",
        "photo_url": "",
    },
    "STU030": {
        "name": "Helena Rocha",
        "nickname": "Lena",
        "number": 30,
        "position": "Presidente do Grêmio",
        "fun_fact": "Organizou a melhor festa junina",
        "group": "Líderes",
        "photo_url": "",
    },
}
