import glob

css_fix = """
/* ==========================================================================
   FINAL MOBILE NAVBAR & LOGO FIX
   ========================================================================== */

/* Fix the Logo Aspect Ratio and Bounds */
.brand-logo {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    max-width: 70vw !important; /* Don't overlap hamburger */
}

.brand-logo img {
    height: 48px !important;
    width: auto !important;
    max-width: 100% !important;
    object-fit: contain !important;
    flex-shrink: 0 !important;
}

@media (max-width: 768px) {
    /* Ensure the hamburger button is clickable and on top */
    .hamburger {
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-around !important;
        width: 30px !important;
        height: 24px !important;
        background: transparent !important;
        border: none !important;
        cursor: pointer !important;
        z-index: 9999 !important; /* Force on top of everything */
        padding: 0 !important;
        margin-left: auto !important;
    }

    .hamburger span {
        display: block !important;
        width: 100% !important;
        height: 3px !important;
        background-color: var(--primary) !important;
        border-radius: 3px !important;
        transition: all 0.3s linear !important;
        transform-origin: 1px !important;
    }

    /* Animate Hamburger into X */
    .hamburger.open span:nth-child(1) { transform: rotate(45deg) !important; }
    .hamburger.open span:nth-child(2) { opacity: 0 !important; }
    .hamburger.open span:nth-child(3) { transform: rotate(-45deg) !important; }

    /* Ensure Navbar Menu slides in properly */
    .nav-menu {
        position: fixed !important;
        top: 0 !important;
        left: -100% !important;
        width: 85vw !important;
        max-width: 400px !important;
        height: 100vh !important;
        background-color: var(--bg-surface) !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        padding: 80px 2rem 2rem !important; /* Space for logo/close button */
        transition: left 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        overflow-y: auto !important;
        z-index: 9998 !important; /* Just below hamburger */
        box-shadow: 10px 0 30px rgba(0,0,0,0.15) !important;
        display: flex !important; /* override the 900px query */
    }

    .nav-menu.active {
        left: 0 !important;
    }
    
    /* Make sure navbar content keeps logo and hamburger in row */
    .navbar-content {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
        flex-wrap: nowrap !important; /* Do not wrap these */
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
        if 'FINAL MOBILE NAVBAR & LOGO FIX' not in content:
            content += '\n' + css_fix
            with open(c, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {c}")
    except FileNotFoundError:
        pass

print("Done applying Final Navbar Fixes!")
