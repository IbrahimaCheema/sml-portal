import glob
import re

content = open(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html', encoding='utf-8').read()
match = re.search(r'function setupNavDropdowns\(\)[\s\S]*?\}\)\(\);', content)
if match:
    print("setupNavDropdowns code:\n", match.group(0))
