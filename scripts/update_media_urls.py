import os
import sys
import re

def update_cdn_urls(r2_cdn_url):
    r2_cdn_url = r2_cdn_url.rstrip('/')
    
    html_dir = r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist'
    
    for root, _, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html') or file.endswith('.css') or file.endswith('.js'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace /images/ and /docs/ with R2 CDN URL
                updated = re.sub(r'/(images|docs)/', f'{r2_cdn_url}/\\1/', content)
                
                if updated != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(updated)
                    print(f"Updated media CDN URLs in {os.path.basename(path)}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        update_cdn_urls(sys.argv[1])
    else:
        print("Usage: python update_media_urls.py <R2_PUBLIC_CDN_URL>")
