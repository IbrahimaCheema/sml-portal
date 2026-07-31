import os
import re

# 1. Remove <div class="card-tag">...</div> from all index.html files
html_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

for h in html_files:
    if os.path.exists(h):
        with open(h, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove <div class="card-tag">...</div> tags
        content = re.sub(r'<div class="card-tag">[\s\S]*?</div>', '', content)
        
        with open(h, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed card-tag labels from HTML in {h}")

# 2. Hide .card-tag in all CSS files as fallback
css_paths = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

css_hide = "\n.card-tag { display: none !important; }\n"

for p in css_paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        if '.card-tag { display: none !important; }' not in c:
            c += css_hide
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Added card-tag hide CSS to {p}")

print("Card tags removal complete!")
