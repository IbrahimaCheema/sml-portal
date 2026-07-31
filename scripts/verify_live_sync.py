import urllib.request
import json
import re
import time

def fetch_psx():
    url = 'https://dps.psx.com.pk/company/SML'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            price = re.search(r'class="quote__close">\s*Rs\.?\s*([\d\.,]+)', html)
            change = re.search(r'class="change__value">\s*([\d\.,\-]+)', html)
            percent = re.search(r'class="change__percent">\s*\(([\d\.,\%\-+]+)\)', html)
            return {
                'price': price.group(1) if price else 'N/A',
                'change': change.group(1) if change else 'N/A',
                'percent': percent.group(1) if percent else 'N/A'
            }
    except Exception as e:
        return {'error': str(e)}

def fetch_sml():
    url = 'https://sml.com.pk'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            
            # Find hoisted script bundles
            js_files = re.findall(r'src="(/_astro/[^"]+\.js)"', html)
            
            psx_code_found = False
            for js in js_files:
                js_url = 'https://sml.com.pk' + js
                try:
                    js_req = urllib.request.Request(js_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(js_req) as js_resp:
                        js_code = js_resp.read().decode('utf-8')
                        if 'psx_live_price' in js_code or 'allorigins.win' in js_code:
                            psx_code_found = True
                            break
                except Exception:
                    pass

            return {
                'psx_code_in_bundle': psx_code_found,
                'js_bundles': js_files
            }
    except Exception as e:
        return {'error': str(e)}

print("Fetching DPS PSX Direct...")
psx_data = fetch_psx()
print("DPS Data:", psx_data)

print("\nFetching SML Live Site Bundle...")
sml_data = fetch_sml()
print("SML Site Data:", sml_data)
