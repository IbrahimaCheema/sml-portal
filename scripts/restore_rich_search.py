import glob, re

# 1. Update HTML across all index files
search_box_html = """            <!-- Site-Wide Search Bar (Home Page Only) -->
            <div class="hero-search-wrapper">
                <div class="search-input-box">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2.5" style="margin-right: 0.75rem; flex-shrink: 0;"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                    <input type="text" id="siteSearchInput" placeholder="Search across Shakarganj site (e.g. Sugar, Annual Report, Biofuel, Directors, SECP)..." aria-label="Search across site">
                    <button id="siteSearchBtn" class="btn-primary" style="padding: 0.6rem 1.4rem; border-radius: var(--radius-full); margin-left: 0.5rem; font-size: 0.875rem; font-weight: 700; flex-shrink: 0; cursor: pointer; border: none; background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: #ffffff; box-shadow: 0 4px 12px rgba(0, 90, 43, 0.25);">Search</button>
                </div>
                <div id="siteSearchResults" class="site-search-dropdown"></div>
            </div>"""

html_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\index.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

for t in html_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<div class="hero-search-wrapper">' in content:
        start_idx = content.find('<!-- Site-Wide Search Bar')
        end_idx = content.find('</div>', content.find('id="siteSearchResults"')) + 6
        if start_idx != -1 and end_idx != -1:
            new_content = content[:start_idx] + search_box_html + content[end_idx:]
            with open(t, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Updated search box HTML with embedded Search button!")

# 2. Update CSS across all style files
search_rich_css = """
/* --- Site-Wide Search Component (Home Page Only) --- */
.hero-search-wrapper {
    max-width: 720px;
    margin: 0 auto 3.5rem;
    position: relative;
    z-index: 150;
}

.search-input-box {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: flex-start !important;
    background: var(--bg-surface) !important;
    border: 2px solid var(--primary-light) !important;
    border-radius: var(--radius-full) !important;
    padding: 0.4rem 0.5rem 0.4rem 1.4rem !important;
    box-shadow: 0 12px 30px rgba(0, 90, 43, 0.15) !important;
    transition: all 250ms ease !important;
    box-sizing: border-box !important;
    width: 100% !important;
}

.search-input-box:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 15px 35px rgba(0, 90, 43, 0.25) !important;
}

.search-input-box svg {
    margin-right: 0.75rem !important;
    flex-shrink: 0 !important;
    display: block !important;
}

.search-input-box input {
    flex: 1 !important;
    width: 100% !important;
    border: none !important;
    outline: none !important;
    background: transparent !important;
    font-size: 0.95rem !important;
    color: var(--text-main) !important;
    font-weight: 500 !important;
    padding: 0.25rem 0 !important;
    margin: 0 !important;
}

.site-search-dropdown {
    display: none;
    position: absolute;
    top: calc(100% + 10px);
    left: 0;
    right: 0;
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.22);
    z-index: 250;
    max-height: 440px;
    overflow-y: auto;
    text-align: left;
    padding: 0.85rem;
}

.search-result-item {
    display: block;
    padding: 1rem 1.15rem;
    border-radius: var(--radius-md);
    text-decoration: none;
    transition: all 200ms ease;
    border-bottom: 1px solid var(--border-color);
    background-color: var(--bg-surface);
    margin-bottom: 0.35rem;
}

.search-result-item:last-child {
    border-bottom: none;
    margin-bottom: 0;
}

.search-result-item:hover {
    background-color: rgba(0, 90, 43, 0.05);
    border-color: var(--primary-light);
    transform: translateX(4px);
}

.search-res-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.4rem;
}

.search-title-group {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex-wrap: wrap;
}

.search-res-title {
    font-size: 1.025rem;
    font-weight: 700;
    color: var(--primary);
}

.search-cat-badge {
    font-size: 0.725rem;
    font-weight: 700;
    padding: 0.2rem 0.65rem;
    border-radius: var(--radius-full);
    background-color: rgba(0, 90, 43, 0.1);
    color: var(--primary);
    border: 1px solid rgba(0, 90, 43, 0.25);
    white-space: nowrap;
}

.search-action-btn {
    font-size: 0.825rem;
    font-weight: 700;
    color: var(--primary);
    background: rgba(0, 90, 43, 0.08);
    padding: 0.3rem 0.85rem;
    border-radius: var(--radius-full);
    transition: all 200ms ease;
    white-space: nowrap;
}

.search-result-item:hover .search-action-btn {
    background: var(--primary);
    color: #ffffff;
}

.search-res-desc {
    font-size: 0.875rem;
    color: var(--text-muted);
    line-height: 1.45;
}

.no-results-box {
    padding: 1.5rem;
    text-align: center;
    color: var(--text-muted);
    font-size: 0.95rem;
}
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
    if '/* --- Site-Wide Search Component' in content:
        parts = content.split('/* --- Site-Wide Search Component')
        new_content = parts[0] + search_rich_css
    else:
        new_content = content + search_rich_css
    with open(t, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated search CSS with rich item cards and View buttons!")

# 3. Update JavaScript logic across all JS files and inline scripts
inline_js = """
<script>
(function() {
    function setupSiteSearch() {
        const input = document.getElementById('siteSearchInput');
        const dropdown = document.getElementById('siteSearchResults');
        const searchBtn = document.getElementById('siteSearchBtn');
        if (!input || !dropdown) return;

        const SITE_INDEX = [
            { title: 'Sugar Manufacturing & Refining Division', category: 'Division', url: 'divisions.html#sugar', desc: 'High-grade refined food & pharmaceutical sugar (32,000+ TCD capacity).' },
            { title: 'Biofuels & Power Division', category: 'Division', url: 'divisions.html#biofuel', desc: '150,000 L/day fuel-grade bio-ethanol distillery and renewable export power.' },
            { title: 'White Crystalline Sugar (1kg, 2kg, 5kg)', category: 'Product', url: 'index.html#crafting-sugar', desc: 'Pure, refined 100% white crystalline sugar sachet & family packs.' },
            { title: 'Crystal and Soft Brown Sugar (0.5kg)', category: 'Product', url: 'index.html#crafting-sugar', desc: 'Organic light & dark brown sugar for culinary baking.' },
            { title: 'Annual Report 2025 (PDF)', category: 'Financial Report', url: 'investors.html#financial-vault', desc: 'Audited Financial Statements & SECP filing for year 2025.' },
            { title: 'Condensed Interim Report Q3 2026', category: 'Financial Report', url: 'investors.html#financial-vault', desc: 'Quarterly financial results for period ended March 2026.' },
            { title: 'Half Yearly Financial Report 2026', category: 'Financial Report', url: 'investors.html#financial-vault', desc: 'Financial results for the half year ended 31 March 2026.' },
            { title: 'Notice of Extraordinary General Meeting (EGM)', category: 'Notice', url: 'investors.html#financial-vault', desc: 'Official notice for Extraordinary General Meeting for shareholders.' },
            { title: 'Corporate Briefing Session 2026', category: 'Notice', url: 'investors.html#financial-vault', desc: 'Presentation and investor briefing session updates.' },
            { title: 'Board of Directors & Management Profile', category: 'Governance', url: 'investors.html#board-directors', desc: 'Profiles of Board of Directors and senior leadership team.' },
            { title: 'Company\'s Own Complaint Handling Cell & SECP', category: 'Compliance', url: 'index.html#complaint', desc: 'SECP SDMS portal, investor complaints and Jama Punji.' },
            { title: 'About Shakarganj Limited (50+ Years History)', category: 'Company Profile', url: 'about.html', desc: 'Incorporated in 1967, premier Pakistani industrial conglomerate.' },
            { title: 'Share Registrar & Shareholding Pattern', category: 'Investor Relations', url: 'investors.html#shareholder-info', desc: 'CorpLink Share Registrar office, Lahore & PSX shareholding details.' },
            { title: 'Contact Corporate Office (Lahore HQ)', category: 'Contact', url: 'contact.html', desc: 'Executive Floor, IT Tower, Hali Road, Gulberg III, Lahore.' }
        ];

        function performSearch() {
            const query = input.value.toLowerCase().trim();
            if (!query) {
                dropdown.style.display = 'none';
                dropdown.innerHTML = '';
                return;
            }

            const matches = SITE_INDEX.filter(item => 
                item.title.toLowerCase().includes(query) ||
                item.category.toLowerCase().includes(query) ||
                item.desc.toLowerCase().includes(query)
            );

            if (matches.length === 0) {
                dropdown.innerHTML = '<div class="no-results-box">No matching pages or documents found for "<strong>' + query + '</strong>"</div>';
            } else {
                dropdown.innerHTML = matches.map(item => `
                    <a href="${item.url}" class="search-result-item">
                        <div class="search-res-header">
                            <div class="search-title-group">
                                <span class="search-res-title">${item.title}</span>
                                <span class="search-cat-badge">${item.category}</span>
                            </div>
                            <span class="search-action-btn">View &rarr;</span>
                        </div>
                        <div class="search-res-desc">${item.desc}</div>
                    </a>
                `).join('');
            }
            dropdown.style.display = 'block';
        }

        input.addEventListener('input', performSearch);
        input.addEventListener('keyup', performSearch);
        input.addEventListener('focus', function() {
            if (input.value.trim()) performSearch();
        });
        if (searchBtn) {
            searchBtn.addEventListener('click', performSearch);
        }

        document.addEventListener('click', function(e) {
            if (!input.contains(e.target) && !dropdown.contains(e.target) && (!searchBtn || !searchBtn.contains(e.target))) {
                dropdown.style.display = 'none';
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupSiteSearch);
    } else {
        setupSiteSearch();
    }
})();
</script>
"""

for t in html_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<script>' in content and 'setupSiteSearch' in content:
        start_script = content.find('<script>', content.find('setupSiteSearch') - 100)
        end_script = content.find('</script>', start_script) + 9
        if start_script != -1 and end_script != -1:
            new_content = content[:start_script] + inline_js + content[end_script:]
            with open(t, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Updated inline setupSiteSearch script with rich item rendering!")
