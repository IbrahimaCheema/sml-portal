import os

# 1. CSS snippet for active menu underline and highlight
css_active_fix = """
/* ==========================================================================
   ACTIVE PARENT MAIN MENU UNDERLINE & COLOR HIGHLIGHT
   ========================================================================== */
.nav-link.active,
.nav-item.active > .nav-link,
.nav-item.dropdown.active > .nav-link,
.nav-item.dropdown.active > .dropdown-toggle {
    color: var(--primary, #005a2b) !important;
    font-weight: 700 !important;
}

.nav-link.active::after,
.nav-item.active > .nav-link::after,
.nav-item.dropdown.active > .nav-link::after,
.nav-item.dropdown.active > .dropdown-toggle::after {
    width: 100% !important;
    background-color: var(--primary, #005a2b) !important;
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
        if 'ACTIVE PARENT MAIN MENU UNDERLINE' not in c:
            c += '\n' + css_active_fix
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Added active menu underline CSS to {p}")

# 2. Add active nav highlighting logic to main.js
js_paths = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

js_active_func = """

/* --- Active Main Menu Auto Highlighting --- */
function initActiveNavHighlight() {
    let currentPath = window.location.pathname.split('/').pop();
    if (!currentPath || currentPath === '') currentPath = 'index.html';
    
    // Clear existing active states
    document.querySelectorAll('.nav-menu .nav-item, .nav-menu .nav-link').forEach(el => {
        el.classList.remove('active');
    });

    let matched = false;

    // Check all sub-menu links inside dropdowns
    document.querySelectorAll('.dropdown-menu a').forEach(subLink => {
        const href = subLink.getAttribute('href');
        if (href) {
            const pageName = href.split('#')[0].split('/').pop();
            if (pageName && pageName === currentPath) {
                subLink.classList.add('active-sub');
                subLink.style.color = 'var(--primary, #005a2b)';
                subLink.style.fontWeight = '700';

                const parentDropdown = subLink.closest('.nav-item.dropdown');
                if (parentDropdown) {
                    parentDropdown.classList.add('active');
                    matched = true;
                }
            }
        }
    });

    // If no dropdown sub-item matched, highlight top-level links
    if (!matched) {
        document.querySelectorAll('.nav-menu > a.nav-link').forEach(topLink => {
            const href = topLink.getAttribute('href');
            if (href) {
                const pageName = href.split('#')[0].split('/').pop();
                if (pageName === currentPath) {
                    topLink.classList.add('active');
                }
            }
        });
    }
}
"""

for p in js_paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        
        if 'initActiveNavHighlight()' not in c:
            # Append function definition
            c += js_active_func
            
            # Add call into runInit
            if 'try { initThemeToggle(); }' in c:
                c = c.replace(
                    'try { initThemeToggle(); }',
                    'try { initActiveNavHighlight(); }\n    try { initThemeToggle(); }'
                )
            
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Added active menu highlight JS to {p}")

print("All active menu underline updates complete!")
