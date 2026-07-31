import glob

# 1. Update styles.css with theme icon visibility rules
theme_css_fix = """
/* --- Theme Toggle Icons Visibility --- */
.sun-icon { display: block !important; }
.moon-icon { display: none !important; }

[data-theme="dark"] .sun-icon { display: none !important; }
[data-theme="dark"] .moon-icon { display: block !important; }
"""

style_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for t in style_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '/* --- Theme Toggle Icons Visibility' not in content:
        new_content = content + theme_css_fix
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Updated styles.css with explicit theme icon visibility rules!")

# 2. Add inline theme toggle script across all HTML and Astro page files
inline_theme_js = """
<script>
(function() {
    function setupThemeToggle() {
        const themeBtn = document.getElementById('themeToggle');
        const savedTheme = localStorage.getItem('sml_theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);

        if (themeBtn) {
            themeBtn.onclick = function(e) {
                e.preventDefault();
                const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('sml_theme', newTheme);
            };
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupThemeToggle);
    } else {
        setupThemeToggle();
    }
})();
</script>
"""

html_files = []
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\*.html'))
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\*.html'))
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\*.astro'))
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\layouts\*.astro'))
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\*.html'))

count = 0
for fpath in set(html_files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'setupThemeToggle' not in content and '</body>' in content:
        new_content = content.replace('</body>', inline_theme_js + '\n</body>')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Inserted inline setupThemeToggle script into all {count} files!")
