import urllib.request
import urllib.parse
import re
import json

def check_direct_psx():
    print("=== 1. Direct DPS PSX Fetch (https://dps.psx.com.pk/company/SML) ===")
    url = 'https://dps.psx.com.pk/company/SML'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            
            # Extract company name
            name_m = re.search(r'<div class="quote__name">([^<]+)</div>', html)
            symbol_m = re.search(r'<div class="quote__symbol">([^<]+)</div>', html)
            price_m = re.search(r'class="quote__close">\s*Rs\.?\s*([\d\.,]+)', html)
            change_m = re.search(r'class="change__value">\s*([\d\.,\-]+)', html)
            percent_m = re.search(r'class="change__percent">\s*\(([\d\.,\%\-+]+)\)', html)
            volume_m = re.search(r'Volume</div>\s*<div class="stats_value">([0-9,]+)</div>', html, re.I)
            ldcp_m = re.search(r'LDCP</div>\s*<div class="stats_value">([0-9\.]+)</div>', html, re.I)
            high_m = re.search(r'High</div>\s*<div class="stats_value">([0-9\.]+)</div>', html, re.I)
            low_m = re.search(r'Low</div>\s*<div class="stats_value">([0-9\.]+)</div>', html, re.I)
            open_m = re.search(r'Open</div>\s*<div class="stats_value">([0-9\.]+)</div>', html, re.I)

            res = {
                'status': 'SUCCESS',
                'symbol': symbol_m.group(1).strip() if symbol_m else 'SML',
                'name': name_m.group(1).strip() if name_m else 'Shakarganj Limited',
                'price': price_m.group(1) if price_m else 'N/A',
                'change': change_m.group(1) if change_m else 'N/A',
                'percent': percent_m.group(1) if percent_m else 'N/A',
                'volume': volume_m.group(1) if volume_m else 'N/A',
                'ldcp': ldcp_m.group(1) if ldcp_m else 'N/A',
                'open': open_m.group(1) if open_m else 'N/A',
                'high': high_m.group(1) if high_m else 'N/A',
                'low': low_m.group(1) if low_m else 'N/A'
            }
            print(json.dumps(res, indent=2))
            return res
    except Exception as e:
        print(f"Error: {e}")
        return None

def check_timeseries_api():
    print("\n=== 2. DPS PSX Timeseries API (https://dps.psx.com.pk/timeseries/int/SML) ===")
    url = 'https://dps.psx.com.pk/timeseries/int/SML'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print("Status:", data.get("status"))
            if "data" in data and len(data["data"]) > 0:
                print(f"Latest Intraday Trade Record: Timestamp={data['data'][0][0]}, Price={data['data'][0][1]}, Volume={data['data'][0][2]}")
                print(f"Total Intraday Trades Today: {len(data['data'])}")
            else:
                print("No intraday trade data points in payload.")
    except Exception as e:
        print(f"Error: {e}")

def check_allorigins_proxy():
    print("\n=== 3. AllOrigins Proxy Fetch (Client-Side Fallback) ===")
    target = 'https://dps.psx.com.pk/company/SML'
    url = 'https://api.allorigins.win/get?url=' + urllib.parse.quote(target)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            html = data.get('contents', '')
            price_m = re.search(r'class="quote__close">\s*Rs\.?\s*([\d\.,]+)', html)
            change_m = re.search(r'class="change__value">\s*([\d\.,\-]+)', html)
            percent_m = re.search(r'class="change__percent">\s*\(([\d\.,\%\-+]+)\)', html)
            print("Proxy Scraped Price:", price_m.group(1) if price_m else "N/A")
            print("Proxy Scraped Change:", change_m.group(1) if change_m else "N/A")
            print("Proxy Scraped Percent:", percent_m.group(1) if percent_m else "N/A")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_direct_psx()
    check_timeseries_api()
    check_allorigins_proxy()
