import glob
import re

# 1. Update static HTML fallback across all page files to current PSX live quote (103.95, 0.00)
stock_block_new = """            <div class="stock-ticker">
                <span class="stock-item">Current Price: <strong id="stockPrice">Rs. 103.95</strong></span>
                <span class="stock-item change positive" id="stockChange">▲ +0.00 (+0.00%)</span>
                <span class="stock-item">LDCP: <strong id="stockLdcp">103.95</strong></span>
                <span class="stock-item">Volume: <strong id="stockVolume">25 shares</strong></span>
            </div>"""

html_files = []
html_files.extend(glob.glob('dist/*.html'))
html_files.extend(glob.glob('src/pages/*.astro'))
html_files.extend(glob.glob('src/layouts/*.astro'))

count = 0
for fpath in set(html_files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<div class="stock-ticker">' in content:
        new_content = re.sub(r'<div class="stock-ticker">.*?</div>', stock_block_new, content, flags=re.DOTALL)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated initial static stock HTML in all {count} files to match PSX live numbers (Rs. 103.95 / 0.00)!")
