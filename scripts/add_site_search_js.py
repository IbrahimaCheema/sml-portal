js_search = """

/* --- Site-Wide Search Component (Home Page Only) --- */
function initSiteSearch() {
    const input = document.getElementById('siteSearchInput');
    const dropdown = document.getElementById('siteSearchResults');

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
                        <span class="search-res-title">${item.title}</span>
                        <span class="search-cat-badge">${item.category}</span>
                    </div>
                    <div class="search-res-desc">${item.desc}</div>
                </a>
            `).join('');
        }
        dropdown.style.display = 'block';
    }

    input.addEventListener('input', performSearch);
    input.addEventListener('focus', () => {
        if (input.value.trim()) performSearch();
    });

    document.addEventListener('click', (e) => {
        if (!input.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    initSiteSearch();
});
"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

for t in targets:
    with open(t, 'a', encoding='utf-8') as f:
        f.write(js_search)

print("Appended site-wide search JS logic!")
