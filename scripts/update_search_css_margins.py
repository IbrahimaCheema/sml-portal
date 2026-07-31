import glob, re

css_fix = """
.hero-buttons {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.25rem;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
}

.hero-search-wrapper {
    max-width: 680px;
    margin: 0 auto 3.5rem;
    position: relative;
    z-index: 150;
}
"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '.hero-buttons {' in content:
        content = re.sub(r'\.hero-buttons\s*\{[^}]*\}', '.hero-buttons {\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    gap: 1.25rem;\n    margin-top: 1.5rem;\n    margin-bottom: 2rem;\n}', content)
        content = re.sub(r'\.hero-search-wrapper\s*\{[^}]*\}', '.hero-search-wrapper {\n    max-width: 680px;\n    margin: 0 auto 3.5rem;\n    position: relative;\n    z-index: 150;\n}', content)
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)

print("Successfully updated CSS margins for search bar and hero buttons!")
