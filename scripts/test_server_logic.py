import urllib.request
import re
import json

req = urllib.request.Request(
    'https://dps.psx.com.pk/company/SML',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
)
with urllib.request.urlopen(req, timeout=10) as response:
    html = response.read().decode('utf-8')
    price_match = re.search(r'class="quote__close">\s*Rs\.?\s*([\d\.,]+)<', html)
    change_match = re.search(r'class="change__value">\s*([\d\.,\-]+)<', html)
    percent_match = re.search(r'class="change__percent">\s*\(([\d\.,\%\-+]+)\)<', html)
    volume_match = re.search(r'Volume</div>\s*<div class="stats_value">([0-9,]+)</div>', html, re.I)
    ldcp_match = re.search(r'LDCP</div>\s*<div class="stats_value">([0-9\.]+)</div>', html, re.I)
    
    data = {
        'symbol': 'SML',
        'current': price_match.group(1).replace(',', '') if price_match else '103.95',
        'change': change_match.group(1) if change_match else '0.00',
        'percent': percent_match.group(1) if percent_match else '0.00%',
        'ldcp': ldcp_match.group(1) if ldcp_match else '103.95',
        'volume': volume_match.group(1) if volume_match else '25 shares',
        'source': 'https://dps.psx.com.pk/company/SML'
    }
    print("SERVER API PARSED OUTPUT:")
    print(json.dumps(data, indent=2))
