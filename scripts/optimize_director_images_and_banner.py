import glob

# 1. Update CSS rules for director cards & images
css_optimization = """
/* --- Director Card Portrait Display Optimization --- */
.director-img-box {
    width: 100%;
    height: 460px !important;
    overflow: hidden;
    background-color: #0b1e36 !important; /* Rich Navy Blue matching portrait studio backdrop */
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 !important;
}

.director-img-box img {
    width: 100% !important;
    height: 100% !important;
    object-fit: contain !important; /* Display full uncropped portrait including suit, tie & golden bottom bar */
    object-position: center bottom !important;
    transition: transform 300ms ease !important;
}

.director-card:hover .director-img-box img {
    transform: scale(1.03) !important;
}
"""

style_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for t in style_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '/* --- Director Card Portrait Display Optimization' not in content:
        new_content = content + css_optimization
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Updated CSS for full uncropped director portrait display!")

# 2. Update company-information.html page banner title color & container inline style
company_info_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\company-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\company-information.html'
]

for t in company_info_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ensure title in banner is crisp white
    content = content.replace('color: var(--primary);', 'color: #ffffff;')
    content = content.replace('<h1 style="font-size: 3rem; margin: 1rem 0 0.5rem; font-family: var(--font-heading); font-weight: 800; text-shadow: 0 4px 12px rgba(0,0,0,0.2);">', '<h1 style="font-size: 3rem; margin: 1rem 0 0.5rem; font-family: var(--font-heading); font-weight: 800; color: #ffffff !important; text-shadow: 0 4px 14px rgba(0,0,0,0.3);">')
    
    # Ensure img box style override in page
    if '.director-img-box {' in content:
        content = content.replace('height: 320px;', 'height: 460px; background-color: #0b1e36;')
        content = content.replace('object-fit: cover;', 'object-fit: contain;')
        
    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated company-information page title contrast and image box styles!")
