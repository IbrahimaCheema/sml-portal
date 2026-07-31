import os

# Complete sticky navigation and sidebar styling for desktop & mobile
css_complete_sticky = """
/* ==========================================================================
   COMPLETE STICKY NAVIGATION & SIDEBAR (ALL PAGES)
   ========================================================================== */

/* Enable sticky positioning globally */
html, body {
    overflow-x: clip !important;
}

/* Sticky Main Navigation Header across ALL pages */
.navbar {
    position: sticky !important;
    position: -webkit-sticky !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    z-index: 9999 !important;
    background-color: #ffffff !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
    border-bottom: 1px solid var(--border-color, #e2e8f0) !important;
}

/* Ensure sticky header remains solid dark background in dark mode */
[data-theme="dark"] .navbar {
    background-color: #0b1e36 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
}

/* Desktop Sticky Sidebar for Shareholders Directory */
@media (min-width: 993px) {
    .sh-main-grid {
        display: grid !important;
        grid-template-columns: 280px 1fr !important;
        gap: 2.5rem !important;
        align-items: start !important;
    }

    .sh-sidebar {
        position: sticky !important;
        position: -webkit-sticky !important;
        top: 90px !important; /* Pins below the 72px navbar */
        z-index: 90 !important;
        max-height: calc(100vh - 110px) !important;
        overflow-y: auto !important;
    }
}

/* Mobile Sticky Bar for Shareholders Directory (Below 992px) */
@media (max-width: 992px) {
    .sh-main-grid {
        display: flex !important;
        flex-direction: column !important;
        gap: 1.5rem !important;
    }

    .sh-sidebar {
        position: relative !important;
        top: 0 !important;
        width: 100% !important;
        z-index: 80 !important;
    }

    .sh-side-nav {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 0.5rem !important;
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
        
        # Ensure overflow-x is clip not hidden
        c = c.replace('overflow-x: hidden !important;', 'overflow-x: clip !important;')

        if 'COMPLETE STICKY NAVIGATION & SIDEBAR' not in c:
            c += '\n' + css_complete_sticky
            
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated sticky navbar & sidebar in {p}")

print("Sticky fix applied for all pages!")
