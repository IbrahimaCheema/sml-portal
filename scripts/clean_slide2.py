clean_text = "Shakarganj Limited's Crystal and Soft Brown sugars are crafted for exceptional baking and culinary flavor. Crystal brown sugar delivers a light, subtle molasses note, while soft brown sugar offers a richer, deep molasses texture. Both varieties add distinctive warmth and sweetness to fine recipes."

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\index.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    start_anchor = '<h3 class="sugar-title">Crystal and Soft Brown Sugar</h3>'
    if start_anchor in content:
        idx1 = content.find(start_anchor)
        p_start = content.find('<p class="sugar-desc">', idx1)
        p_end = content.find('</p>', p_start)
        new_content = content[:p_start] + '<p class="sugar-desc">\n                            ' + clean_text + '\n                        ' + content[p_end:]
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Successfully cleaned Slide 2 description text!")
