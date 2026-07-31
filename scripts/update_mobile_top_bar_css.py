import glob

mobile_top_bar_css = """

/* --- Mobile Top Info Bar (Stacked Address & UAN) --- */
@media (max-width: 768px) {
    .top-bar-content {
        display: flex !important;
        flex-direction: row !important;
        justify-content: space-between !important;
        align-items: center !important;
        padding: 0.4rem 0.5rem !important;
    }

    .top-info {
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 0.25rem !important;
        flex: 1 !important;
    }

    .top-info span {
        font-size: 0.75rem !important;
        line-height: 1.35 !important;
    }

    .top-info .divider,
    .top-divider {
        display: none !important;
    }

    .top-actions {
        margin-left: 0.75rem !important;
        flex-shrink: 0 !important;
        align-self: center !important;
    }
}
"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '/* --- Mobile Top Info Bar' in content:
        parts = content.split('/* --- Mobile Top Info Bar')
        new_content = parts[0] + mobile_top_bar_css
    else:
        new_content = content + mobile_top_bar_css
    with open(t, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Appended mobile top bar stacked layout CSS to all style files!")
