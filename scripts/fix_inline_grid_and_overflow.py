import glob

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\shareholders-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\shareholders-information.html'
]

css_fix = """
    /* --- Master Mobile Overflow & Grid Specificity Fix --- */
    html, body {
        overflow-x: hidden !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .sh-main-grid {
        display: grid;
        grid-template-columns: 260px 1fr;
        gap: 2.5rem;
        align-items: start;
        width: 100%;
        box-sizing: border-box;
    }

    @media (max-width: 992px) {
        .sh-main-grid {
            grid-template-columns: 1fr !important;
            gap: 1.5rem !important;
        }

        .sh-sidebar {
            position: relative !important;
            top: 0 !important;
            width: 100% !important;
            box-sizing: border-box !important;
        }

        .sh-side-nav {
            display: flex !important;
            flex-direction: row !important;
            overflow-x: auto !important;
            white-space: nowrap !important;
            gap: 0.5rem !important;
            padding-bottom: 0.5rem !important;
            -webkit-overflow-scrolling: touch !important;
        }

        .side-nav-item {
            flex-shrink: 0 !important;
        }
    }

    @media (max-width: 768px) {
        .sh-section-card {
            padding: 1.25rem 1rem !important;
            width: 100% !important;
            box-sizing: border-box !important;
            overflow: hidden !important;
        }

        .sh-section-title {
            font-size: 1.25rem !important;
            word-break: break-word !important;
            overflow-wrap: anywhere !important;
            white-space: normal !important;
        }

        .sh-section-desc {
            font-size: 0.85rem !important;
            word-break: break-word !important;
        }

        .secp-portal-box {
            padding: 1rem !important;
            width: 100% !important;
            box-sizing: border-box !important;
        }

        .secp-portal-box img {
            max-width: 100% !important;
            height: auto !important;
        }

        .btn-primary-pill, .btn-primary-action, .btn-outline-action {
            width: 100% !important;
            display: flex !important;
            justify-content: center !important;
            text-align: center !important;
            box-sizing: border-box !important;
            white-space: normal !important;
        }

        .stock-ticker {
            font-size: 0.75rem !important;
            overflow-x: auto !important;
            white-space: nowrap !important;
        }
    }
"""

count = 0
for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace inline grid style on container tag with class .sh-main-grid
    old_container_tag = '<div class="container" style="display: grid; grid-template-columns: 280px 1fr; gap: 2.5rem; align-items: start;">'
    new_container_tag = '<div class="container sh-main-grid">'
    
    if old_container_tag in content:
        content = content.replace(old_container_tag, new_container_tag)
        
    # Replace style tag or append css_fix
    if '</style>' in content and '/* --- Master Mobile Overflow & Grid Specificity Fix --- */' not in content:
        content = content.replace('</style>', css_fix + '\n    </style>')
        
    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1

print(f"Fixed container inline grid style & master mobile overflow across {count} files!")
