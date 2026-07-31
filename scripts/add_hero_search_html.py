search_html = """
            <!-- Site-Wide Search Bar (Home Page Only) -->
            <div class="hero-search-wrapper">
                <div class="search-input-box">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2.5" style="margin-right: 0.75rem; flex-shrink: 0;"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                    <input type="text" id="siteSearchInput" placeholder="Search across Shakarganj site (e.g. Sugar, Annual Report, Biofuel, Directors, SECP)..." aria-label="Search across site">
                </div>
                <div id="siteSearchResults" class="site-search-dropdown"></div>
            </div>
"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\index.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'id="siteSearchInput"' not in content and '<div class="hero-buttons">' in content:
        new_content = content.replace('<div class="hero-buttons">', search_html + '\n            <div class="hero-buttons">')
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Inserted Site-Wide Search Bar into Hero section across all index files!")
