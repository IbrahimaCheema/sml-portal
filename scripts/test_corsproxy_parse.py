import urllib.request
import urllib.parse
import json

url_ts = 'https://corsproxy.io/?' + urllib.parse.quote('https://dps.psx.com.pk/timeseries/int/SML')
req = urllib.request.Request(url_ts, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=6) as resp:
        content = resp.read().decode('utf-8')
        print("Corsproxy Timeseries Raw Content (first 200 chars):")
        print(content[:200])
        data = json.loads(content)
        if data.get('data'):
            print("Latest Trade Data:", data['data'][0])
except Exception as e:
    print("Error:", e)
