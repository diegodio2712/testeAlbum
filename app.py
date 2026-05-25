import streamlit as st
import json
import random
import hashlib
from datetime import datetime
from data import STUDENTS, TEAM_NAME, TEAM_MOTTO, TEAM_COLORS
from sticker_svg import render_sticker_svg, render_sticker_placeholder_svg, render_pack_svg

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(
    page_title=f"Álbum de Figurinhas — {TEAM_NAME}",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PACK_SIZE = 7

# ============================================================
# SESSION STATE INIT
# ============================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""
    st.session_state.user_email = ""
    st.session_state.user_photo = ""

if "collection" not in st.session_state:
    # dict: student_id -> count of how many times pulled
    st.session_state.collection = {}

if "packs_opened" not in st.session_state:
    st.session_state.packs_opened = 0

if "current_pack" not in st.session_state:
    st.session_state.current_pack = None

if "pack_reveal_index" not in st.session_state:
    st.session_state.pack_reveal_index = -1

if "total_stickers" not in st.session_state:
    st.session_state.total_stickers = 0


# ============================================================
# CSS
# ============================================================
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Barlow+Condensed:wght@400;500;600;700&family=Barlow:wght@400;500;600&display=swap');

    :root {
        --primary: """ + TEAM_COLORS["primary"] + """;
        --secondary: """ + TEAM_COLORS["secondary"] + """;
        --accent: """ + TEAM_COLORS["accent"] + """;
        --bg-dark: #0a1628;
        --bg-card: #0f1f3a;
        --gold: #d4a843;
        --baby-blue: #a8d8ea;
        --text-light: #e8edf3;
    }

    .stApp {
        background: linear-gradient(135deg, var(--bg-dark) 0%, #0d1a30 50%, #091220 100%);
    }

    /* Hide streamlit defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding-top: 1rem !important;
        max-width: 1200px;
    }

    /* Album header */
    .album-header {
        text-align: center;
        padding: 2rem 1rem;
        margin-bottom: 2rem;
        background: linear-gradient(180deg, rgba(168,216,234,0.1) 0%, transparent 100%);
        border-bottom: 3px solid var(--gold);
        position: relative;
    }
    .album-header::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(
            90deg,
            transparent,
            transparent 80px,
            rgba(212,168,67,0.03) 80px,
            rgba(212,168,67,0.03) 82px
        );
        pointer-events: none;
    }
    .album-title {
        font-family: 'Oswald', sans-serif;
        font-weight: 700;
        font-size: 3rem;
        color: var(--gold);
        text-transform: uppercase;
        letter-spacing: 4px;
        margin: 0;
        text-shadow: 0 2px 20px rgba(212,168,67,0.3);
    }
    .album-subtitle {
        font-family: 'Barlow Condensed', sans-serif;
        font-weight: 500;
        font-size: 1.3rem;
        color: var(--baby-blue);
        letter-spacing: 6px;
        text-transform: uppercase;
        margin-top: 0.3rem;
    }
    .album-year {
        font-family: 'Oswald', sans-serif;
        font-size: 8rem;
        font-weight: 700;
        color: rgba(168,216,234,0.06);
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        pointer-events: none;
        letter-spacing: 20px;
    }

    /* Stats bar */
    .stats-bar {
        display: flex;
        justify-content: center;
        gap: 2.5rem;
        padding: 1rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }
    .stat-item {
        text-align: center;
    }
    .stat-number {
        font-family: 'Oswald', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--gold);
        line-height: 1;
    }
    .stat-label {
        font-family: 'Barlow Condensed', sans-serif;
        font-size: 0.85rem;
        color: var(--baby-blue);
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Login page */
    .login-container {
        max-width: 420px;
        margin: 5rem auto;
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(145deg, rgba(15,31,58,0.9), rgba(10,22,40,0.95));
        border: 1px solid rgba(212,168,67,0.2);
        border-radius: 12px;
    }
    .login-title {
        font-family: 'Oswald', sans-serif;
        font-weight: 700;
        font-size: 2rem;
        color: var(--gold);
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    .google-btn {
        display: inline-flex;
        align-items: center;
        gap: 12px;
        padding: 14px 32px;
        background: white;
        color: #333;
        border-radius: 8px;
        font-family: 'Barlow', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        text-decoration: none;
        margin-top: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s;
        cursor: pointer;
        border: none;
    }
    .google-btn:hover {
        transform: translateY(-2px);
    }

    /* Pack area */
    .pack-area {
        text-align: center;
        padding: 2rem 0;
    }
    .pack-wrapper {
        display: inline-block;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    .pack-wrapper:hover {
        transform: scale(1.03) rotate(-1deg);
    }

    /* Sticker grid */
    .sticker-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
        gap: 1.2rem;
        padding: 1rem 0;
    }
    .sticker-cell {
        text-align: center;
        transition: transform 0.3s;
    }
    .sticker-cell:hover {
        transform: scale(1.05);
    }

    /* Pack reveal */
    .reveal-grid {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
        padding: 1rem 0;
    }
    .reveal-item {
        animation: popIn 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) both;
    }
    @keyframes popIn {
        0% { transform: scale(0) rotate(-15deg); opacity: 0; }
        100% { transform: scale(1) rotate(0); opacity: 1; }
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        justify-content: center;
        border-bottom: 2px solid rgba(212,168,67,0.2);
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'Oswald', sans-serif;
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: var(--baby-blue);
        padding: 0.8rem 2rem;
    }
    .stTabs [aria-selected="true"] {
        color: var(--gold) !important;
        border-bottom-color: var(--gold) !important;
    }

    /* User bar */
    .user-bar {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 10px;
        padding: 0.5rem 1rem;
        font-family: 'Barlow', sans-serif;
        color: var(--baby-blue);
        font-size: 0.9rem;
    }
    .user-avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: var(--gold);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Oswald', sans-serif;
        font-weight: 700;
        color: var(--bg-dark);
        font-size: 0.9rem;
    }

    /* New sticker badge */
    .new-badge {
        display: inline-block;
        background: #e63946;
        color: white;
        font-family: 'Oswald', sans-serif;
        font-size: 0.7rem;
        padding: 2px 8px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 4px;
    }
    .repeat-badge {
        display: inline-block;
        background: rgba(168,216,234,0.15);
        color: var(--baby-blue);
        font-family: 'Oswald', sans-serif;
        font-size: 0.7rem;
        padding: 2px 8px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 4px;
    }

    /* Progress bar */
    .progress-container {
        max-width: 500px;
        margin: 0 auto 1rem;
        text-align: center;
    }
    .progress-bar-bg {
        background: rgba(168,216,234,0.1);
        border-radius: 10px;
        height: 14px;
        overflow: hidden;
        border: 1px solid rgba(212,168,67,0.2);
    }
    .progress-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--gold), #f0c75e);
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    .progress-text {
        font-family: 'Barlow Condensed', sans-serif;
        color: var(--gold);
        font-size: 1rem;
        margin-top: 0.3rem;
        letter-spacing: 1px;
    }

    /* Group header */
    .group-header {
        font-family: 'Oswald', sans-serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: var(--gold);
        text-transform: uppercase;
        letter-spacing: 3px;
        padding: 0.8rem 0 0.5rem;
        border-bottom: 2px solid rgba(212,168,67,0.15);
        margin: 1.5rem 0 1rem;
    }

    /* Button overrides */
    .stButton > button {
        font-family: 'Oswald', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        font-weight: 600 !important;
        border: 2px solid var(--gold) !important;
        background: transparent !important;
        color: var(--gold) !important;
        border-radius: 6px !important;
        padding: 0.6rem 2rem !important;
        transition: all 0.3s !important;
    }
    .stButton > button:hover {
        background: var(--gold) !important;
        color: var(--bg-dark) !important;
    }
    .stButton > button:active, .stButton > button:focus {
        background: var(--gold) !important;
        color: var(--bg-dark) !important;
        border-color: var(--gold) !important;
    }
    </style>
    """, unsafe_allow_html=True)


inject_css()


# ============================================================
# AUTH (MOCK)
# ============================================================
def show_login():
    st.markdown("""
    <div class="login-container">
        <div style="font-size:3rem; margin-bottom:0.5rem;">⚽</div>
        <div class="login-title">Álbum de Figurinhas</div>
        <div style="font-family:'Barlow Condensed',sans-serif; color:var(--baby-blue); 
             font-size:1.1rem; letter-spacing:3px; text-transform:uppercase; margin-top:0.3rem;">
            """ + TEAM_NAME + """
        </div>
        <div style="font-family:'Barlow',sans-serif; color:rgba(168,216,234,0.5); 
             font-size:0.85rem; margin-top:1.5rem; line-height:1.6;">
            Faça login para colecionar figurinhas<br>dos seus colegas de turma!
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.text_input("Nome", key="login_name", placeholder="Seu nome completo")
        st.text_input("E-mail", key="login_email", placeholder="seu@email.com")
        if st.button("🔑  Entrar com Google (Mock)", use_container_width=True):
            if st.session_state.login_name and st.session_state.login_email:
                st.session_state.logged_in = True
                st.session_state.user_name = st.session_state.login_name
                st.session_state.user_email = st.session_state.login_email
                st.rerun()
            else:
                st.warning("Preencha nome e e-mail!")


