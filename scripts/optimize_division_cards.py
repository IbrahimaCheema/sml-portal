import os
import re

# 1. Update HTML in index.html to include real image tags for Sugar and Biofuel cards
html_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

new_divisions_grid = """<div class="divisions-grid">
                <div class="division-card">
                    <div class="card-image">
                        <img src="/images/sugar-card.jpg" alt="Sugar Manufacturing Division" class="division-card-img">
                        <div class="card-tag">Sugar Division</div>
                    </div>
                    <div class="card-body">
                        <div class="division-icon">
                            <img src="/images/sugar-icon.svg" alt="Sugar Icon" onerror="this.onerror=null; this.parentNode.innerHTML='🌾';" style="width:28px; height:28px; object-fit:contain;">
                        </div>
                        <h3>Sugar Manufacturing</h3>
                        <p>High-grade refined food &amp; pharmaceutical sugar serving top multinational beverage brands across Pakistan.</p>
                        <a href="divisions.html#sugar" class="btn btn-outline" style="margin-top: 1rem;">View Sugar Specs &rarr;</a>
                    </div>
                </div>
                <div class="division-card">
                    <div class="card-image">
                        <img src="/images/biofuel-card.jpg" alt="Biofuels &amp; Power Division" class="division-card-img">
                        <div class="card-tag">Green Energy</div>
                    </div>
                    <div class="card-body">
                        <div class="division-icon">
                            <img src="/images/biofuel-icon.svg" alt="Biofuel Icon" onerror="this.onerror=null; this.parentNode.innerHTML='⚡';" style="width:28px; height:28px; object-fit:contain;">
                        </div>
                        <h3>Biofuels &amp; Power</h3>
                        <p>Anhydrous ethanol distillery producing eco-friendly fuel-grade bio-ethanol and renewable export power.</p>
                        <a href="divisions.html#biofuel" class="btn btn-outline" style="margin-top: 1rem;">View Biofuel Specs &rarr;</a>
                    </div>
                </div>
            </div>"""

for h in html_files:
    if os.path.exists(h):
        with open(h, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace divisions-grid block
        content = re.sub(
            r'<div class="divisions-grid">[\s\S]*?</div>\s*</div>\s*</div>\s*</section>',
            new_divisions_grid + '\n        </div>\n    </section>',
            content
        )
        
        with open(h, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated divisions grid HTML in {h}")

# 2. Update CSS for Division Cards to display images and floating icon overlay
cards_css = """
/* ==========================================================================
   OPTIMIZED DIVISION CARDS (REAL IMAGES & FLOATING ICON OVERLAY)
   ========================================================================== */
.divisions-grid {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 2.25rem !important;
    max-width: 960px !important;
    margin: 2.5rem auto 0 !important;
}

.division-card {
    background-color: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 18px !important;
    overflow: hidden !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06) !important;
    transition: transform 300ms ease, box-shadow 300ms ease, border-color 300ms ease !important;
}

[data-theme="dark"] .division-card {
    background-color: #0f2438 !important;
    border-color: rgba(255, 255, 255, 0.1) !important;
}

.division-card:hover {
    transform: translateY(-6px) !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12) !important;
    border-color: #005a2b !important;
}

.card-image {
    position: relative !important;
    height: 200px !important;
    overflow: hidden !important;
    background-color: #f1f5f9 !important;
}

.division-card-img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    transition: transform 400ms ease !important;
}

.division-card:hover .division-card-img {
    transform: scale(1.05) !important;
}

.card-tag {
    position: absolute !important;
    top: 1rem !important;
    right: 1rem !important;
    background: rgba(15, 23, 42, 0.5) !important;
    backdrop-filter: blur(8px) !important;
    -webkit-backdrop-filter: blur(8px) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    padding: 0.35rem 1rem !important;
    border-radius: 9999px !important;
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    z-index: 2 !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
}

.card-body {
    padding: 0 2rem 2.25rem !important;
    position: relative !important;
}

.division-icon {
    position: relative !important;
    z-index: 10 !important;
    width: 64px !important;
    height: 64px !important;
    margin-top: -32px !important; /* Pulls up half way over image edge */
    margin-bottom: 1.25rem !important;
    background-color: #ffffff !important;
    border: 3px solid #ffffff !important;
    border-radius: 16px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12) !important;
    font-size: 1.8rem !important;
}

[data-theme="dark"] .division-icon {
    background-color: #0b1a28 !important;
    border-color: #0b1a28 !important;
}

.card-body h3 {
    font-family: var(--font-heading, 'Outfit', sans-serif) !important;
    font-size: 1.6rem !important;
    font-weight: 800 !important;
    color: #0f172a !important;
    margin-bottom: 0.75rem !important;
}

[data-theme="dark"] .card-body h3 {
    color: #f8fafc !important;
}

.card-body p {
    font-size: 0.98rem !important;
    color: #64748b !important;
    line-height: 1.6 !important;
    margin-bottom: 1.5rem !important;
}

[data-theme="dark"] .card-body p {
    color: #94a3b8 !important;
}

@media (max-width: 768px) {
    .divisions-grid {
        grid-template-columns: 1fr !important;
    }
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
        
        if 'OPTIMIZED DIVISION CARDS (REAL IMAGES & FLOATING ICON OVERLAY)' not in c:
            c += '\n' + cards_css
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Applied division cards CSS to {p}")

print("Division cards optimization complete!")
