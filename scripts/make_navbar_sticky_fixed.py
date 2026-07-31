import os
import re

css_sticky_fix = """
/* ==========================================================================
   PERMANENT STICKY NAVBAR FIX
   ========================================================================== */
html {
    overflow-x: clip !important;
}

body {
    overflow-x: clip !important;
}

.navbar {
    position: sticky !important;
    position: -webkit-sticky !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    z-index: 9999 !important;
    background-color: var(--bg-surface, #ffffff) !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
    border-bottom: 1px solid var(--border-color, #e2e8f0) !important;
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
        
        # Replace overflow-x: hidden on html, body with overflow-x: clip
        c = c.replace('overflow-x: hidden !important;', 'overflow-x: clip !important;')

        if 'PERMANENT STICKY NAVBAR FIX' not in c:
            c += '\n' + css_sticky_fix
            
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated sticky navbar and overflow-x in {p}")

print("Sticky navbar fix complete!")
