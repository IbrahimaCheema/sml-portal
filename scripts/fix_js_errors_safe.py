import re

js_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

safe_init = """
document.addEventListener('DOMContentLoaded', () => {
    try { initThemeToggle(); } catch (e) { console.error('Error initThemeToggle:', e); }
    try { initMobileNav(); } catch (e) { console.error('Error initMobileNav:', e); }
    try { initTabs(); } catch (e) { console.error('Error initTabs:', e); }
    try { initStockSimulation(); } catch (e) { console.error('Error initStockSimulation:', e); }
    try { initReportSearchAndFilter(); } catch (e) { console.error('Error initReportSearchAndFilter:', e); }
    try { initSiteSearch(); } catch (e) { console.error('Error initSiteSearch:', e); }
    try { initSugarCarousel(); } catch (e) { console.error('Error initSugarCarousel:', e); }
});
"""

for j in js_files:
    try:
        with open(j, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace the DOMContentLoaded block
        content = re.sub(
            r'document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{.*?\}\);',
            safe_init.strip(),
            content,
            flags=re.DOTALL
        )

        with open(j, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Isolated init blocks in {j}")
    except FileNotFoundError:
        pass
