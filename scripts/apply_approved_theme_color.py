import os

# 1. Update index.html HTML markup to match sample image headline & layout
html_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

hero_headline_html = """<h1 class="hero-title">
                Pioneering <span class="text-sugar-green">Sugar, Biofuels &amp;</span><br>
                <span class="text-amber">Renewable Energy</span> in Pakistan
            </h1>"""

for h in html_files:
    if os.path.exists(h):
        with open(h, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace hero title span to separate green & amber colors matching sample
        content = content.replace(
            '<h1 class="hero-title">\n                Pioneering <span class="gradient-text">Sugar, Biofuels & Renewable Energy</span> in Pakistan\n            </h1>',
            hero_headline_html
        )
        content = content.replace(
            '<h1 class="hero-title">Pioneering <span class="gradient-text">Sugar, Biofuels & Renewable Energy</span> in Pakistan</h1>',
            hero_headline_html
        )
        content = content.replace(
            '<h1 class="hero-title">\n                Pioneering <span class="gradient-text">Sugar, Biofuels &amp; Renewable Energy</span> in Pakistan\n            </h1>',
            hero_headline_html
        )
        
        with open(h, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated index HTML hero title in {h}")

# 2. Update CSS colors & gradients matching the approved theme sample image
approved_theme_css = """
/* ==========================================================================
   APPROVED THEME COLOR SAMPLE SPECIFICATIONS
   ========================================================================== */

/* Top Info Bar */
.top-bar {
    background-color: #08131f !important;
    color: #94a3b8 !important;
    font-size: 0.825rem !important;
    padding: 0.5rem 0 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
}

/* PSX Stock Bar */
.stock-bar {
    background: linear-gradient(90deg, #004722, #005a2b, #004722) !important;
    color: #ffffff !important;
    padding: 0.55rem 0 !important;
    font-size: 0.875rem !important;
    font-weight: 600 !important;
}

.stock-badge {
    background: #003318 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    color: #ffffff !important;
    padding: 0.3rem 0.85rem !important;
    border-radius: 9999px !important;
}

.pulse-dot {
    background-color: #10b981 !important;
}

/* Navbar */
.navbar {
    background-color: #ffffff !important;
    border-bottom: 1px solid #e2e8f0 !important;
}

/* Hero Section Mint Gradient Background */
.hero {
    position: relative !important;
    padding: 4.5rem 0 4rem !important;
    background: linear-gradient(115deg, #ffffff 35%, #aee3cb 70%, #68c79c 100%) !important;
    overflow: hidden !important;
}

[data-theme="dark"] .hero {
    background: linear-gradient(115deg, #0b1a28 40%, #0d382b 75%, #05402b 100%) !important;
}

/* Hero Badge Pill */
.hero-badge {
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
    padding: 0.45rem 1.25rem !important;
    background-color: #ffffff !important;
    border: 1px solid #c3e6d3 !important;
    border-radius: 9999px !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    color: #005a2b !important;
    margin-bottom: 1.5rem !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
}

/* Hero Title Typography & Sample Colors */
.hero-title {
    font-family: var(--font-heading, 'Outfit', sans-serif) !important;
    font-size: 2.75rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
    color: #0f172a !important;
    line-height: 1.25 !important;
    margin-bottom: 1.25rem !important;
}

[data-theme="dark"] .hero-title {
    color: #f8fafc !important;
}

.text-sugar-green {
    color: #005a2b !important;
    font-weight: 800 !important;
}

.text-amber {
    color: #d97706 !important;
    font-weight: 800 !important;
}

/* Hero Subtitle Description */
.hero-desc {
    font-size: 1.08rem !important;
    color: #475569 !important;
    max-width: 720px !important;
    margin: 0 auto 2.25rem !important;
    line-height: 1.6 !important;
    font-weight: 500 !important;
}

[data-theme="dark"] .hero-desc {
    color: #cbd5e1 !important;
}

/* Hero Buttons */
.hero-buttons {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 1.25rem !important;
    margin-bottom: 2.25rem !important;
}

.btn-primary {
    background: #004d25 !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    padding: 0.85rem 1.75rem !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 14px rgba(0, 77, 37, 0.3) !important;
    border: none !important;
}

.btn-primary:hover {
    background: #003318 !important;
    box-shadow: 0 6px 20px rgba(0, 77, 37, 0.45) !important;
}

.btn-secondary {
    background: #ffffff !important;
    color: #0f172a !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 12px !important;
    padding: 0.85rem 1.75rem !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) !important;
}

.btn-secondary:hover {
    background: #f8fafc !important;
    border-color: #005a2b !important;
    color: #005a2b !important;
}

/* Hero Search Bar Green Pill */
.hero-search-wrapper {
    max-width: 720px !important;
    margin: 0 auto 3rem !important;
}

.search-input-box {
    display: flex !important;
    align-items: center !important;
    background: #ffffff !important;
    border: 2px solid #005a2b !important;
    border-radius: 9999px !important;
    padding: 0.75rem 1.5rem !important;
    box-shadow: 0 4px 16px rgba(0, 90, 43, 0.12) !important;
}

.search-input-box input {
    width: 100% !important;
    border: none !important;
    outline: none !important;
    background: transparent !important;
    font-size: 0.95rem !important;
    color: #0f172a !important;
    font-weight: 500 !important;
}

.search-input-box input::placeholder {
    color: #64748b !important;
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
        
        if 'APPROVED THEME COLOR SAMPLE SPECIFICATIONS' not in c:
            c += '\n' + approved_theme_css
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Applied approved theme colors to {p}")

print("Approved theme color update complete!")
