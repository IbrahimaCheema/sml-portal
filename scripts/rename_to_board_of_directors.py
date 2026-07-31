import os, glob

# 1. Rename files across directories
renames = [
    (r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\company-information.html', r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\board-of-directors.html'),
    (r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\company-information.html', r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\board-of-directors.html'),
    (r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\company-information.astro', r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\board-of-directors.astro'),
    (r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\company-information.html', r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\board-of-directors.html')
]

for old_p, new_p in renames:
    if os.path.exists(old_p):
        os.rename(old_p, new_p)

print("Renamed company-information files to board-of-directors!")

# 2. Replace all references to company-information.html across all codebase files
files = []
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\*.html'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\*.html'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\*.astro'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\layouts\*.astro'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\*.js'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\*.js'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\*.html'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\*.js'))

count = 0
for fpath in set(files):
    if not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'company-information.html' in content:
        new_content = content.replace('company-information.html', 'board-of-directors.html')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated all company-information.html link references to board-of-directors.html across {count} files!")
