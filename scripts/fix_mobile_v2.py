import glob
import re

css_fix = """
/* ==========================================================================
   ULTIMATE MOBILE RESPONSIVE FIX V2
   ========================================================================== */
@media (max-width: 768px) {
    /* Hard enforce viewport bounds */
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        max-width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .container {
        width: 100vw !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
        padding-left: 15px !important;
        padding-right: 15px !important;
        box-sizing: border-box !important;
    }

    /* Wrap all directory pills so they are fully visible, not hidden in a scroll */
    .sh-side-nav {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        overflow: visible !important;
        white-space: normal !important;
        gap: 0.5rem !important;
    }

    .side-nav-item {
        flex: 1 1 calc(50% - 0.5rem) !important;
        text-align: center !important;
        white-space: normal !important;
        padding: 0.5rem !important;
        font-size: 0.75rem !important;
        min-width: 120px !important;
    }

    /* Ensure text wrapping on literally everything that might cause overflow */
    p, a, span, h1, h2, h3, h4, h5, h6, div {
        word-break: break-word !important;
        overflow-wrap: break-word !important;
    }

    /* Force images to stay inside bounds */
    img, svg {
        max-width: 100% !important;
        height: auto !important;
    }

    /* Any flex row that might not wrap needs wrapping */
    .secp-portal-box, .secp-portal-box > div, .top-bar-content, .top-info {
        flex-wrap: wrap !important;
    }
}
"""

css_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for c in css_files:
    try:
        with open(c, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'ULTIMATE MOBILE RESPONSIVE FIX V2' not in content:
            content += '\n' + css_fix
            with open(c, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {c}")
    except FileNotFoundError:
        pass

html_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\shareholders-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\shareholders-information.html'
]

for h in html_files:
    try:
        with open(h, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Also clean up any lingering 'white-space: nowrap' inline styles just in case
        content = re.sub(r'white-space:\s*nowrap;?', '', content)
        
        with open(h, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {h}")
    except FileNotFoundError:
        pass

print("Done applying V2 fixes!")
