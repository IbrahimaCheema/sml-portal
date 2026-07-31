import os

# 1. Update HTML to wrap "Renewable Energy" in a single continuous gradient span
html_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

continuous_headline_html = """<h1 class="hero-title">
                <span class="text-navy">Pioneering</span> <span class="text-sugar-green">Sugar, Biofuels &amp;</span><br>
                <span class="text-renewable-energy-gradient">Renewable Energy</span> <span class="text-navy">in Pakistan</span>
            </h1>"""

for h in html_files:
    if os.path.exists(h):
        with open(h, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace hero title with continuous gradient wrapper
        content = content.replace(
            '<h1 class="hero-title">\n                <span class="text-navy">Pioneering</span> <span class="text-sugar-green">Sugar, Biofuels &amp;</span><br>\n                <span class="text-olive-green">Renewable</span> <span class="text-golden-amber">Energy</span> <span class="text-navy">in Pakistan</span>\n            </h1>',
            continuous_headline_html
        )
        content = content.replace(
            '<h1 class="hero-title">\n                Pioneering <span class="text-sugar-green">Sugar, Biofuels &amp;</span><br>\n                <span class="text-sugar-green">Renewable</span> <span class="text-amber">Energy</span> in Pakistan\n            </h1>',
            continuous_headline_html
        )
        
        with open(h, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated continuous gradient headline HTML in {h}")

# 2. Add continuous multi-stop gradient CSS for "Renewable Energy"
bleed_css = """
/* ==========================================================================
   CONTINUOUS COLOR BLEED GRADIENT FOR RENEWABLE ENERGY
   ========================================================================== */

.text-renewable-energy-gradient {
    background: linear-gradient(90deg, #046a38 0%, #3e7527 28%, #6a7c1b 55%, #9e9514 80%, #eab308 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    display: inline-block !important;
    font-weight: 800 !important;
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
        
        if 'CONTINUOUS COLOR BLEED GRADIENT FOR RENEWABLE ENERGY' not in c:
            c += '\n' + bleed_css
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Applied continuous bleed CSS to {p}")

print("Continuous headline bleed update complete!")
