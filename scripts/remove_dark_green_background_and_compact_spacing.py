import os
import re

css_clean_compact = """
/* ==========================================================================
   PERMANENT REMOVAL OF DARK GREEN BACKGROUND & COMPACT SPACING
   ========================================================================== */
.sugar-heritage-section {
    padding: 2.25rem 0 2.5rem !important;
    background: #ffffff !important;
    background-image: none !important;
    color: #0f172a !important;
    position: relative !important;
}

[data-theme="dark"] .sugar-heritage-section {
    background: #0b1a28 !important;
    background-image: none !important;
}

.sugar-heritage-section .section-header {
    margin-bottom: 1.25rem !important;
}

.sugar-carousel {
    position: relative !important;
    max-width: 1060px !important;
    margin: 1.25rem auto 0 !important;
}

.sugar-slide {
    padding: 2rem 2.5rem !important;
    margin-bottom: 1.25rem !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05) !important;
}

.carousel-controls {
    margin-top: 1.25rem !important;
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
        
        # Replace old dark gradient rule if present
        c = re.sub(
            r'\.sugar-heritage-section\s*\{\s*padding:\s*5rem\s*0;\s*background:\s*linear-gradient\([^;]+\);[\s\S]*?\}',
            '',
            c
        )

        if 'PERMANENT REMOVAL OF DARK GREEN BACKGROUND' not in c:
            c += '\n' + css_clean_compact
        else:
            # Update existing clean compact block
            c = re.sub(
                r'/\* ==========================================================================\s*PERMANENT REMOVAL OF DARK GREEN BACKGROUND[\s\S]*$',
                css_clean_compact.strip(),
                c
            )
            
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated clean white background & compact spacing in {p}")

print("Clean background and compact spacing update complete!")
