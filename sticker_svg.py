# ============================================================
# STICKER_SVG.PY — Gerador de SVG das figurinhas estilo Panini 2026
# ============================================================
# Design baseado no layout Panini Copa 2026:
# - Fundo baby blue com "26" grande atrás
# - Foto do jogador no centro (ou iniciais como placeholder)
# - Barra azul escura embaixo com nome do jogador
# - Número da figurinha no canto
# - Bandeirinha / emblema do time
# ============================================================

import hashlib


def _color_from_name(name: str) -> str:
    """Generate a consistent color from a name for avatar backgrounds."""
    h = int(hashlib.md5(name.encode()).hexdigest()[:6], 16)
    hue = h % 360
    return f"hsl({hue}, 55%, 45%)"


def _initials(name: str) -> str:
    parts = name.split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    return name[0].upper()


def render_sticker_svg(sid: str, student: dict, team_name: str, colors: dict, width: int = 160) -> str:
    """Render a collected sticker in Panini 2026 style."""
    height = int(width * 1.35)
    name = student["name"]
    nickname = student.get("nickname", "")
    number = student.get("number", "?")
    position = student.get("position", "")
    fun_fact = student.get("fun_fact", "")
    photo_url = student.get("photo_url", "")

    bg_color = colors.get("sticker_bg", "#c9e7f2")
    bar_color = colors.get("sticker_bar", "#1a3a5c")
    text_color = colors.get("sticker_text", "#ffffff")
    number_bg = colors.get("sticker_number_bg", "#d4a843")
    accent = colors.get("accent", "#d4a843")

    initials = _initials(name)
    avatar_color = _color_from_name(name)

    # Split name for display
    name_parts = name.split()
    if len(name_parts) > 2:
        display_name = f"{name_parts[0]} {name_parts[-1]}"
    else:
        display_name = name
    
    # Font sizes proportional to width
    name_font = max(9, int(width * 0.065))
    number_font = max(10, int(width * 0.075))
    position_font = max(7, int(width * 0.05))
    initials_font = max(24, int(width * 0.22))
    big26_font = max(60, int(width * 0.55))
    
    bar_y = height - int(height * 0.22)
    bar_height = int(height * 0.18)
    
    # Photo or initials
    if photo_url:
        avatar_element = f'''
        <clipPath id="avatar-clip-{sid}">
            <circle cx="{width//2}" cy="{int(height*0.42)}" r="{int(width*0.28)}"/>
        </clipPath>
        <image href="{photo_url}" x="{width//2 - int(width*0.28)}" y="{int(height*0.42) - int(width*0.28)}" 
               width="{int(width*0.56)}" height="{int(width*0.56)}" 
               clip-path="url(#avatar-clip-{sid})" preserveAspectRatio="xMidYMid slice"/>
        '''
    else:
        avatar_element = f'''
        <circle cx="{width//2}" cy="{int(height*0.42)}" r="{int(width*0.28)}" fill="{avatar_color}"/>
        <text x="{width//2}" y="{int(height*0.42)+int(initials_font*0.35)}" 
              font-family="Oswald,sans-serif" font-weight="700" font-size="{initials_font}" 
              fill="white" text-anchor="middle" opacity="0.95">{initials}</text>
        '''

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" 
         xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 3px 8px rgba(0,0,0,0.4));">
        <defs>
            <linearGradient id="bg-grad-{sid}" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="{bg_color}"/>
                <stop offset="100%" stop-color="#9ccfde"/>
            </linearGradient>
            <linearGradient id="bar-grad-{sid}" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="{bar_color}"/>
                <stop offset="100%" stop-color="#0f2840"/>
            </linearGradient>
            <linearGradient id="gold-grad-{sid}" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="{accent}"/>
                <stop offset="100%" stop-color="#f0c75e"/>
            </linearGradient>
        </defs>
        
        <!-- Card background -->
        <rect width="{width}" height="{height}" rx="6" fill="url(#bg-grad-{sid})"/>
        
        <!-- Border -->
        <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="5" 
              fill="none" stroke="url(#gold-grad-{sid})" stroke-width="2" opacity="0.6"/>
        
        <!-- Big 26 watermark -->
        <text x="{width//2}" y="{int(height*0.55)}" 
              font-family="Oswald,sans-serif" font-weight="700" font-size="{big26_font}" 
              fill="#1a3a5c" opacity="0.07" text-anchor="middle">26</text>
        
        <!-- Number badge -->
        <rect x="6" y="6" width="{int(width*0.2)}" height="{int(width*0.14)}" rx="3" 
              fill="url(#gold-grad-{sid})"/>
        <text x="{6+int(width*0.1)}" y="{6+int(width*0.11)}" 
              font-family="Oswald,sans-serif" font-weight="700" font-size="{number_font}" 
              fill="{bar_color}" text-anchor="middle">{number}</text>
        
        <!-- Team name tiny -->
        <text x="{width-8}" y="{16}" 
              font-family="Barlow Condensed,sans-serif" font-weight="600" font-size="{max(6,int(width*0.04))}" 
              fill="{bar_color}" text-anchor="end" opacity="0.5" 
              letter-spacing="1">{team_name.upper()}</text>
        
        <!-- Avatar -->
        {avatar_element}
        
        <!-- Position label -->
        <text x="{width//2}" y="{int(height*0.72)}" 
              font-family="Barlow Condensed,sans-serif" font-weight="600" font-size="{position_font}" 
              fill="{bar_color}" text-anchor="middle" opacity="0.6" 
              letter-spacing="1" text-transform="uppercase">{position.upper()}</text>
        
        <!-- Name bar -->
        <rect x="0" y="{bar_y}" width="{width}" height="{bar_height}" 
              rx="0" fill="url(#bar-grad-{sid})"/>
        
        <!-- Gold accent line on bar -->
        <rect x="0" y="{bar_y}" width="{width}" height="2" fill="url(#gold-grad-{sid})" opacity="0.7"/>
        
        <!-- Player name -->
        <text x="{width//2}" y="{bar_y + int(bar_height*0.5)}" 
              font-family="Oswald,sans-serif" font-weight="600" font-size="{name_font}" 
              fill="{text_color}" text-anchor="middle" letter-spacing="1">{display_name.upper()}</text>
        
        <!-- Nickname -->
        <text x="{width//2}" y="{bar_y + int(bar_height*0.82)}" 
              font-family="Barlow Condensed,sans-serif" font-weight="400" font-size="{max(7,int(name_font*0.75))}" 
              fill="{accent}" text-anchor="middle" letter-spacing="1">"{nickname}"</text>
        
        <!-- Bottom gold line -->
        <rect x="0" y="{height-3}" width="{width}" height="3" rx="0" fill="url(#gold-grad-{sid})" opacity="0.5"/>
    </svg>'''

    return svg


def render_sticker_placeholder_svg(sid: str, student: dict, colors: dict, width: int = 160) -> str:
    """Render a not-yet-collected sticker placeholder (grayscale, covered)."""
    height = int(width * 1.35)
    number = student.get("number", "?")
    name = student["name"]
    
    name_parts = name.split()
    if len(name_parts) > 2:
        display_name = f"{name_parts[0]} {name_parts[-1]}"
    else:
        display_name = name
    
    number_font = max(10, int(width * 0.075))
    name_font = max(9, int(width * 0.065))
    question_font = max(30, int(width * 0.25))
    
    bar_y = height - int(height * 0.22)
    bar_height = int(height * 0.18)

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" 
         xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 2px 5px rgba(0,0,0,0.3)); opacity:0.5;">
        <defs>
            <linearGradient id="ph-bg-{sid}" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="#3a3a3a"/>
                <stop offset="100%" stop-color="#2a2a2a"/>
            </linearGradient>
            <pattern id="lines-{sid}" patternUnits="userSpaceOnUse" width="8" height="8">
                <line x1="0" y1="8" x2="8" y2="0" stroke="#4a4a4a" stroke-width="0.5" opacity="0.3"/>
            </pattern>
        </defs>
        
        <!-- Card background -->
        <rect width="{width}" height="{height}" rx="6" fill="url(#ph-bg-{sid})"/>
        <rect width="{width}" height="{height}" rx="6" fill="url(#lines-{sid})"/>
        
        <!-- Border -->
        <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="5" 
              fill="none" stroke="#555" stroke-width="1.5" opacity="0.4"/>
        
        <!-- Number badge -->
        <rect x="6" y="6" width="{int(width*0.2)}" height="{int(width*0.14)}" rx="3" 
              fill="#555"/>
        <text x="{6+int(width*0.1)}" y="{6+int(width*0.11)}" 
              font-family="Oswald,sans-serif" font-weight="700" font-size="{number_font}" 
              fill="#888" text-anchor="middle">{number}</text>
        
        <!-- Question mark -->
        <text x="{width//2}" y="{int(height*0.48)}" 
              font-family="Oswald,sans-serif" font-weight="700" font-size="{question_font}" 
              fill="#555" text-anchor="middle">?</text>
        
        <!-- Name bar -->
        <rect x="0" y="{bar_y}" width="{width}" height="{bar_height}" fill="#222"/>
        <rect x="0" y="{bar_y}" width="{width}" height="1.5" fill="#555" opacity="0.4"/>
        
        <!-- Redacted name -->
        <text x="{width//2}" y="{bar_y + int(bar_height*0.55)}" 
              font-family="Oswald,sans-serif" font-weight="600" font-size="{name_font}" 
              fill="#555" text-anchor="middle" letter-spacing="1">? ? ?</text>
    </svg>'''

    return svg


