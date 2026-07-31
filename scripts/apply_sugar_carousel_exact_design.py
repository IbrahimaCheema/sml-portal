import os
import re

# 1. CSS for Sugar Carousel matching sample image
sugar_css = """
/* ==========================================================================
   SUGAR HERITAGE & PRODUCT CAROUSEL SECTION (EXACT SAMPLE REPLICATION)
   ========================================================================== */
.sugar-heritage-section {
    padding: 5rem 0 6rem !important;
    background-color: #f8fafc !important;
    position: relative !important;
}

[data-theme="dark"] .sugar-heritage-section {
    background-color: #0b1a28 !important;
}

.sugar-heritage-section .section-subtitle {
    color: #005a2b !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    margin-bottom: 0.5rem !important;
}

.sugar-heritage-section .section-title {
    color: #0f172a !important;
    font-family: var(--font-heading, 'Outfit', sans-serif) !important;
    font-size: 2.35rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
}

[data-theme="dark"] .sugar-heritage-section .section-title {
    color: #f8fafc !important;
}

.sugar-carousel {
    position: relative !important;
    max-width: 1060px !important;
    margin: 3rem auto 0 !important;
}

.sugar-slide {
    display: none !important;
    grid-template-columns: 420px 1fr !important;
    gap: 3.5rem !important;
    align-items: center !important;
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 20px !important;
    padding: 3.25rem 3.5rem !important;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.06) !important;
    margin-bottom: 2rem !important;
}

.sugar-slide.active {
    display: grid !important;
    animation: fadeInSlide 300ms ease forwards !important;
}

@keyframes fadeInSlide {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

[data-theme="dark"] .sugar-slide {
    background: #0f2438 !important;
    border-color: rgba(255, 255, 255, 0.1) !important;
}

/* Left Image Box & Badge */
.sugar-img-container {
    position: relative !important;
    background: #f8fafc !important;
    border-radius: 14px !important;
    padding: 2.5rem 1.5rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-height: 320px !important;
    border: 1px solid #f1f5f9 !important;
}

[data-theme="dark"] .sugar-img-container {
    background: #081726 !important;
    border-color: rgba(255, 255, 255, 0.05) !important;
}

.sugar-badge {
    position: absolute !important;
    top: 1rem !important;
    left: 1rem !important;
    background: #004d25 !important;
    color: #ffffff !important;
    padding: 0.4rem 1rem !important;
    border-radius: 9999px !important;
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 8px rgba(0, 77, 37, 0.25) !important;
    z-index: 2 !important;
}

.sugar-img-container img {
    max-width: 100 !important;
    max-height: 260px !important;
    object-fit: contain !important;
    filter: drop-shadow(0 10px 18px rgba(0, 0, 0, 0.12)) !important;
}

/* Right Content Box */
.sugar-details {
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
}

.sugar-title {
    font-family: var(--font-heading, 'Outfit', sans-serif) !important;
    font-size: 2.1rem !important;
    font-weight: 800 !important;
    color: #005a2b !important;
    margin-bottom: 1rem !important;
    line-height: 1.25 !important;
}

[data-theme="dark"] .sugar-title {
    color: #10b981 !important;
}

.sugar-desc {
    font-size: 0.98rem !important;
    color: #64748b !important;
    line-height: 1.68 !important;
    margin-bottom: 1.75rem !important;
    font-weight: 400 !important;
}

[data-theme="dark"] .sugar-desc {
    color: #94a3b8 !important;
}

.sugar-sizes-title {
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    color: #1e293b !important;
    margin-bottom: 0.85rem !important;
}

[data-theme="dark"] .sugar-sizes-title {
    color: #cbd5e1 !important;
}

.sugar-sizes-list {
    display: flex !important;
    gap: 0.75rem !important;
    flex-wrap: wrap !important;
}

.size-pill {
    background: #f0fdf4 !important;
    border: 1px solid #dcfce7 !important;
    color: #005a2b !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    padding: 0.5rem 1.2rem !important;
    border-radius: 9999px !important;
    display: inline-flex !important;
    align-items: center !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02) !important;
}

[data-theme="dark"] .size-pill {
    background: rgba(16, 185, 129, 0.1) !important;
    border-color: rgba(16, 185, 129, 0.2) !important;
    color: #34d399 !important;
}

/* Controls Below Card (< ●━ • >) */
.carousel-controls {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 1.25rem !important;
    margin-top: 1.75rem !important;
}

.carousel-arrow {
    width: 44px !important;
    height: 44px !important;
    border-radius: 50% !important;
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    color: #0f172a !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    transition: all 200ms ease !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05) !important;
}

.carousel-arrow:hover {
    border-color: #005a2b !important;
    color: #005a2b !important;
    transform: scale(1.05) !important;
}

[data-theme="dark"] .carousel-arrow {
    background: #0f2438 !important;
    border-color: rgba(255, 255, 255, 0.15) !important;
    color: #f8fafc !important;
}

.carousel-dots {
    display: flex !important;
    align-items: center !important;
    gap: 0.6rem !important;
}

.carousel-dots .dot {
    width: 8px !important;
    height: 8px !important;
    border-radius: 50% !important;
    background-color: #cbd5e1 !important;
    cursor: pointer !important;
    transition: all 250ms ease !important;
}

.carousel-dots .dot.active {
    width: 28px !important;
    height: 8px !important;
    border-radius: 4px !important;
    background-color: #005a2b !important;
}

@media (max-width: 900px) {
    .sugar-slide {
        grid-template-columns: 1fr !important;
        padding: 2rem 1.5rem !important;
        gap: 2rem !important;
    }
}
"""

css_paths = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for p in css_paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        
        if 'SUGAR HERITAGE & PRODUCT CAROUSEL SECTION (EXACT SAMPLE REPLICATION)' not in c:
            c += '\n' + sugar_css
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Applied sugar carousel CSS to {p}")

# 2. Update initSugarCarousel in main.js to handle slides & dots cleanly
js_paths = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

sugar_js_func = """
/* --- 7. Sugar Division Carousel --- */
function initSugarCarousel() {
    const slides = document.querySelectorAll('.sugar-slide');
    const dots = document.querySelectorAll('.carousel-dots .dot');
    const prevBtn = document.getElementById('sugarPrev');
    const nextBtn = document.getElementById('sugarNext');

    if (slides.length === 0) return;

    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
        currentIndex = index;
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            let nextIndex = (currentIndex + 1) % slides.length;
            showSlide(nextIndex);
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            let prevIndex = (currentIndex - 1 + slides.length) % slides.length;
            showSlide(prevIndex);
        });
    }

    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => {
            showSlide(i);
        });
    });
}
"""

for p in js_paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        
        c = re.sub(
            r'/\* --- 7\. Sugar Division Carousel --- \*/[\s\S]*?$',
            sugar_js_func.strip(),
            c
        )
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated initSugarCarousel JS in {p}")

print("Sugar carousel replication complete!")
