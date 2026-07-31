import glob

css_addition = """

/* --- Company's Own Complaint Handling Cell Section --- */
.complaint-section {
    padding: 4rem 0 5rem;
    background-color: var(--bg-alt);
    border-top: 1px solid var(--border-color);
}

.complaint-card {
    background-color: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    padding: 3rem 2.5rem;
    box-shadow: var(--shadow-md);
    text-align: center;
    max-width: 1100px;
    margin: 0 auto;
}

.complaint-title {
    font-size: 2.1rem;
    color: var(--primary);
    margin-top: 0.35rem;
    margin-bottom: 1.25rem;
    line-height: 1.25;
}

.complaint-desc {
    font-size: 0.98rem;
    color: var(--text-muted);
    line-height: 1.7;
    max-width: 960px;
    margin: 0 auto 2.25rem;
    text-align: justify;
    text-justify: inter-word;
}

.secp-banner-wrapper {
    margin-bottom: 2rem;
    overflow: hidden;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    transition: transform 300ms ease, box-shadow 300ms ease;
}

.secp-banner-wrapper:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

.secp-banner-link {
    display: block;
}

.secp-banner-link img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: var(--radius-md);
}

.jama-punji-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 1.5rem;
}

.jama-punji-link {
    display: inline-block;
    transition: transform 250ms ease;
}

.jama-punji-link:hover {
    transform: scale(1.06);
}

.jama-punji-link img {
    height: 65px;
    width: auto;
    object-fit: contain;
}
"""

style_targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\styles.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\styles\global.css',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\styles.css'
]

for t in style_targets:
    with open(t, 'a', encoding='utf-8') as f:
        f.write(css_addition)

print("Appended Complaint Cell CSS to all stylesheets!")

complaint_html = """
    <!-- Company's Own Complaint Handling Cell Section -->
    <section class="section complaint-section">
        <div class="container">
            <div class="complaint-card">
                <span class="section-subtitle">SECP Regulatory Compliance</span>
                <h2 class="complaint-title">Company's Own Complaint Handling Cell</h2>
                <p class="complaint-desc">
                    In case your complaint has not been properly redressed by us, you may lodge your complaint with Securities and Exchange Commission of Pakistan (the “SECP”). However, please note that SECP will entertain only those complaints which were at first directly requested to be redressed by the company and the company has failed to redress the same. Further, the complaints that are not relevant to SECP’s regulatory domain/competence shall not be entertained by the SECP.
                </p>

                <div class="secp-banner-wrapper">
                    <a href="https://sdms.secp.gov.pk" target="_blank" rel="noopener noreferrer" class="secp-banner-link" aria-label="Lodge Complaint with SECP SDMS Portal">
                        <img src="/images/secp-banner.png" alt="Securities and Exchange Commission of Pakistan - Investor Complaints SDMS Portal">
                    </a>
                </div>

                <div class="jama-punji-wrapper">
                    <a href="https://jamapunji.pk" target="_blank" rel="noopener noreferrer" class="jama-punji-link" aria-label="Jama Punji Investor Education Portal">
                        <img src="/images/jama-punji.png" alt="Jama Punji - Investor Education Portal SECP">
                    </a>
                </div>
            </div>
        </div>
    </section>

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
    if '<!-- Company\'s Own Complaint Handling Cell Section -->' not in content and '<!-- Footer -->' in content:
        new_content = content.replace('<!-- Footer -->', complaint_html + '    <!-- Footer -->')
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Inserted Complaint Cell section right before footer across all index files!")
