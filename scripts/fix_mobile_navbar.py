import re

css_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for c in css_files:
    try:
        with open(c, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove the dangerous global img, svg overrides
        img_svg_pattern = r'/\*\s*Force images to stay inside bounds\s*\*/\s*img,\s*svg\s*\{[^}]*\}'
        content = re.sub(img_svg_pattern, '', content)
        
        # Remove the dangerous global div override
        div_pattern = r'p,\s*a,\s*span,\s*h1,\s*h2,\s*h3,\s*h4,\s*h5,\s*h6,\s*div\s*\{'
        content = re.sub(div_pattern, r'p, a, span, h1, h2, h3, h4, h5, h6 {', content)
        
        with open(c, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {c}")
    except FileNotFoundError:
        pass

print("Done fixing navbar and logo CSS!")
