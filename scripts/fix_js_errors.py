import re

js_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

for j in js_files:
    try:
        with open(j, 'r', encoding='utf-8') as f:
            content = f.read()

        # Wrap everything in try-catch to be 100% bulletproof
        new_content = re.sub(
            r'document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{(.*?)\}\);',
            r"document.addEventListener('DOMContentLoaded', () => {\n    try { \1 } catch (e) { console.error('Error during init:', e); }\n});",
            content,
            flags=re.DOTALL
        )

        with open(j, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Added try-catch in {j}")
    except FileNotFoundError:
        pass
