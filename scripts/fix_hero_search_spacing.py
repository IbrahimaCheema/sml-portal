import glob

hero_content_new = """            <div class="hero-buttons">
                <a href="divisions.html" class="btn btn-primary">
                    Explore Divisions 
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
                <a href="investors.html" class="btn btn-secondary">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                    Investor Center & Financials
                </a>
            </div>

            <!-- Site-Wide Search Bar (Home Page Only) -->
            <div class="hero-search-wrapper">
                <div class="search-input-box">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2.5" style="margin-right: 0.75rem; flex-shrink: 0;"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                    <input type="text" id="siteSearchInput" placeholder="Search across Shakarganj site (e.g. Sugar, Annual Report, Biofuel, Directors, SECP)..." aria-label="Search across site">
                </div>
                <div id="siteSearchResults" class="site-search-dropdown"></div>
            </div>"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\index.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<div class="hero-search-wrapper">' in content:
        # Swap order: buttons first, search second
        start_idx = content.find('<!-- Site-Wide Search Bar')
        end_idx = content.find('</div>', content.find('<div class="hero-buttons">')) + 6
        if start_idx != -1 and end_idx != -1:
            new_content = content[:start_idx] + hero_content_new + content[end_idx:]
            with open(t, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Successfully fixed Hero search bar and buttons spacing order!")
