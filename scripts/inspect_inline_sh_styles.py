import re

html = open(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\shareholders-information.html', encoding='utf-8').read()
matches = re.findall(r'<style[\s\S]*?</style>', html)
for i, m in enumerate(matches):
    print(f"=== Style Block {i+1} ===")
    lines = [line.strip() for line in m.split('\n') if 'sidebar' in line or 'sticky' in line or 'top' in line]
    print('\n'.join(lines[:30]))
