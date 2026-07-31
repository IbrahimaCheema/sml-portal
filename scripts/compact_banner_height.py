import glob

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\company-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\company-information.html'
]

old_banner = '<section style="background: linear-gradient(135deg, #003318, #005a2b); padding: 4rem 0 4.5rem; color: #ffffff; text-align: center;">'
new_banner = '<section style="background: linear-gradient(135deg, #003318, #005a2b); padding: 2.25rem 0 2.5rem; color: #ffffff; text-align: center;">'

old_h1 = '<h1 style="font-size: 3rem; margin: 1rem 0 0.5rem; font-family: var(--font-heading); font-weight: 800; color: #ffffff !important; text-shadow: 0 4px 14px rgba(0,0,0,0.3);">'
new_h1 = '<h1 style="font-size: 2.35rem; margin: 0.5rem 0 0.35rem; font-family: var(--font-heading); font-weight: 800; color: #ffffff !important; text-shadow: 0 2px 8px rgba(0,0,0,0.3);">'

old_p = '<p style="font-size: 1.15rem; color: rgba(255,255,255,0.9); max-width: 780px; margin: 0 auto; line-height: 1.6;">'
new_p = '<p style="font-size: 1rem; color: rgba(255,255,255,0.88); max-width: 720px; margin: 0 auto; line-height: 1.5;">'

old_section2 = '<section style="padding: 3.5rem 0 5rem; background-color: var(--bg-main);">'
new_section2 = '<section style="padding: 2rem 0 4rem; background-color: var(--bg-main);">'

old_tabs_margin = 'margin-bottom: 3rem;'
new_tabs_margin = 'margin-bottom: 2rem;'

count = 0
for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_banner in content:
        content = content.replace(old_banner, new_banner)
        content = content.replace(old_h1, new_h1)
        content = content.replace(old_p, new_p)
        content = content.replace(old_section2, new_section2)
        content = content.replace(old_tabs_margin, new_tabs_margin)
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Compact banner height and padding applied across {count} files!")
