import glob
import re

files = glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\*.html')

for f in files:
    content = open(f, encoding='utf-8').read()
    scripts = re.findall(r'<script[\s\S]*?</script>', content)
    print(f"=== {f} ({len(scripts)} scripts) ===")
    for s in scripts:
        clean_s = s.replace('\n', ' ')
        print("  SCRIPT:", clean_s[:120])