# ============================================================
# PACK OPENING LOGIC
# ============================================================
def generate_pack():
    """Generate a pack of PACK_SIZE random stickers."""
    ids = list(STUDENTS.keys())
    pack = random.choices(ids, k=PACK_SIZE)
    return pack


def open_pack():
    pack = generate_pack()
    st.session_state.current_pack = pack
    st.session_state.pack_reveal_index = PACK_SIZE  # reveal all at once
    st.session_state.packs_opened += 1
    
    for sid in pack:
        st.session_state.total_stickers += 1
        if sid in st.session_state.collection:
            st.session_state.collection[sid] += 1
        else:
            st.session_state.collection[sid] = 1


# ============================================================
# MAIN APP
# ============================================================
def show_app():
    total_students = len(STUDENTS)
    collected = len(st.session_state.collection)
    pct = int((collected / total_students) * 100) if total_students > 0 else 0

    # User bar
    initials = "".join([p[0].upper() for p in st.session_state.user_name.split()[:2]])
    st.markdown(f"""
    <div class="user-bar">
        <div class="user-avatar">{initials}</div>
        <span>{st.session_state.user_name}</span>
    </div>
    """, unsafe_allow_html=True)

    # Header
    st.markdown(f"""
    <div class="album-header">
        <div class="album-year">26</div>
        <div class="album-title">{TEAM_NAME}</div>
        <div class="album-subtitle">{TEAM_MOTTO}</div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown(f"""
    <div class="stats-bar">
        <div class="stat-item">
            <div class="stat-number">{collected}/{total_students}</div>
            <div class="stat-label">Figurinhas Únicas</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">{st.session_state.total_stickers}</div>
            <div class="stat-label">Total Coletadas</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">{st.session_state.packs_opened}</div>
            <div class="stat-label">Pacotes Abertos</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">{pct}%</div>
            <div class="stat-label">Progresso</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Progress bar
    st.markdown(f"""
    <div class="progress-container">
        <div class="progress-bar-bg">
            <div class="progress-bar-fill" style="width:{pct}%"></div>
        </div>
        <div class="progress-text">{collected} de {total_students} figurinhas</div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs
    tab_pack, tab_album = st.tabs(["📦 Abrir Pacotes", "📖 Álbum"])

    # ------ TAB: OPEN PACKS ------
    with tab_pack:
        st.markdown("")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # Pack SVG
            pack_svg = render_pack_svg(TEAM_NAME, TEAM_COLORS)
            st.markdown(f'<div class="pack-area">{pack_svg}</div>', unsafe_allow_html=True)

            if st.button("⚽  ABRIR PACOTE", use_container_width=True):
                open_pack()
                st.rerun()

        # Show current pack results
        if st.session_state.current_pack:
            st.markdown("---")
            st.markdown(f"""
            <div style="text-align:center; margin:1rem 0;">
                <span style="font-family:'Oswald',sans-serif; font-size:1.5rem; color:var(--gold); 
                      text-transform:uppercase; letter-spacing:3px;">
                    Pacote #{st.session_state.packs_opened}
                </span>
            </div>
            """, unsafe_allow_html=True)

            reveal_html = '<div class="reveal-grid">'
            for i, sid in enumerate(st.session_state.current_pack):
                student = STUDENTS[sid]
                is_new = st.session_state.collection.get(sid, 0) == 1
                badge = '<div class="new-badge">NOVA!</div>' if is_new else '<div class="repeat-badge">REPETIDA</div>'
                delay = i * 0.15
                svg = render_sticker_svg(sid, student, TEAM_NAME, TEAM_COLORS)
                reveal_html += f'''
                <div class="reveal-item" style="animation-delay:{delay}s">
                    {svg}
                    {badge}
                </div>
                '''
            reveal_html += '</div>'
            st.markdown(reveal_html, unsafe_allow_html=True)

    # ------ TAB: ALBUM ------
    with tab_album:
        st.markdown("")

        # Group students by their "group" field
        groups = {}
        for sid, s in STUDENTS.items():
            g = s.get("group", "Sem Grupo")
            if g not in groups:
                groups[g] = []
            groups[g].append((sid, s))

        for group_name, members in groups.items():
            st.markdown(f'<div class="group-header">{group_name}</div>', unsafe_allow_html=True)

            grid_html = '<div class="sticker-grid">'
            for sid, student in members:
                collected_count = st.session_state.collection.get(sid, 0)
                if collected_count > 0:
                    svg = render_sticker_svg(sid, student, TEAM_NAME, TEAM_COLORS)
                    count_label = f'<div style="font-family:Barlow Condensed,sans-serif; color:var(--baby-blue); font-size:0.8rem; margin-top:2px;">x{collected_count}</div>' if collected_count > 1 else ''
                    grid_html += f'<div class="sticker-cell">{svg}{count_label}</div>'
                else:
                    svg = render_sticker_placeholder_svg(sid, student, TEAM_COLORS)
                    grid_html += f'<div class="sticker-cell">{svg}</div>'
            grid_html += '</div>'
            st.markdown(grid_html, unsafe_allow_html=True)


# ============================================================
# ROUTING
# ============================================================
if not st.session_state.logged_in:
    show_login()
else:
    show_app()
