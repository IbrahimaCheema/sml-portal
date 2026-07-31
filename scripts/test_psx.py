import urllib.request
import re

req = urllib.request.Request('https://dps.psx.com.pk/company/SML', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

price_match = re.search(r'class="quote__close">Rs\.([0-9\.]+)<', html)
change_match = re.search(r'class="change__value">([0-9\.\-]+)<', html)
percent_match = re.search(r'class="change__percent">\s*\(([0-9\.\%\-]+)\)<', html)
volume_match = re.search(r'Volume</div><div class="stats_value">([0-9,]+)</div>', html)
ldcp_match = re.search(r'LDCP</div><div class="stats_value">([0-9\.]+)</div>', html)

print("PARSED FROM PSX:")
print("Price:", price_match.group(1) if price_match else "N/A")
print("Change:", change_match.group(1) if change_match else "N/A")
print("Percent:", percent_match.group(1) if percent_match else "N/A")
print("Volume:", volume_match.group(1) if volume_match else "N/A")
print("LDCP:", ldcp_match.group(1) if ldcp_match else "N/A")
