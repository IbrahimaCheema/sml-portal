import urllib.request
import json
import re

url = 'https://api.allorigins.win/get?url=' + urllib.parse.quote('https://dps.psx.com.pk/company/SML')
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        html = res_data.get('contents', '')
        
        price = re.search(r'class="quote__close">\s*Rs\.?\s*([\d\.,]+)', html)
        change = re.search(r'class="change__value">\s*([\d\.,\-]+)', html)
        percent = re.search(r'class="change__percent">\s*\(([\d\.,\%\-+]+)\)', html)
        is_pos = 'change__text--pos' in html
        
        print("--- ALLORIGINS LIVE PROXY RESPONSE ---")
        print("Price:", price.group(1) if price else "Not Found")
        print("Change:", change.group(1) if change else "Not Found")
        print("Percent:", percent.group(1) if percent else "Not Found")
        print("Is Positive:", is_pos)
except Exception as e:
    print("Error querying proxy:", e)
