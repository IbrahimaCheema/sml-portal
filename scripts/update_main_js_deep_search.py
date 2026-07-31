import glob

deep_index_js = """    const SITE_INDEX = [
        // --- Board of Directors & Leadership ---
        { title: 'Mr. Ali Habib (Director)', category: 'Director Profile', url: 'investors.html#board-directors', desc: 'Independent Director, Member of Audit & HR Committees at Shakarganj Limited.' },
        { title: 'Syed Faisal Ali (Non-Executive Director)', category: 'Director Profile', url: 'investors.html#board-directors', desc: 'Non-Executive Director with over 20 years corporate governance experience.' },
        { title: 'Mr. Mohammad Asghar (CEO & Managing Director)', category: 'Leadership', url: 'investors.html#board-directors', desc: 'Chief Executive Officer leading Shakarganj industrial & biofuel strategy.' },
        { title: 'Mr. Mazhar Karim (Chairman Board of Directors)', category: 'Leadership', url: 'investors.html#board-directors', desc: 'Chairman of the Board of Directors of Shakarganj Limited.' },
        { title: 'Mrs. Nusrat Jabeen (Independent Female Director)', category: 'Director Profile', url: 'investors.html#board-directors', desc: 'Independent Director heading ESG & CSR sustainability oversight.' },
        { title: 'Board of Directors & Management Team', category: 'Governance', url: 'investors.html#board-directors', desc: 'Complete profiles of Board of Directors and senior executive leadership.' },

        // --- Business Divisions & Manufacturing Plants ---
        { title: 'Sugar Manufacturing & Refining Division', category: 'Division', url: 'divisions.html#sugar', desc: 'High-grade refined food & pharmaceutical sugar (32,000+ TCD crushing capacity).' },
        { title: 'Biofuels & Renewable Energy Division', category: 'Division', url: 'divisions.html#biofuel', desc: '150,000 L/day fuel-grade bio-ethanol distillery and renewable export power.' },
        { title: 'Jhang & Bhakkar Industrial Plants', category: 'Facilities', url: 'about.html#plants', desc: 'State-of-the-art sugar crushing and biofuel distillery units in Punjab, Pakistan.' },

        // --- Consumer & Retail Products ---
        { title: 'White Crystalline Sugar (1kg, 2kg, 5kg)', category: 'Product', url: 'index.html#crafting-sugar', desc: 'Pure, refined 100% white crystalline sugar sachet & family packs.' },
        { title: 'Crystal and Soft Brown Sugar (0.5kg)', category: 'Product', url: 'index.html#crafting-sugar', desc: 'Organic light & dark brown sugar for fine baking and cooking.' },

        // --- Financial Reports & Investor Releases ---
        { title: 'Annual Report 2025 (PDF)', category: 'Financial Report', url: 'investors.html#financial-vault', desc: 'Audited Financial Statements & SECP annual filing for year 2025.' },
        { title: 'Condensed Interim Report Q3 2026', category: 'Financial Report', url: 'investors.html#financial-vault', desc: 'Quarterly financial results for the period ended March 2026.' },
        { title: 'Half Yearly Financial Report 2026', category: 'Financial Report', url: 'investors.html#financial-vault', desc: 'Financial results for the half year ended 31 March 2026.' },

        // --- Notices & Announcements ---
        { title: 'Notice of Extraordinary General Meeting (EGM)', category: 'Notice', url: 'investors.html#financial-vault', desc: 'Official notice for Extraordinary General Meeting for SML shareholders.' },
        { title: 'Corporate Briefing Session 2026', category: 'Notice', url: 'investors.html#financial-vault', desc: 'Presentation and investor briefing session updates.' },

        // --- Compliance, SECP & Complaints ---
        { title: 'Company\'s Own Complaint Handling Cell & SECP', category: 'Compliance', url: 'index.html#complaint', desc: 'SECP SDMS portal (https://sdms.secp.gov.pk), Toll Free 0800-88008.' },
        { title: 'Jama Punji Investor Education Portal (SECP)', category: 'Compliance', url: 'index.html#complaint', desc: 'SECP investor awareness portal for smart, informed investing.' },

        // --- Corporate Profile & Contact ---
        { title: 'About Shakarganj Limited (50+ Years History)', category: 'Company Profile', url: 'about.html', desc: 'Incorporated in 1967, premier Pakistani industrial conglomerate.' },
        { title: 'Share Registrar (CorpLink Lahore)', category: 'Investor Relations', url: 'investors.html#shareholder-info', desc: 'CorpLink Share Registrar office, Lahore & PSX shareholding details.' },
        { title: 'Contact Corporate Office (Lahore HQ)', category: 'Contact', url: 'contact.html', desc: 'Executive Floor, IT Tower, Hali Road, Gulberg III, Lahore (UAN: +92 42 111 111 765).' }
    ];"""

js_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\main.js',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\main.js'
]

for t in js_targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'const SITE_INDEX = [' in content:
        start_idx = content.find('const SITE_INDEX = [')
        end_idx = content.find('];', start_idx) + 2
        new_content = content[:start_idx] + deep_index_js + content[end_idx:]
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Updated main.js with deep search index!")
