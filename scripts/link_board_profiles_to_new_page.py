import glob

files = []
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\*.html'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\*.html'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\*.astro'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\layouts\*.astro'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\*.html'))

count = 0
for fpath in set(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'investors.html#board-directors' in content and 'Profile of Board of Directors' in content:
        new_content = content.replace('href="investors.html#board-directors" class="dropdown-item">Profile of Board of Directors', 'href="company-information.html" class="dropdown-item">Profile of Board of Directors')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated Profile of Board of Directors link to company-information.html across {count} files!")
