import glob

# 1. Update styles.css with display: grid !important; on .sugar-slide.active
style_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for t in style_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '.sugar-slide.active {' in content:
        content = content.replace('.sugar-slide.active {\n    display: grid;', '.sugar-slide.active {\n    display: grid !important;')
        content = content.replace('.sugar-slide.active {\n    display: grid', '.sugar-slide.active {\n    display: grid !important;')
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated CSS for .sugar-slide.active!")

# 2. Update main.js to call initSugarCarousel() at top DOMContentLoaded
js_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

for t in js_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'initSiteSearch();' in content and 'initSugarCarousel();' not in content[:300]:
        content = content.replace('initSiteSearch();', 'initSiteSearch();\n    initSugarCarousel();')
    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated main.js to invoke initSugarCarousel() on DOMContentLoaded!")

# 3. Add inline carousel script into index files to guarantee instant responsiveness
inline_carousel_js = """
<script>
(function() {
    function setupSugarCarousel() {
        const slides = document.querySelectorAll('.sugar-slide');
        const dots = document.querySelectorAll('.carousel-dots .dot');
        const prevBtn = document.getElementById('sugarPrev');
        const nextBtn = document.getElementById('sugarNext');

        if (!slides.length) return;

        let currentIndex = 0;

        function showSlide(index) {
            if (index < 0) index = slides.length - 1;
            if (index >= slides.length) index = 0;
            currentIndex = index;

            slides.forEach(function(s, idx) {
                if (idx === currentIndex) {
                    s.classList.add('active');
                    s.style.display = 'grid';
                } else {
                    s.classList.remove('active');
                    s.style.display = 'none';
                }
            });

            dots.forEach(function(d, idx) {
                if (idx === currentIndex) {
                    d.classList.add('active');
                } else {
                    d.classList.remove('active');
                }
            });
        }

        if (prevBtn) {
            prevBtn.onclick = function(e) {
                e.preventDefault();
                showSlide(currentIndex - 1);
            };
        }

        if (nextBtn) {
            nextBtn.onclick = function(e) {
                e.preventDefault();
                showSlide(currentIndex + 1);
            };
        }

        dots.forEach(function(dot, idx) {
            dot.onclick = function(e) {
                e.preventDefault();
                showSlide(idx);
            };
        });

        // Auto slide every 6 seconds
        setInterval(function() {
            showSlide(currentIndex + 1);
        }, 6000);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupSugarCarousel);
    } else {
        setupSugarCarousel();
    }
})();
</script>
"""

html_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\index.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

for t in html_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'setupSugarCarousel' not in content and '</body>' in content:
        new_content = content.replace('</body>', inline_carousel_js + '\n</body>')
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Inserted setupSugarCarousel inline script directly into all index files!")
