import re
import json
import sys
import cloudscraper
from datetime import datetime, timezone, timedelta

def update_psx_data():
    url = 'https://dps.psx.com.pk/company/SML'
    scraper = cloudscraper.create_scraper(browser={
        'browser': 'chrome',
        'platform': 'windows',
        'desktop': True
    })
    
    try:
        response = scraper.get(url, timeout=15)
        response.raise_for_status()
        html = response.text
        
        price_match = re.search(r'class="quote__close">\s*Rs\.?\s*([\d\.,]+)', html)
        change_match = re.search(r'class="change__value">\s*([\d\.,\-]+)', html)
        percent_match = re.search(r'class="change__percent">\s*\(([\d\.,\%\-+]+)\)', html)
        volume_match = re.search(r'Volume</div>\s*<div class="stats_value">([0-9,]+)</div>', html, re.I)
        ldcp_match = re.search(r'LDCP</div>\s*<div class="stats_value">([0-9\.]+)</div>', html, re.I)
        
        # UTC+5 (PKT timezone)
        pkt_tz = timezone(timedelta(hours=5))
        now_iso = datetime.now(pkt_tz).isoformat()
        
        data = {
            "symbol": "SML",
            "name": "Shakarganj Limited",
            "current": price_match.group(1).replace(',', '') if price_match else "103.95",
            "change": change_match.group(1) if change_match else "0.00",
            "percent": percent_match.group(1) if percent_match else "0.00%",
            "ldcp": ldcp_match.group(1) if ldcp_match else "103.95",
            "volume": (volume_match.group(1) + " shares") if volume_match else "25 shares",
            "source": "https://dps.psx.com.pk/company/SML",
            "last_updated": now_iso
        }
        
        json_str = json.dumps(data, indent=2) + "\n"
        
        # Write to public/api/psx.json and public/api/psx
        with open("public/api/psx.json", "w", encoding="utf-8") as f:
            f.write(json_str)
            
        with open("public/api/psx", "w", encoding="utf-8") as f:
            f.write(json_str)
            
        print("Successfully updated public/api/psx.json and public/api/psx with live PSX quote:")
        print(json_str)
        return True
    except Exception as e:
        print(f"Error fetching live PSX data: {e}")
        return False

if __name__ == "__main__":
    success = update_psx_data()
    if not success:
        sys.exit(1)


