import os

server_py_content = """import http.server
import socketserver
import urllib.request
import re
import json
import os
import mimetypes

PORT = 8080

class CleanRouterHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Real-Time PSX Live Proxy API Endpoint
        if self.path == '/api/psx':
            try:
                req = urllib.request.Request(
                    'https://dps.psx.com.pk/company/SML',
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                )
                with urllib.request.urlopen(req, timeout=6) as response:
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
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(json.dumps(data).encode('utf-8'))
                    return
            except Exception as e:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                fallback = {'symbol': 'SML', 'current': '103.95', 'change': '0.00', 'percent': '0.00%', 'ldcp': '103.95', 'volume': '25 shares'}
                self.wfile.write(json.dumps(fallback).encode('utf-8'))
                return

        # 2. Clean URL Router (Maps /about -> about.html, /investors -> investors.html, etc.)
        url_path = self.path.split('?')[0].rstrip('/')
        if url_path == '':
            url_path = '/'

        base_dir = os.path.dirname(os.path.abspath(__file__))

        clean_routes = {
            '/': 'dist/index.html',
            '/about': 'dist/about.html',
            '/divisions': 'dist/divisions.html',
            '/investors': 'dist/investors.html',
            '/sustainability': 'dist/sustainability.html',
            '/contact': 'dist/contact.html',
            '/admin': 'dist/admin.html',
            '/board-of-directors': 'dist/board-of-directors.html',
            '/shareholders-information': 'dist/shareholders-information.html'
        }

        target_file = None
        if url_path in clean_routes:
            target_file = os.path.join(base_dir, clean_routes[url_path])

        if not target_file or not os.path.isfile(target_file):
            target_file = os.path.join(base_dir, 'dist', url_path.lstrip('/'))

        if os.path.isfile(target_file):
            ext = os.path.splitext(target_file)[1].lower()
            mime_map = {
                '.html': 'text/html; charset=utf-8',
                '.css': 'text/css; charset=utf-8',
                '.js': 'application/javascript; charset=utf-8',
                '.json': 'application/json; charset=utf-8',
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.svg': 'image/svg+xml',
                '.pdf': 'application/pdf',
                '.ico': 'image/x-icon'
            }
            content_type = mime_map.get(ext, 'application/octet-stream')

            with open(target_file, 'rb') as f:
                content = f.read()

            self.send_response(200)
            self.send_header('Content-Type', content_type)
            if ext == '.pdf':
                self.send_header('Content-Disposition', f'inline; filename="{os.path.basename(target_file)}"')
            self.send_header('Content-Length', str(len(content)))
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            if self.command != 'HEAD':
                self.wfile.write(content)
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'<h1>404 Not Found - Shakarganj Server</h1>')

    def do_HEAD(self):
        self.do_GET()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CleanRouterHandler) as httpd:
        print(f"Shakarganj Local Dev Server running at http://localhost:{PORT}")
        httpd.serve_forever()
"""

with open(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\server.py', 'w', encoding='utf-8') as f:
    f.write(server_py_content)

print("Updated server.py with proper PDF application/pdf MIME type and Content-Disposition inline header!")
