import glob

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\shareholders-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\shareholders-information.html'
]

count = 0
for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update email address to asif.ali@shakarganj.pk
    content = content.replace('asif.ali@shakarganj.com.pk', 'asif.ali@shakarganj.pk')
    
    # 2. Remove icon box from Unclaimed Dividends section
    old_icon_block = """                        <div class="doc-icon-badge-lg">
                                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                            </div>"""
    
    if old_icon_block in content:
        content = content.replace(old_icon_block, '')
        
    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1

print(f"Updated email to asif.ali@shakarganj.pk and removed Unclaimed Dividends icon across {count} files!")
