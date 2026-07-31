import os

css_notices_4_row = """
/* ==========================================================================
   ALL 4 NOTICES & UPDATES IN A SINGLE ROW ON DESKTOP
   ========================================================================== */
.notices-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 1.5rem !important;
    margin-top: 2.5rem !important;
}

.notice-card {
    display: flex !important;
    flex-direction: column !important;
    height: 100% !important;
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04) !important;
    transition: transform 250ms ease, box-shadow 250ms ease !important;
}

.notice-card:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1) !important;
    border-color: #005a2b !important;
}

.notice-img-wrapper {
    width: 100% !important;
    height: 160px !important;
    overflow: hidden !important;
    background: #f8fafc !important;
}

.notice-img-wrapper img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    transition: transform 300ms ease !important;
}

.notice-card:hover .notice-img-wrapper img {
    transform: scale(1.04) !important;
}

.notice-content {
    padding: 1.15rem 1.15rem 1.35rem !important;
    display: flex !important;
    flex-direction: column !important;
    flex-grow: 1 !important;
    justify-content: space-between !important;
}

.notice-title {
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    line-height: 1.4 !important;
    color: #0f172a !important;
    margin-bottom: 0.85rem !important;

    a {
        color: #0f172a !important;
        text-decoration: none !important;
        transition: color 200ms ease !important;
    }

    a:hover {
        color: #005a2b !important;
    }
}

.notice-date {
    font-size: 0.825rem !important;
    color: #64748b !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.4rem !important;
    font-weight: 500 !important;
}

@media (max-width: 1024px) and (min-width: 641px) {
    .notices-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 1.25rem !important;
    }
}

@media (max-width: 640px) {
    .notices-grid {
        grid-template-columns: 1fr !important;
        gap: 1.25rem !important;
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
        
        if 'ALL 4 NOTICES & UPDATES IN A SINGLE ROW' not in c:
            c += '\n' + css_notices_4_row
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Applied 4-in-a-row notices CSS to {p}")

print("Notices single row layout update complete!")
