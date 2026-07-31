import glob
import re

for folder in ['dist', 'public']:
    for fpath in glob.glob(f'{folder}/*.html'):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(r'id="stockPrice">Rs\.\s*[0-9\.]+', 'id="stockPrice">Rs. 93.65', content)
        content = re.sub(r'id="stockChange">[^<]+</span>', 'id="stockChange">▼ -7.79 (-7.68%)</span>', content)
        content = re.sub(r'id="stockLdcp">[0-9\.]+', 'id="stockLdcp">101.44', content)
        content = re.sub(r'id="stockVolume">[0-9,]+ shares', 'id="stockVolume">90 shares', content)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Successfully updated static HTML stock figures!")
