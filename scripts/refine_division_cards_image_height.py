import os
import re

card_refinements_css = """
/* ==========================================================================
   REFINED DIVISION CARDS (DARK GREEN TAGS & INCREASED HEIGHT CENTER TOP)
   ========================================================================== */
.card-image {
    position: relative !important;
    height: 240px !important; /* Increased height so image head/jar is never cropped */
    overflow: hidden !important;
    background-color: #0b1a28 !important;
}

.division-card-img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center top !important; /* Aligns from top so head of jar/towers is 100% visible */
    transition: transform 400ms ease !important;
}

.card-tag {
    position: absolute !important;
    top: 1rem !important;
    right: 1rem !important;
    background: #004d25 !important; /* Theme Dark Green */
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    padding: 0.4rem 1.15rem !important;
    border-radius: 9999px !important;
    font-size: 0.825rem !important;
    font-weight: 700 !important;
    z-index: 2 !important;
    box-shadow: 0 3px 10px rgba(0, 77, 37, 0.35) !important;
}
"""

css_paths = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for p in css_paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        
        if 'REFINED DIVISION CARDS (DARK GREEN TAGS & INCREASED HEIGHT CENTER TOP)' not in c:
            c += '\n' + card_refinements_css
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Applied card height & theme tag CSS to {p}")

print("Card refinements complete!")
