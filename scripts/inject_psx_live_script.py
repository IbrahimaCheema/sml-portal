import glob
import os
import re

script_code = """<script>
// Live PSX Stock Ticker Fetch (Backend API + Direct Intraday + Multi-CORS Proxy Fallbacks)
async function fetchPsxStock() {
    const priceEl = document.getElementById('stockPrice');
    const changeEl = document.getElementById('stockChange');
    const ldcpEl = document.getElementById('stockLdcp');
    const volumeEl = document.getElementById('stockVolume');
    const invPriceEl = document.getElementById('investorStockPrice');
    const invChangeEl = document.getElementById('investorStockChange');
    const invLdcpEl = document.getElementById('investorStockLdcp');
    const psxPriceEl = document.getElementById('psx_live_price');
    const psxChangeEl = document.getElementById('psx_live_change');

    function applyData(data) {
        if (!data || !data.current) return;
        const priceNum = parseFloat(data.current.toString().replace(/,/g, '')).toFixed(2);
        const numChange = parseFloat(data.change || 0);
        const absChange = Math.abs(numChange).toFixed(2);
        const rawP = (data.percent || '0').toString().replace('%', '').replace('+', '').replace('-', '');
        const absPercent = Math.abs(parseFloat(rawP) || 0).toFixed(2);
        const isPositive = numChange >= 0;
        const arrow = isPositive ? '▲' : '▼';
        const sign = isPositive ? '+' : '-';
        const changeFormatted = arrow + ' ' + sign + absChange + ' (' + sign + absPercent + '%)';

        if (psxPriceEl) psxPriceEl.textContent = 'Rs.' + priceNum;
        if (psxChangeEl) {
            psxChangeEl.className = 'psx_change_val ' + (isPositive ? 'pos' : 'neg');
            psxChangeEl.innerHTML = '<span>' + arrow + ' ' + sign + absChange + '</span> <span>(' + sign + absPercent + '%)</span>';
        }

        if (priceEl) priceEl.textContent = 'Rs. ' + priceNum;
        if (changeEl) {
            changeEl.className = isPositive ? 'stock-item change positive' : 'stock-item change negative';
            changeEl.textContent = changeFormatted;
        }
        if (ldcpEl && data.ldcp) ldcpEl.textContent = data.ldcp;
        if (volumeEl && data.volume) volumeEl.textContent = (data.volume + '').replace(' shares', '') + ' shares';

        if (invPriceEl) invPriceEl.textContent = 'Rs. ' + priceNum;
        if (invChangeEl) {
            invChangeEl.style.color = isPositive ? '#4ade80' : '#f87171';
            invChangeEl.textContent = changeFormatted;
        }
        if (invLdcpEl && data.ldcp) invLdcpEl.textContent = data.ldcp;
    }

    async function fetchTimeout(url, options = {}, timeoutMs = 2500) {
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), timeoutMs);
        try {
            const res = await fetch(url, { ...options, signal: controller.signal });
            clearTimeout(timer);
            return res;
        } catch (e) {
            clearTimeout(timer);
            throw e;
        }
    }

    // 1. Backend Endpoint
    try {
        const res = await fetchTimeout('/api/psx', {}, 2500);
        if (res.ok) {
            const data = await res.json();
            if (data && data.current && !data.error) {
                applyData(data);
                return;
            }
        }
    } catch (e) {}

    // 2. Direct Intraday Endpoint
    try {
        const res = await fetchTimeout('https://dps.psx.com.pk/timeseries/int/SML', {}, 2500);
        if (res.ok) {
            const data = await res.json();
            if (data && data.data && data.data.length > 0) {
                const latest = data.data[0];
                if (latest && latest[1]) {
                    const price = parseFloat(latest[1]).toFixed(2);
                    applyData({
                        current: price,
                        change: '0.00',
                        percent: '0.00%',
                        ldcp: price,
                        volume: (latest[2] || '25') + ' shares'
                    });
                    return;
                }
            }
        }
    } catch (e) {}

    // 3. AllOrigins Proxy
    try {
        const proxyUrl = 'https://api.allorigins.win/get?url=' + encodeURIComponent('https://dps.psx.com.pk/company/SML');
        const res = await fetchTimeout(proxyUrl, {}, 3000);
        if (res.ok) {
            const json = await res.json();
            const html = json.contents || '';
            const priceMatch = html.match(/class="quote__close">\\s*Rs\\.?\\s*([\\d\\.,]+)/i);
            const changeMatch = html.match(/class="change__value">\\s*([\\d\\.,\\-]+)/i);
            const percentMatch = html.match(/class="change__percent">\\s*\\(([\\d\\.,\\%\\-+]+)\\)/i);
            const volumeMatch = html.match(/Volume<\\/div>\\s*<div class="stats_value">([0-9,]+)<\\/div>/i);
            const ldcpMatch = html.match(/LDCP<\\/div>\\s*<div class="stats_value">([0-9\\.]+)<\\/div>/i);

            if (priceMatch && priceMatch[1]) {
                applyData({
                    current: priceMatch[1],
                    change: changeMatch ? changeMatch[1] : '0.00',
                    percent: percentMatch ? percentMatch[1] : '0.00%',
                    ldcp: ldcpMatch ? ldcpMatch[1] : priceMatch[1],
                    volume: volumeMatch ? volumeMatch[1] : '25'
                });
                return;
            }
        }
    } catch (e) {}

    // 4. CodeTabs Proxy
    try {
        const proxyUrl = 'https://api.codetabs.com/v1/proxy?quest=' + encodeURIComponent('https://dps.psx.com.pk/company/SML');
        const res = await fetchTimeout(proxyUrl, {}, 3000);
        if (res.ok) {
            const html = await res.text();
            const priceMatch = html.match(/class="quote__close">\\s*Rs\\.?\\s*([\\d\\.,]+)/i);
            const changeMatch = html.match(/class="change__value">\\s*([\\d\\.,\\-]+)/i);
            const percentMatch = html.match(/class="change__percent">\\s*\\(([\\d\\.,\\%\\-+]+)\\)/i);
            const volumeMatch = html.match(/Volume<\\/div>\\s*<div class="stats_value">([0-9,]+)<\\/div>/i);
            const ldcpMatch = html.match(/LDCP<\\/div>\\s*<div class="stats_value">([0-9\\.]+)<\\/div>/i);

            if (priceMatch && priceMatch[1]) {
                applyData({
                    current: priceMatch[1],
                    change: changeMatch ? changeMatch[1] : '0.00',
                    percent: percentMatch ? percentMatch[1] : '0.00%',
                    ldcp: ldcpMatch ? ldcpMatch[1] : priceMatch[1],
                    volume: volumeMatch ? volumeMatch[1] : '25'
                });
                return;
            }
        }
    } catch (e) {}
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fetchPsxStock);
} else {
    fetchPsxStock();
}
</script>"""

dist_files = glob.glob('dist/*.html')
updated_count = 0

for fpath in dist_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Clean up old PSX stock scripts
    content = re.sub(r'<script>\s*// Client-side PSX Stock Ticker Fetch.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// Live PSX Stock Ticker Fetch.*?</script>', '', content, flags=re.DOTALL)
    
    if '</body>' in content:
        content = content.replace('</body>', script_code + '\n</body>')
    else:
        content = content + '\n' + script_code
        
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    updated_count += 1

print(f"Successfully injected/updated live PSX stock script across {updated_count} files in dist/")
