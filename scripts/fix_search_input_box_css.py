import glob

search_css_full = """

/* --- Site-Wide Search Component (Home Page Only) --- */
.hero-search-wrapper {
    max-width: 680px;
    margin: 0 auto 3.5rem;
    position: relative;
    z-index: 150;
}

.search-input-box {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: flex-start !important;
    background: var(--bg-surface) !important;
    border: 2px solid var(--primary-light) !important;
    border-radius: var(--radius-full) !important;
    padding: 0.6rem 1.25rem 0.6rem 1.4rem !important;
    box-shadow: 0 10px 25px rgba(0, 90, 43, 0.15) !important;
    transition: all 250ms ease !important;
    box-sizing: border-box !important;
    width: 100% !important;
}

.search-input-box:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 14px 35px rgba(0, 90, 43, 0.25) !important;
}

.search-input-box svg {
    margin-right: 0.75rem !important;
    flex-shrink: 0 !important;
    display: block !important;
}

.search-input-box input {
    flex: 1 !important;
    width: 100% !important;
    border: none !important;
    outline: none !important;
    background: transparent !important;
    font-size: 0.95rem !important;
    color: var(--text-main) !important;
    font-weight: 500 !important;
    padding: 0.25rem 0 !important;
    margin: 0 !important;
}

.site-search-dropdown {
    display: none;
    position: absolute;
    top: calc(100% + 10px);
    left: 0;
    right: 0;
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.22);
    z-index: 250;
    max-height: 420px;
    overflow-y: auto;
    text-align: left;
    padding: 0.75rem;
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
    if '/* --- Site-Wide Search Component' in content:
        parts = content.split('/* --- Site-Wide Search Component')
        new_content = parts[0] + search_css_full
    else:
        new_content = content + search_css_full
    with open(t, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Successfully restored full .search-input-box CSS rules across all style files!")
