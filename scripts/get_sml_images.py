import urllib.request
import re

req = urllib.request.Request('https://www.sml.com.pk/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    images = re.findall(r'https?://[^\s\"\'\>]+?\.(?:png|jpg|jpeg|webp)', html, re.IGNORECASE)
    print(f"Found {len(set(images))} unique image URLs on sml.com.pk:")
    for img in sorted(set(images)):
        print('  -', img)
except Exception as e:
    print('Error fetching sml.com.pk:', e)
