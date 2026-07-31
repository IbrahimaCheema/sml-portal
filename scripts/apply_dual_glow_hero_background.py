import os

# Dual origin green glow background for hero section (Top-Right & Bottom-Left)
hero_dual_glow_css = """
/* ==========================================================================
   DUAL ORIGIN HERO MINT GREEN GLOW (TOP-RIGHT & BOTTOM-LEFT)
   ========================================================================== */

.hero {
    position: relative !important;
    padding: 4.5rem 0 4rem !important;
    background-color: #ffffff !important;
    background-image: 
        radial-gradient(circle at 92% 8%, #78cca4 0%, rgba(174, 227, 203, 0.55) 35%, transparent 65%),
        radial-gradient(circle at 8% 92%, #86d6af 0%, rgba(174, 227, 203, 0.50) 35%, transparent 65%),
        linear-gradient(135deg, #ffffff 0%, #f2faf5 50%, #ffffff 100%) !important;
    overflow: hidden !important;
}

[data-theme="dark"] .hero {
    background-color: #0b1a28 !important;
    background-image: 
        radial-gradient(circle at 92% 8%, #005a2b 0%, rgba(0, 90, 43, 0.45) 40%, transparent 70%),
        radial-gradient(circle at 8% 92%, #044723 0%, rgba(0, 90, 43, 0.40) 40%, transparent 70%),
        linear-gradient(135deg, #0b1a28 0%, #0d281e 50%, #0b1a28 100%) !important;
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
        
        if 'DUAL ORIGIN HERO MINT GREEN GLOW' not in c:
            c += '\n' + hero_dual_glow_css
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Applied dual origin hero glow CSS to {p}")

print("Dual origin hero background update complete!")
