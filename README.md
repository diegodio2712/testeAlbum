# ⚽ Álbum de Figurinhas — Estilo Panini Copa 2026

Aplicativo Streamlit para colecionar figurinhas personalizadas de uma turma, inspirado no álbum Panini da Copa do Mundo 2026.

## 🚀 Como Rodar

```bash
pip install streamlit
cd figurinhas
streamlit run app.py
```

## 🎨 Personalização

### Trocar os dados da turma
Edite o arquivo `data.py`:

1. **TEAM_NAME** — Nome da turma/grupo
2. **TEAM_MOTTO** — Subtítulo do álbum
3. **TEAM_COLORS** — Cores do tema
4. **STUDENTS** — Dicionário com os membros:

```python
"ID_UNICO": {
    "name": "Nome Completo",
    "nickname": "Apelido",
    "number": 1,                    # Número da figurinha
    "position": "Função/Cargo",     # Ex: "Atacante", "Designer"
    "fun_fact": "Curiosidade",
    "group": "Nome do Grupo",       # Agrupamento no álbum
    "photo_url": "",                # URL ou caminho da foto (vazio = iniciais)
}
```

### Usar fotos reais
Coloque a URL da foto no campo `photo_url`. Aceita URLs externas ou caminhos locais.

### Trocar as cores
Edite `TEAM_COLORS` em `data.py`:
- `primary` — Fundo escuro
- `secondary` — Baby blue (cor principal do sticker)
- `accent` — Dourado (destaques)
- `sticker_bg` — Fundo do sticker
- `sticker_bar` — Barra do nome
- `sticker_text` — Texto na barra
- `sticker_number_bg` — Fundo do número

## 📁 Estrutura

```
figurinhas/
├── app.py          # App principal Streamlit
├── data.py         # Dados da turma (EDITE ESTE ARQUIVO)
├── sticker_svg.py  # Gerador de SVG das figurinhas
└── README.md       # Este arquivo
```

## 🔐 Login
Atualmente o login Google é **mock** (simulado). Para implementar login real, 
substitua a função `show_login()` em `app.py` por uma integração OAuth2.

## 🎯 Features
- ✅ Pacotes de 7 figurinhas infinitos
- ✅ Álbum com figurinhas coletadas e não coletadas (P&B)
- ✅ Design estilo Panini Copa 2026 (baby blue, dourado, barra azul)
- ✅ Contagem de repetidas
- ✅ Barra de progresso
- ✅ Estatísticas (únicas, total, pacotes, %)
- ✅ Agrupamento por categorias
- ✅ Login mock (Google)
- ✅ 30 membros mock para teste
