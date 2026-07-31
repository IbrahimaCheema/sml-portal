import glob
import re

files = glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\*.html')

for f in files:
    content = open(f, encoding='utf-8').read()
    match = re.search(r'<header[\s\S]*?</header>', content)
    if match:
        print(f"=== {f} ===")
        header = match.group(0)
        # find dropdown toggles
        toggles = re.findall(r'<a[^>]*class=["\'][^"\']*dropdown-toggle[^"\']*["\'][^>]*>[\s\S]*?</a>', header)
        print("Toggles count:", len(toggles))
        if toggles:
            print("First toggle:", toggles[0])
