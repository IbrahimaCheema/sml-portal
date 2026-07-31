import glob

exact_sentence = "Shakarganj Limited is a premier diversified corporate industrial group delivering high-grade refined sugar, eco-friendly biofuels, and renewable co-generation power."

files = []
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\*.html'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\*.html'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\*.astro'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\layouts\*.astro'))
files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\*.html'))

for fpath in set(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'delivering high-grade refined sugar' in content:
        # Replace hero description text
        p_start = content.find('delivering high-grade refined sugar')
        p_begin = content.rfind('<p', 0, p_start)
        p_end = content.find('</p>', p_start) + 4
        if p_begin != -1 and p_end != -1:
            new_p = '<p class="hero-desc">\n                ' + exact_sentence + '\n            </p>'
            content_new = content[:p_begin] + new_p + content[p_end:]
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content_new)

print("Updated exact hero description text across all files!")
