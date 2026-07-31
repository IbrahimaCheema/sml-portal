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
    if 'investors.html#shareholder-info' in content or 'shareholder-information.html' in content:
        new_content = content.replace('href="investors.html#shareholder-info"', 'href="shareholders-information.html"')
        new_content = new_content.replace('href="shareholder-information.html"', 'href="shareholders-information.html"')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated Shareholder's Information link to shareholders-information.html across {count} files!")
