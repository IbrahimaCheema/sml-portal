import os
import re

css_slide_display_fix = """
/* ==========================================================================
   CAROUSEL SLIDE HIDING & TOGGLING FIX
   ========================================================================== */
.sugar-slide {
    display: none !important;
    grid-template-columns: 420px 1fr !important;
    gap: 3.5rem !important;
    align-items: center !important;
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 20px !important;
    padding: 2rem 2.5rem !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05) !important;
}

.sugar-slide.active {
    display: grid !important;
    animation: fadeInSlide 300ms ease forwards !important;
}

[data-theme="dark"] .sugar-slide {
    background: #0f2438 !important;
    border-color: rgba(255, 255, 255, 0.1) !important;
}

@media (max-width: 900px) {
    .sugar-slide {
        grid-template-columns: 1fr !important;
        padding: 2rem 1.5rem !important;
        gap: 2rem !important;
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
        
        # Remove conflicting .sugar-slide display: grid !important rules
        c = re.sub(
            r'\.sugar-slide\s*\{[^}]*display:\s*grid\s*!important;[^}]*\}',
            '',
            c
        )

        if 'CAROUSEL SLIDE HIDING & TOGGLING FIX' not in c:
            c += '\n' + css_slide_display_fix
        else:
            c = re.sub(
                r'/\* ==========================================================================\s*CAROUSEL SLIDE HIDING & TOGGLING FIX[\s\S]*$',
                css_slide_display_fix.strip(),
                c
            )

        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Fixed .sugar-slide CSS display in {p}")

print("Sugar slide display CSS fix complete!")
