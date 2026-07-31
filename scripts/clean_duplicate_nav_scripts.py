import glob
import re

html_files = glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\**\*.html', recursive=True)

pattern = r'<script>\s*\(function\(\)\s*\{\s*function setupNavDropdowns\(\)[\s\S]*?\}\)\(\);\s*</script>'

updated_count = 0
for f in html_files:
    try:
        content = open(f, encoding='utf-8').read()
        if 'setupNavDropdowns' in content:
            new_content = re.sub(pattern, '', content)
            # Fallback if pattern didn't match cleanly
            if 'setupNavDropdowns' in new_content:
                new_content = re.sub(r'<script>[\s\S]*?setupNavDropdowns[\s\S]*?</script>', '', new_content)
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Removed duplicate inline setupNavDropdowns from: {f}")
            updated_count += 1
    except Exception as e:
        print(f"Error on {f}: {e}")

print(f"Total HTML files cleaned: {updated_count}")
