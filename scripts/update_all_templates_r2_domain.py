import os
import re

cdn = 'https://docs.sml.com.pk'

dirs = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign'
]

for d in dirs:
    if os.path.exists(d):
        for root, _, files in os.walk(d):
            for f in files:
                if f.endswith('.html') or f.endswith('.css') or f.endswith('.js') or f.endswith('.astro') or f.endswith('.ts'):
                    p = os.path.join(root, f)
                    with open(p, 'r', encoding='utf-8') as fh:
                        c = fh.read()
                    
                    updated = re.sub(r'/(images|docs)/', f'{cdn}/\\1/', c)
                    if updated != c:
                        with open(p, 'w', encoding='utf-8') as fh:
                            fh.write(updated)
                        print(f"Synced R2 custom domain in {os.path.relpath(p, d)}")

print("Template sync complete!")
