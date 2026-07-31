import glob

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace unescaped single quote
    content = content.replace("Company's", "Company\\'s")
    
    # Add initSiteSearch to top DOMContentLoaded
    if "initSiteSearch();" not in content[:300]:
        content = content.replace("initReportSearchAndFilter();", "initReportSearchAndFilter();\n    initSiteSearch();")
        
    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)

print("Successfully fixed main.js syntax and enabled initSiteSearch!")
