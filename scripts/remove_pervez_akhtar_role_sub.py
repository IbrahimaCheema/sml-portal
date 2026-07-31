import glob

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\company-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\company-information.html'
]

count = 0
for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<p class="role-sub">Executive Director & CEO</p>' in content:
        new_content = content.replace('<p class="role-sub">Executive Director & CEO</p>', '<p class="role-sub">&nbsp;</p>')
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Removed 'Executive Director & CEO' from Mr. Muhammad Pervez Akhtar's card across {count} files while preserving spacing!")
