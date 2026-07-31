import glob
import re

files = []
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\*.html'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\*.html'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\*.astro'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\*.html'))

count = 0
for fpath in set(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'id="siteSearchBtn"' in content:
        new_content = re.sub(r'<button id="siteSearchBtn".*?</button>\s*', '', content, flags=re.DOTALL)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Successfully removed search button from search bar across {count} files!")
