import re
import json
import sys
import os
import cloudscraper
import requests
from datetime import datetime, timezone, timedelta

def get_html_cloudscraper(url):
    try:
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        })
        res = scraper.get(url, timeout=15)
        if res.status_code == 200:
            return res.text
    except Exception as e:
        print(f"[Warning] Cloudscraper failed: {e}")
    return None

def get_html_requests(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://dps.psx.com.pk/'
        }
        res = requests.get(url, headers=headers, timeout=15)
        if res.status_code == 200:
            return res.text
    except Exception as e:
        print(f"[Warning] Direct requests failed: {e}")
    return None

def update_psx_data():
    url = 'https://dps.psx.com.pk/company/SML'
    pkt_tz = timezone(timedelta(hours=5))
    now_iso = datetime.now(pkt_tz).isoformat()
    
    html = get_html_cloudscraper(url)
    if not html:
        print("Retrying with standard HTTP requests...")
        html = get_html_requests(url)

    if html:
        price_match = re.search(r'class="quote__close">\s*Rs\.?\s*([\d\.,]+)', html)
        change_match = re.search(r'class="change__value">\s*([\d\.,\-]+)', html)
        percent_match = re.search(r'class="change__percent">\s*\(([\d\.,\%\-+]+)\)', html)
        volume_match = re.search(r'Volume</div>\s*<div class="stats_value">([0-9,]+)</div>', html, re.I)
        ldcp_match = re.search(r'LDCP</div>\s*<div class="stats_value">([0-9\.]+)</div>', html, re.I)
        
        if price_match:
            data = {
                "symbol": "SML",
                "name": "Shakarganj Limited",
                "current": price_match.group(1).replace(',', ''),
                "change": change_match.group(1) if change_match else "0.00",
                "percent": percent_match.group(1) if percent_match else "0.00%",
                "ldcp": ldcp_match.group(1) if ldcp_match else "103.95",
                "volume": (volume_match.group(1) + " shares") if volume_match else "0 shares",
                "source": "https://dps.psx.com.pk/company/SML",
                "last_updated": now_iso
            }
            
            json_str = json.dumps(data, indent=2) + "\n"
            os.makedirs("public/api", exist_ok=True)
            with open("public/api/psx.json", "w", encoding="utf-8") as f:
                f.write(json_str)
            with open("public/api/psx", "w", encoding="utf-8") as f:
                f.write(json_str)
                
            print("Successfully updated public/api/psx.json and public/api/psx with live PSX quote:")
            print(json_str)
            return True

    # Fallback to existing psx.json if scraping was blocked or failed
    if os.path.exists("public/api/psx.json"):
        try:
            with open("public/api/psx.json", "r", encoding="utf-8") as f:
                existing_data = json.load(f)
            existing_data["last_updated"] = now_iso
            json_str = json.dumps(existing_data, indent=2) + "\n"
            with open("public/api/psx.json", "w", encoding="utf-8") as f:
                f.write(json_str)
            with open("public/api/psx", "w", encoding="utf-8") as f:
                f.write(json_str)
            print("[Fallback] Preserved existing PSX data and updated timestamp:")
            print(json_str)
            return True
        except Exception as err:
            print(f"[Fallback Error] Failed to read/update cached data: {err}")

    return False

if __name__ == "__main__":
    success = update_psx_data()
    if not success:
        sys.exit(1)



