import glob

full_js_search_script = """<script>
(function() {
    function setupSiteSearch() {
        const input = document.getElementById('siteSearchInput');
        const dropdown = document.getElementById('siteSearchResults');
        const searchBtn = document.getElementById('siteSearchBtn');
        if (!input || !dropdown) return;

        const SITE_INDEX = [
            { title: "Mr. Ali Habib (Director)", category: "Director Profile", url: "investors.html#board-directors", desc: "Independent Director, Member of Audit & HR Committees at Shakarganj Limited." },
            { title: "Syed Faisal Ali (Non-Executive Director)", category: "Director Profile", url: "investors.html#board-directors", desc: "Non-Executive Director with over 20 years corporate governance experience." },
            { title: "Mr. Mohammad Asghar (CEO & Managing Director)", category: "Leadership", url: "investors.html#board-directors", desc: "Chief Executive Officer leading Shakarganj industrial & biofuel strategy." },
            { title: "Mr. Mazhar Karim (Chairman Board of Directors)", category: "Leadership", url: "investors.html#board-directors", desc: "Chairman of the Board of Directors of Shakarganj Limited." },
            { title: "Mrs. Nusrat Jabeen (Independent Female Director)", category: "Director Profile", url: "investors.html#board-directors", desc: "Independent Director heading ESG & CSR sustainability oversight." },
            { title: "Board of Directors & Management Team", category: "Governance", url: "investors.html#board-directors", desc: "Complete profiles of Board of Directors and senior executive leadership." },
            { title: "Sugar Manufacturing & Refining Division", category: "Division", url: "divisions.html#sugar", desc: "High-grade refined food & pharmaceutical sugar (32,000+ TCD crushing capacity)." },
            { title: "Biofuels & Renewable Energy Division", category: "Division", url: "divisions.html#biofuel", desc: "150,000 L/day fuel-grade bio-ethanol distillery and renewable export power." },
            { title: "Jhang & Bhakkar Industrial Plants", category: "Facilities", url: "about.html#plants", desc: "State-of-the-art sugar crushing and biofuel distillery units in Punjab, Pakistan." },
            { title: "White Crystalline Sugar (1kg, 2kg, 5kg)", category: "Product", url: "index.html#crafting-sugar", desc: "Pure, refined 100% white crystalline sugar sachet & family packs." },
            { title: "Crystal and Soft Brown Sugar (0.5kg)", category: "Product", url: "index.html#crafting-sugar", desc: "Organic light & dark brown sugar for fine baking and cooking." },
            { title: "Annual Report 2025 (PDF)", category: "Financial Report", url: "investors.html#financial-vault", desc: "Audited Financial Statements & SECP annual filing for year 2025." },
            { title: "Condensed Interim Report Q3 2026", category: "Financial Report", url: "investors.html#financial-vault", desc: "Quarterly financial results for the period ended March 2026." },
            { title: "Half Yearly Financial Report 2026", category: "Financial Report", url: "investors.html#financial-vault", desc: "Financial results for the half year ended 31 March 2026." },
            { title: "Notice of Extraordinary General Meeting (EGM)", category: "Notice", url: "investors.html#financial-vault", desc: "Official notice for Extraordinary General Meeting for SML shareholders." },
            { title: "Corporate Briefing Session 2026", category: "Notice", url: "investors.html#financial-vault", desc: "Presentation and investor briefing session updates." },
            { title: "Company's Own Complaint Handling Cell & SECP", category: "Compliance", url: "index.html#complaint", desc: "SECP SDMS portal (https://sdms.secp.gov.pk), Toll Free 0800-88008." },
            { title: "Jama Punji Investor Education Portal (SECP)", category: "Compliance", url: "index.html#complaint", desc: "SECP investor awareness portal for smart, informed investing." },
            { title: "About Shakarganj Limited (50+ Years History)", category: "Company Profile", url: "about.html", desc: "Incorporated in 1967, premier Pakistani industrial conglomerate." },
            { title: "Share Registrar (CorpLink Lahore)", category: "Investor Relations", url: "investors.html#shareholder-info", desc: "CorpLink Share Registrar office, Lahore & PSX shareholding details." },
            { title: "Contact Corporate Office (Lahore HQ)", category: "Contact", url: "contact.html", desc: "Executive Floor, IT Tower, Hali Road, Gulberg III, Lahore (UAN: +92 42 111 111 765)." }
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
</script>"""

html_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\index.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\index.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\index.html'
]

for t in html_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<script>' in content and 'setupSiteSearch' in content:
        start_script = content.find('<script>', content.find('setupSiteSearch') - 100)
        end_script = content.find('</script>', start_script) + 9
        new_content = content[:start_script] + full_js_search_script + content[end_script:]
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Updated inline setupSiteSearch script with double-quoted JSON strings!")
