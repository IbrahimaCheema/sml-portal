import glob
import re

stock_block = """            <div class="stock-ticker">
                <span class="stock-item">Current Price: <strong id="stockPrice">Rs. 93.65</strong></span>
                <span class="stock-item change positive" id="stockChange">▼ -7.79 (-7.68%)</span>
                <span class="stock-item">LDCP: <strong id="stockLdcp">101.44</strong></span>
                <span class="stock-item">Volume: <strong id="stockVolume">90 shares</strong></span>
            </div>"""

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
    if '<div class="stock-ticker">' in content:
        new_content = re.sub(r'<div class="stock-ticker">.*?</div>', stock_block, content, flags=re.DOTALL)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Fixed initial static stock HTML in all {count} page files!")
