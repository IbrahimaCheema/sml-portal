import urllib.request
import urllib.parse
import json
import re

targets = [
    ("AllOrigins RAW", "https://api.allorigins.win/raw?url=" + urllib.parse.quote("https://dps.psx.com.pk/company/SML")),
    ("AllOrigins GET", "https://api.allorigins.win/get?url=" + urllib.parse.quote("https://dps.psx.com.pk/company/SML")),
    ("CodeTabs", "https://api.codetabs.com/v1/proxy?quest=" + urllib.parse.quote("https://dps.psx.com.pk/company/SML")),
    ("ThingProxy", "https://thingproxy.freeboard.io/fetch/https://dps.psx.com.pk/company/SML"),
    ("PSX Intraday Direct", "https://dps.psx.com.pk/timeseries/int/SML")
]

for name, url in targets:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            price_match = re.search(r'class="quote__close">\s*Rs\.?\s*([\d\.,]+)', content)
            if price_match:
                print(f"[OK] {name}: Price = {price_match.group(1)}")
            elif 'data' in content and 'status' in content:
                print(f"[OK] {name}: Timeseries Data Received ({len(content)} bytes)")
            else:
                print(f"[WARN] {name}: Responded but price regex failed. Length={len(content)}")
    except Exception as e:
        print(f"[FAIL] {name}: {e}")
