import glob

inner_footer_html = """    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-content">
            <div class="footer-bottom">
                <p>&copy; 2026 Shakarganj Limited. All Rights Reserved.</p>
                <div class="legal-links"><a href="index.html">Home</a> | <a href="contact.html">Contact Us</a></div>
            </div>
        </div>
    </footer>"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\company-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\company-information.html'
]

count = 0
for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<footer class="footer">' in content:
        start_idx = content.find('<footer class="footer">')
        end_idx = content.find('</footer>', start_idx) + 9
        if start_idx != -1 and end_idx != -1:
            new_content = content[:start_idx] + inner_footer_html + content[end_idx:]
            with open(t, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

print(f"Synchronized footer on company-information page across {count} files to match all other inner pages!")