def render_pack_svg(team_name: str, colors: dict, width: int = 220) -> str:
    """Render a sticker pack SVG (Panini-style foil pack)."""
    height = int(width * 1.4)
    accent = colors.get("accent", "#d4a843")
    bar_color = colors.get("sticker_bar", "#1a3a5c")
    secondary = colors.get("secondary", "#a8d8ea")

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" 
         xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 6px 20px rgba(0,0,0,0.5));">
        <defs>
            <linearGradient id="pack-bg" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="#1a3a5c"/>
                <stop offset="30%" stop-color="#0f2840"/>
                <stop offset="70%" stop-color="#1a3a5c"/>
                <stop offset="100%" stop-color="#0f2840"/>
            </linearGradient>
            <linearGradient id="pack-gold" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#b8942e"/>
                <stop offset="30%" stop-color="#f0c75e"/>
                <stop offset="50%" stop-color="#d4a843"/>
                <stop offset="70%" stop-color="#f0c75e"/>
                <stop offset="100%" stop-color="#b8942e"/>
            </linearGradient>
            <linearGradient id="pack-shine" x1="0" y1="0" x2="0.3" y2="1">
                <stop offset="0%" stop-color="white" stop-opacity="0.15"/>
                <stop offset="50%" stop-color="white" stop-opacity="0"/>
                <stop offset="100%" stop-color="white" stop-opacity="0.05"/>
            </linearGradient>
            <filter id="pack-glow">
                <feGaussianBlur stdDeviation="3" result="blur"/>
                <feComposite in="SourceGraphic" in2="blur" operator="over"/>
            </filter>
        </defs>
        
        <!-- Pack body -->
        <rect width="{width}" height="{height}" rx="8" fill="url(#pack-bg)"/>
        
        <!-- Diagonal stripes -->
        <g opacity="0.06">
            <line x1="0" y1="30" x2="{width}" y2="{height-30}" stroke="{secondary}" stroke-width="25"/>
            <line x1="30" y1="0" x2="{width+30}" y2="{height}" stroke="{secondary}" stroke-width="15"/>
            <line x1="-30" y1="20" x2="{width-30}" y2="{height+20}" stroke="{secondary}" stroke-width="15"/>
        </g>
        
        <!-- Shine overlay -->
        <rect width="{width}" height="{height}" rx="8" fill="url(#pack-shine)"/>
        
        <!-- Gold border -->
        <rect x="4" y="4" width="{width-8}" height="{height-8}" rx="6" 
              fill="none" stroke="url(#pack-gold)" stroke-width="2.5"/>
        
        <!-- Inner border -->
        <rect x="10" y="10" width="{width-20}" height="{height-20}" rx="4" 
              fill="none" stroke="url(#pack-gold)" stroke-width="0.5" opacity="0.4"/>
        
        <!-- Big 26 watermark -->
        <text x="{width//2}" y="{int(height*0.52)}" 
              font-family="Oswald,sans-serif" font-weight="700" font-size="{int(width*0.65)}" 
              fill="{secondary}" opacity="0.08" text-anchor="middle">26</text>
        
        <!-- Team emblem area -->
        <circle cx="{width//2}" cy="{int(height*0.32)}" r="{int(width*0.18)}" 
                fill="none" stroke="url(#pack-gold)" stroke-width="1.5" opacity="0.4"/>
        <text x="{width//2}" y="{int(height*0.35)}" 
              font-family="Oswald,sans-serif" font-weight="700" font-size="{int(width*0.14)}" 
              fill="url(#pack-gold)" text-anchor="middle">⚽</text>
        
        <!-- Team name -->
        <text x="{width//2}" y="{int(height*0.55)}" 
              font-family="Oswald,sans-serif" font-weight="700" font-size="{int(width*0.1)}" 
              fill="url(#pack-gold)" text-anchor="middle" letter-spacing="3">{team_name.upper()}</text>
        
        <!-- Subtitle -->
        <text x="{width//2}" y="{int(height*0.62)}" 
              font-family="Barlow Condensed,sans-serif" font-weight="500" font-size="{int(width*0.05)}" 
              fill="{secondary}" text-anchor="middle" letter-spacing="4" opacity="0.7">COLEÇÃO OFICIAL DE FIGURINHAS</text>
        
        <!-- Sticker count badge -->
        <rect x="{width//2 - int(width*0.25)}" y="{int(height*0.72)}" 
              width="{int(width*0.5)}" height="{int(width*0.12)}" rx="3" 
              fill="url(#pack-gold)" opacity="0.9"/>
        <text x="{width//2}" y="{int(height*0.72) + int(width*0.09)}" 
              font-family="Oswald,sans-serif" font-weight="700" font-size="{int(width*0.055)}" 
              fill="{bar_color}" text-anchor="middle" letter-spacing="2">7 FIGURINHAS</text>
        
        <!-- Bottom decorative line -->
        <line x1="20" y1="{height-25}" x2="{width-20}" y2="{height-25}" 
              stroke="url(#pack-gold)" stroke-width="0.5" opacity="0.3"/>
        <text x="{width//2}" y="{height-12}" 
              font-family="Barlow Condensed,sans-serif" font-size="{int(width*0.035)}" 
              fill="{secondary}" text-anchor="middle" opacity="0.4" letter-spacing="2">EDIÇÃO ESPECIAL</text>
        
        <!-- Tear line (zigzag at top) -->
        <polyline points="0,12 8,8 16,12 24,8 32,12 40,8 48,12 56,8 64,12 72,8 80,12 88,8 96,12 104,8 112,12 120,8 128,12 136,8 144,12 152,8 160,12 168,8 176,12 184,8 192,12 200,8 208,12 216,8 {width},12" 
                  fill="none" stroke="url(#pack-gold)" stroke-width="0.8" opacity="0.3"/>
    </svg>'''

    return svg
