import os

# 1. Update HTML files with exact span structure
html_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

exact_headline_html = """<h1 class="hero-title">
                <span class="text-navy">Pioneering</span> <span class="text-sugar-green">Sugar, Biofuels &amp;</span><br>
                <span class="text-olive-green">Renewable</span> <span class="text-golden-amber">Energy</span> <span class="text-navy">in Pakistan</span>
            </h1>"""

for h in html_files:
    if os.path.exists(h):
        with open(h, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace hero title with exact pixel-matching spans
        content = content.replace(
            '<h1 class="hero-title">\n                Pioneering <span class="text-sugar-green">Sugar, Biofuels &amp;</span><br>\n                <span class="text-sugar-green">Renewable</span> <span class="text-amber">Energy</span> in Pakistan\n            </h1>',
            exact_headline_html
        )
        content = content.replace(
            '<h1 class="hero-title">\n                Pioneering <span class="text-sugar-green">Sugar, Biofuels &amp;</span><br>\n                <span class="text-amber">Renewable Energy</span> in Pakistan\n            </h1>',
            exact_headline_html
        )
        
        with open(h, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated exact headline HTML in {h}")

# 2. Add exact CSS color definitions matching the image crop
exact_css = """
/* ==========================================================================
   EXACT HEADLINE COLOR GRADIENT & SPAN STYLES MATCHING SAMPLE CROP
   ========================================================================== */

.text-navy {
    color: #0f172a !important;
    font-weight: 800 !important;
}

[data-theme="dark"] .text-navy {
    color: #f8fafc !important;
}

.text-sugar-green {
    color: #046a38 !important;
    font-weight: 800 !important;
}

.text-olive-green {
    background: linear-gradient(90deg, #046a38 0%, #467425 35%, #6a7a1b 70%, #7b8116 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    display: inline-block !important;
    font-weight: 800 !important;
}

.text-golden-amber {
    color: #eab308 !important;
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
        
        if 'EXACT HEADLINE COLOR GRADIENT' not in c:
            c += '\n' + exact_css
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Applied exact headline CSS to {p}")

print("Exact headline update complete!")
