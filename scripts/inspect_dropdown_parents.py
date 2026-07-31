import glob
import re

files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\shareholders-information.html'
]

for f in files:
    content = open(f, encoding='utf-8').read()
    print(f"=== {f} ===")
    matches = re.findall(r'<[^>]*class=["\'][^"\']*dropdown[^"\']*["\'][^>]*>[\s\S]*?</a>', content)
    for m in matches[:3]:
        print("MATCH:", m.strip()[:150])
