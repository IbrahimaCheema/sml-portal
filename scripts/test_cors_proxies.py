import urllib.request
import urllib.parse
import json

proxies = [
    ("Corsproxy.io Timeseries", "https://corsproxy.io/?" + urllib.parse.quote("https://dps.psx.com.pk/timeseries/int/SML")),
    ("Corsproxy.io HTML", "https://corsproxy.io/?" + urllib.parse.quote("https://dps.psx.com.pk/company/SML")),
    ("Codetabs HTML", "https://api.codetabs.com/v1/proxy?quest=" + urllib.parse.quote("https://dps.psx.com.pk/company/SML")),
    ("AllOrigins", "https://api.allorigins.win/get?url=" + urllib.parse.quote("https://dps.psx.com.pk/company/SML")),
]

for name, url in proxies:
    print(f"Testing {name}: {url}")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            content = resp.read()
            print(f"  -> SUCCESS ({len(content)} bytes)")
    except Exception as e:
        print(f"  -> FAILED ({e})")
