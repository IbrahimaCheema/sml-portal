import glob

notices_html = """
    <!-- Notices & Updates Section -->
    <section class="section notices-section">
        <div class="container">
            <div class="section-header text-center">
                <h2 class="section-title">Notices & Updates</h2>
                <div class="accent-line"></div>
            </div>

            <div class="notices-grid">
                <!-- Notice Card 1 -->
                <div class="notice-card">
                    <a href="investors.html#financial-vault" class="notice-img-link">
                        <div class="notice-img-wrapper">
                            <img src="/images/notice-1.png" alt="Financial results for Half Year Ended 31 Mar 2026">
                        </div>
                    </a>
                    <div class="notice-content">
                        <div class="notice-gold-bar"></div>
                        <h3 class="notice-title">
                            <a href="investors.html#financial-vault">Financial results for the Half Year Ended 31 Mar 2026</a>
                        </h3>
                        <div class="notice-date">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                            <span>25 May, 2026</span>
                        </div>
                    </div>
                </div>

                <!-- Notice Card 2 -->
                <div class="notice-card">
                    <a href="investors.html#financial-vault" class="notice-img-link">
                        <div class="notice-img-wrapper">
                            <img src="/images/notice-2.png" alt="Notice of Extraordinary General Meeting">
                        </div>
                    </a>
                    <div class="notice-content">
                        <div class="notice-gold-bar"></div>
                        <h3 class="notice-title">
                            <a href="investors.html#financial-vault">Notice of Extraordinary General Meeting</a>
                        </h3>
                        <div class="notice-date">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                            <span>8 May, 2026</span>
                        </div>
                    </div>
                </div>

                <!-- Notice Card 3 -->
                <div class="notice-card">
                    <a href="investors.html#financial-vault" class="notice-img-link">
                        <div class="notice-img-wrapper">
                            <img src="/images/notice-3.png" alt="Corporate Briefing Session">
                        </div>
                    </a>
                    <div class="notice-content">
                        <div class="notice-gold-bar"></div>
                        <h3 class="notice-title">
                            <a href="investors.html#financial-vault">Corporate Briefing Session</a>
                        </h3>
                        <div class="notice-date">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                            <span>27 February, 2026</span>
                        </div>
                    </div>
                </div>

                <!-- Notice Card 4 -->
                <div class="notice-card">
                    <a href="investors.html#financial-vault" class="notice-img-link">
                        <div class="notice-img-wrapper">
                            <img src="/images/notice-4.png" alt="Quarterly Report Period Ended 31 Dec 2025">
                        </div>
                    </a>
                    <div class="notice-content">
                        <div class="notice-gold-bar"></div>
                        <h3 class="notice-title">
                            <a href="investors.html#financial-vault">Quarterly Report for the Period Ended 31 December, 2025</a>
                        </h3>
                        <div class="notice-date">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                            <span>10 February, 2026</span>
                        </div>
                    </div>
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
    if '<!-- Notices & Updates Section -->' not in content and '<!-- Footer -->' in content:
        new_content = content.replace('<!-- Footer -->', notices_html + '    <!-- Footer -->')
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Inserted Notices & Updates section right before footer in all index files!")
