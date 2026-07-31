import glob

heritage_html = """
    <!-- Crafting Sugar since 1972 Section -->
    <section class="section sugar-heritage-section">
        <div class="container">
            <div class="section-header text-center">
                <span class="section-subtitle">Purity & Excellence</span>
                <h2 class="section-title">Crafting Sugar since 1972</h2>
            </div>

            <div class="sugar-carousel">
                <!-- Slide 1: White Crystalline Sugar -->
                <div class="sugar-slide active">
                    <div class="sugar-img-container">
                        <span class="sugar-badge">100% Pure & Refined</span>
                        <img src="/images/sugar-product-1.png" alt="White Crystalline Sugar - Shakarganj Good Food">
                    </div>
                    <div class="sugar-details">
                        <h3 class="sugar-title">White Crystalline Sugar</h3>
                        <p class="sugar-desc">
                            Shakarganj Limited's Crystalline White Sugar is meticulously crafted to offer the highest quality. It is pure, refined, and manufactured in a thoroughly hygienic environment. This premium sugar is carefully processed to ensure that every grain is of uniform size and sweetness, resulting in a consistent texture and flavor.
                        </p>
                        <div class="sugar-sizes-title">Available Pack Sizes</div>
                        <div class="sugar-sizes-list">
                            <span class="size-pill">1kg Pack</span>
                            <span class="size-pill">2kg Pack</span>
                            <span class="size-pill">5kg Pack</span>
                            <span class="size-pill">Sachet Pack</span>
                        </div>
                    </div>
                </div>

                <!-- Slide 2: Crystal and Soft Brown Sugar -->
                <div class="sugar-slide">
                    <div class="sugar-img-container">
                        <span class="sugar-badge">Organic & Natural</span>
                        <img src="/images/sugar-product-2.png" alt="Crystal and Soft Brown Sugar - Shakarganj Whole Foods">
                    </div>
                    <div class="sugar-details">
                        <h3 class="sugar-title">Crystal and Soft Brown Sugar</h3>
                        <p class="sugar-desc">
                            Shakarganj Limited's Crystal and Soft Brown sugar are two popular variations of sugar used in cooking and baking. Crystal brown sugar, often called light brown sugar, has a mild molasses flavor and a fine, sand-like texture. It's great for cookies and cakes. On the other hand, soft brown sugar, also known as dark brown sugar, has a stronger molasses taste and a moist, clumpy texture. It's ideal for rich, flavorful dishes like barbecue sauces and gingerbread. Both sugars bring their unique characteristics to recipes, adding depth and sweetness to a wide range of culinary delights.
                        </p>
                        <div class="sugar-sizes-title">Available Pack Sizes</div>
                        <div class="sugar-sizes-list">
                            <span class="size-pill">0.5kg Pack</span>
                            <span class="size-pill">Sachet Pack</span>
                        </div>
                    </div>
                </div>

                <!-- Carousel Controls -->
                <div class="carousel-controls">
                    <button class="carousel-arrow" id="sugarPrev" aria-label="Previous Slide">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
                    </button>
                    <div class="carousel-dots">
                        <span class="dot active"></span>
                        <span class="dot"></span>
                    </div>
                    <button class="carousel-arrow" id="sugarNext" aria-label="Next Slide">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                    </button>
                </div>
            </div>
        </div>
    </section>

"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\index.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<!-- Crafting Sugar since 1972 Section -->' not in content and '<!-- Notices & Updates Section -->' in content:
        new_content = content.replace('<!-- Notices & Updates Section -->', heritage_html + '    <!-- Notices & Updates Section -->')
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Inserted Crafting Sugar since 1972 section right before Notices & Updates!")
