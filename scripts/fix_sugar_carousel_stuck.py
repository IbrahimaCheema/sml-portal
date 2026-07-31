import os

# Update initSugarCarousel in main.js across all script locations
sugar_js_fix = """
/* --- 7. Sugar Division Carousel --- */
function initSugarCarousel() {
    const slides = document.querySelectorAll('.sugar-slide');
    const dots = document.querySelectorAll('.carousel-dots .dot');
    const prevBtn = document.getElementById('sugarPrev');
    const nextBtn = document.getElementById('sugarNext');

    if (slides.length === 0) return;

    let currentIndex = 0;

    function goToSlide(index) {
        currentIndex = (index + slides.length) % slides.length;
        
        slides.forEach((slide, i) => {
            if (i === currentIndex) {
                slide.classList.add('active');
                slide.style.setProperty('display', 'grid', 'important');
            } else {
                slide.classList.remove('active');
                slide.style.setProperty('display', 'none', 'important');
            }
        });
        
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === currentIndex);
        });
    }

    // Ensure slide 0 is active initially
    goToSlide(0);

    if (nextBtn) {
        nextBtn.onclick = function(e) {
            e.preventDefault();
            goToSlide(currentIndex + 1);
        };
    }

    if (prevBtn) {
        prevBtn.onclick = function(e) {
            e.preventDefault();
            goToSlide(currentIndex - 1);
        };
    }

    dots.forEach((dot, i) => {
        dot.onclick = function(e) {
            e.preventDefault();
            goToSlide(i);
        };
    });
}
"""

js_paths = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

for p in js_paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        
        # Replace initSugarCarousel
        import re
        c = re.sub(
            r'/\* --- 7\. Sugar Division Carousel --- \*/[\s\S]*?$',
            sugar_js_fix.strip(),
            c
        )
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Fixed initSugarCarousel JS in {p}")

print("Sugar carousel stuck fix complete!")
