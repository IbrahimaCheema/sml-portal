import glob

js_files = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

for j in js_files:
    try:
        with open(j, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix initThemeToggle
        if 'themeBtn.addEventListener(' in content and 'if (themeBtn)' not in content:
            content = content.replace(
                "themeBtn.addEventListener('click', () => {",
                "if (themeBtn) {\n        themeBtn.addEventListener('click', () => {"
            )
            content = content.replace(
                "localStorage.setItem('sml_theme', newTheme);\n    });\n}",
                "localStorage.setItem('sml_theme', newTheme);\n        });\n    }\n}"
            )

        # Fix initMobileNav
        if 'hamburger.addEventListener(' in content and 'if (hamburger' not in content:
            content = content.replace(
                "hamburger.addEventListener('click', () => {",
                "if (hamburger && navMenu) {\n        hamburger.addEventListener('click', () => {"
            )
            content = content.replace(
                "navMenu.classList.remove('active');\n        });\n    });\n}",
                "navMenu.classList.remove('active');\n            });\n        });\n    }\n}"
            )

        with open(j, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Fixed null checks in {j}")
    except FileNotFoundError:
        pass
