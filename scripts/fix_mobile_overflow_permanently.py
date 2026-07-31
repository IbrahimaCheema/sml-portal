import glob

master_responsive_css = """
/* ==========================================================================
   PERMANENT MOBILE OVERFLOW & RESPONSIVE FIX
   ========================================================================== */

/* 1. Reset Global Box Sizing & Overflows */
*, *::before, *::after {
    box-sizing: border-box !important;
}

html, body {
    overflow-x: hidden !important;
    width: 100% !important;
    max-width: 100% !important;
    position: relative !important;
}

/* 2. Responsive Container Padding */
@media (max-width: 768px) {
    .container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    /* Top Bar Mobile Stacking */
    .top-bar-content {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 0.5rem !important;
    }
    .top-info {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 0.2rem !important;
    }
    .top-info .divider {
        display: none !important;
    }
    .top-info span {
        font-size: 0.725rem !important;
        white-space: normal !important;
        word-break: break-word !important;
        line-height: 1.3 !important;
    }

    /* Stock Ticker Mobile Scroll */
    .stock-bar {
        overflow-x: hidden !important;
        width: 100% !important;
    }
    .stock-flex {
        overflow-x: auto !important;
        max-width: 100% !important;
        white-space: nowrap !important;
        -webkit-overflow-scrolling: touch !important;
    }

    /* Hero Banner Mobile Scaling */
    section[style*="linear-gradient"] h1 {
        font-size: 1.65rem !important;
        line-height: 1.3 !important;
        word-break: break-word !important;
    }
    section[style*="linear-gradient"] p {
        font-size: 0.875rem !important;
    }

    /* Force all grid columns to 1fr on mobile */
    .sh-main-grid,
    div[style*="grid-template-columns"],
    .directors-grid,
    .strategy-grid,
    .grid-2 {
        grid-template-columns: 1fr !important;
        gap: 1.25rem !important;
        width: 100% !important;
    }

    /* Section Cards & Box Bounds */
    .sh-section-card,
    .sh-sidebar-card,
    .info-box-card,
    .policy-card,
    .secp-portal-box,
    .statutory-card,
    .doc-card,
    .election-item-card,
    .statutory-hero-box {
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        overflow: hidden !important;
        padding: 1.15rem 1rem !important;
    }

    /* Typography Wrapping */
    .sh-section-title, .info-box-title, .policy-card-title, .doc-title, h2, h3, h4 {
        word-break: break-word !important;
        overflow-wrap: anywhere !important;
        white-space: normal !important;
        line-height: 1.3 !important;
    }

    /* All Action Buttons Full Width & Flexible Text */
    .btn-primary-pill,
    .btn-primary-action,
    .btn-outline-action,
    .doc-btn,
    .action-btn-primary,
    .action-btn-outline,
    .mini-btn-primary,
    .mini-btn-outline {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
        text-align: center !important;
        box-sizing: border-box !important;
        white-space: normal !important;
        word-break: break-word !important;
        padding: 0.65rem 0.85rem !important;
    }

    /* SECP Inner Flex Wrapper Mobile Stacking */
    .secp-portal-box > div:first-child {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 0.85rem !important;
    }

    .secp-portal-box img {
        max-height: 40px !important;
        width: auto !important;
    }

    /* Sidebar Navigation Horizontal Touch Bar */
    .sh-sidebar {
        position: relative !important;
        top: 0 !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }

    .sh-side-nav {
        display: flex !important;
        flex-direction: row !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        gap: 0.5rem !important;
        padding-bottom: 0.4rem !important;
        -webkit-overflow-scrolling: touch !important;
    }

    .side-nav-item {
        flex-shrink: 0 !important;
    }
}
"""

# Update styles.css files
css_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for c in css_files:
    with open(c, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'PERMANENT MOBILE OVERFLOW & RESPONSIVE FIX' not in content:
        content += '\n' + master_responsive_css
        with open(c, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated master styles.css with permanent mobile overflow fix!")

# Also clean inline grid styles in shareholders-information.html
html_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\shareholders-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\shareholders-information.html'
]

for h in html_files:
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace inline grid styles in sub-divs so CSS can force 1fr on mobile
    content = content.replace('style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;"', 'class="grid-sub-cards"')
    content = content.replace('style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;"', 'class="grid-sub-cards"')
    content = content.replace('style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.75rem;"', 'class="grid-sub-cards"')
    content = content.replace('style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem;"', 'class="grid-sub-cards"')
    content = content.replace('style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin-bottom: 1.75rem;"', 'class="grid-sub-cards"')

    if 'PERMANENT MOBILE OVERFLOW & RESPONSIVE FIX' not in content:
        content = content.replace('</style>', master_responsive_css + '\n    </style>')

    with open(h, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cleaned inline grid styles and updated shareholders-information pages!")
