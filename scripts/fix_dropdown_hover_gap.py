import os

css_fix = """
/* ==========================================================================
   DESKTOP DROPDOWN HOVER GAP & INVISIBLE BRIDGE FIX
   ========================================================================== */
@media (min-width: 993px) {
    .nav-item.dropdown {
        position: relative !important;
        padding-bottom: 10px !important;
        margin-bottom: -10px !important;
    }

    .dropdown-menu {
        top: 100% !important;
        left: 0 !important;
        margin-top: 0 !important;
        transform: translateY(0) !important;
    }

    /* Invisible hover bridge: covers any space between link and dropdown */
    .dropdown-menu::before {
        content: '' !important;
        position: absolute !important;
        top: -16px !important;
        left: 0 !important;
        right: 0 !important;
        height: 16px !important;
        background: transparent !important;
        display: block !important;
        z-index: 99999 !important;
    }

    /* Smooth display with no flickering */
    .nav-item.dropdown:hover .dropdown-menu,
    .nav-item.dropdown:focus-within .dropdown-menu {
        display: block !important;
        opacity: 1 !important;
        visibility: visible !important;
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
        if 'DESKTOP DROPDOWN HOVER GAP' not in c:
            c += '\n' + css_fix
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Applied hover bridge fix to {p}")

print("Hover gap fix complete!")
