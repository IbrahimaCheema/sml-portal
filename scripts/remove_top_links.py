import glob
import re

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
    if 'Investor Center' in content and 'top-actions' in content:
        new_content = re.sub(r'<a href="[^"]*investors[^"]*" class="quick-link">Investor Center</a>\s*', '', content)
        new_content = re.sub(r'<a href="[^"]*financial-vault[^"]*" class="quick-link">Financial Reports</a>\s*', '', new_content)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Successfully removed Investor Center and Financial Reports links from top bar across {count} files!")
