import os

html_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

old_title_1 = """<h1 class="hero-title">
                Pioneering <span class="text-sugar-green">Sugar, Biofuels &amp;</span><br>
                <span class="text-amber">Renewable Energy</span> in Pakistan
            </h1>"""

new_title_exact = """<h1 class="hero-title">
                Pioneering <span class="text-sugar-green">Sugar, Biofuels &amp;</span><br>
                <span class="text-sugar-green">Renewable</span> <span class="text-amber">Energy</span> in Pakistan
            </h1>"""

for h in html_files:
    if os.path.exists(h):
        with open(h, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace headline to split Renewable (Green) and Energy (Golden Amber)
        if old_title_1 in content:
            content = content.replace(old_title_1, new_title_exact)
        else:
            # Fallback regex/string replacement
            content = content.replace(
                '<span class="text-amber">Renewable Energy</span>',
                '<span class="text-sugar-green">Renewable</span> <span class="text-amber">Energy</span>'
            )
            content = content.replace(
                '<span class="text-amber">Renewable</span>',
                '<span class="text-sugar-green">Renewable</span>'
            )
        
        with open(h, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated Renewable Energy color split in {h}")

print("Renewable Energy color fix complete!")
