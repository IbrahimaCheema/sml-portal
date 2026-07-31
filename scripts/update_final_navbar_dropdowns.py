import glob, re

# 1. CSS for Navbar Dropdowns
dropdown_css = """

/* --- Finalized Sub-Menu Navigation System --- */
.nav-item.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-toggle {
    cursor: pointer !important;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    user-select: none;
}

.dropdown-chevron {
    transition: transform 200ms ease;
}

.nav-item.dropdown:hover .dropdown-chevron,
.nav-item.dropdown.open .dropdown-chevron {
    transform: rotate(180deg);
}

.dropdown-menu {
    display: none;
    position: absolute;
    top: calc(100% + 6px);
    left: 0;
    min-width: 250px;
    background-color: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.16);
    padding: 0.6rem 0;
    z-index: 350;
    backdrop-filter: var(--backdrop-blur);
    animation: fadeInDropdown 200ms ease forwards;
}

@keyframes fadeInDropdown {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

.nav-item.dropdown:hover .dropdown-menu,
.nav-item.dropdown:focus-within .dropdown-menu,
.nav-item.dropdown.open .dropdown-menu {
    display: block;
}

.dropdown-item {
    display: block;
    padding: 0.65rem 1.35rem;
    font-size: 0.88rem;
    font-weight: 600;
    color: var(--text-main);
    text-decoration: none;
    transition: all 180ms ease;
    white-space: nowrap;
}

.dropdown-item:hover {
    background-color: rgba(0, 90, 43, 0.08);
    color: var(--primary);
    padding-left: 1.6rem;
}

@media (max-width: 900px) {
    .nav-menu {
        flex-direction: column;
        align-items: flex-start;
        width: 100%;
        padding: 1.25rem 1rem;
    }
    
    .nav-item.dropdown {
        width: 100%;
        margin-bottom: 0.5rem;
    }
    
    .dropdown-menu {
        position: static;
        box-shadow: none;
        border: none;
        background-color: rgba(0, 90, 43, 0.04);
        border-left: 3px solid var(--primary);
        border-radius: var(--radius-md);
        padding: 0.4rem 0;
        margin-top: 0.4rem;
        display: none;
    }
    
    .nav-item.dropdown.open .dropdown-menu {
        display: block;
    }
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
    if '/* --- Finalized Sub-Menu Navigation System' not in content:
        new_content = content + dropdown_css
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Updated CSS with Finalized Sub-Menu styles!")

# 2. Master Navigation HTML Block
nav_html_master = """<nav class="nav-menu" id="navMenu">
                <a href="index.html" class="nav-link">Home</a>
                
                <!-- About Us Dropdown -->
                <div class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false">
                        About Us 
                        <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                    </a>
                    <div class="dropdown-menu">
                        <a href="about.html#company-profile" class="dropdown-item">Company's Profile</a>
                        <a href="about.html#associated-companies" class="dropdown-item">Associated Companies</a>
                    </div>
                </div>

                <!-- Divisions Dropdown -->
                <div class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false">
                        Divisions 
                        <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                    </a>
                    <div class="dropdown-menu">
                        <a href="divisions.html#sugar" class="dropdown-item">Sugar</a>
                        <a href="divisions.html#biofuel" class="dropdown-item">Bio Fuels</a>
                    </div>
                </div>

                <!-- Investor Relations Dropdown -->
                <div class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false">
                        Investor Relations 
                        <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                    </a>
                    <div class="dropdown-menu">
                        <a href="investors.html#board-directors" class="dropdown-item">Profile of Board of Directors</a>
                        <a href="investors.html#shareholder-info" class="dropdown-item">Shareholder's Information</a>
                        <a href="investors.html#financial-vault" class="dropdown-item">Financial Reports</a>
                        <a href="investors.html#financial-highlights" class="dropdown-item">Financial Highlights</a>
                        <a href="investors.html#stock-info" class="dropdown-item">Stock Information</a>
                        <a href="investors.html#shareholding-pattern" class="dropdown-item">Shareholding Pattern</a>
                        <a href="investors.html#free-float" class="dropdown-item">Free Float of Shares</a>
                        <a href="investors.html#corporate-briefing" class="dropdown-item">Corporate Briefing Session</a>
                        <a href="investors.html#share-registrar" class="dropdown-item">Share Registrar</a>
                        <a href="investors.html#election-directors" class="dropdown-item">Election of Directors</a>
                    </div>
                </div>

                <!-- Sustainability Dropdown -->
                <div class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false">
                        Sustainability 
                        <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                    </a>
                    <div class="dropdown-menu">
                        <a href="sustainability.html#hse" class="dropdown-item">Health Safety Environment</a>
                        <a href="sustainability.html#csr" class="dropdown-item">CSR</a>
                        <a href="sustainability.html#quality-assurance" class="dropdown-item">Quality Assurance</a>
                    </div>
                </div>

                <!-- Media Dropdown -->
                <div class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false">
                        Media 
                        <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                    </a>
                    <div class="dropdown-menu">
                        <a href="index.html#notices" class="dropdown-item">Notices & Updates</a>
                        <a href="index.html#notices" class="dropdown-item">Press Releases & News</a>
                    </div>
                </div>

                <a href="contact.html" class="nav-link">Contact Us</a>
            </nav>"""

html_files = []
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\*.html'))
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\*.html'))
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\*.astro'))
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\layouts\*.astro'))
html_files.extend(glob.glob(r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\*.html'))

count = 0
for fpath in set(html_files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<nav class="nav-menu"' in content:
        start_idx = content.find('<nav class="nav-menu"')
        end_idx = content.find('</nav>', start_idx) + 6
        if start_idx != -1 and end_idx != -1:
            page_nav = nav_html_master
            # Set active class based on page
            if 'about.html' in fpath or 'about.astro' in fpath:
                page_nav = page_nav.replace('About Us', 'About Us (Active)').replace('nav-item dropdown">', 'nav-item dropdown active">', 1)
            elif 'divisions.html' in fpath or 'divisions.astro' in fpath:
                page_nav = page_nav.replace('Divisions', 'Divisions (Active)').replace('Divisions \n', 'Divisions \n')
            elif 'investors.html' in fpath or 'investors.astro' in fpath:
                page_nav = page_nav.replace('Investor Relations', 'Investor Relations (Active)')
            elif 'sustainability.html' in fpath or 'sustainability.astro' in fpath:
                page_nav = page_nav.replace('Sustainability', 'Sustainability (Active)')
            elif 'contact.html' in fpath or 'contact.astro' in fpath:
                page_nav = page_nav.replace('class="nav-link">Contact Us', 'class="nav-link active">Contact Us')
            elif 'index.html' in fpath or 'index.astro' in fpath:
                page_nav = page_nav.replace('class="nav-link">Home', 'class="nav-link active">Home')
            
            # Remove (Active) text marker clean up
            page_nav = page_nav.replace(' (Active)', '')
            
            new_content = content[:start_idx] + page_nav + content[end_idx:]
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

print(f"Updated Navigation Bar across all {count} files!")

# 3. Add JS for dropdown toggling on click/tap
inline_dropdown_js = """
<script>
(function() {
    function setupNavDropdowns() {
        const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
        dropdownToggles.forEach(function(toggle) {
            toggle.onclick = function(e) {
                e.preventDefault();
                const parent = toggle.closest('.nav-item.dropdown');
                if (!parent) return;
                
                // Close other open dropdowns
                document.querySelectorAll('.nav-item.dropdown.open').forEach(function(item) {
                    if (item !== parent) item.classList.remove('open');
                });
                
                parent.classList.toggle('open');
            };
        });

        document.addEventListener('click', function(e) {
            if (!e.target.closest('.nav-item.dropdown')) {
                document.querySelectorAll('.nav-item.dropdown.open').forEach(function(item) {
                    item.classList.remove('open');
                });
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupNavDropdowns);
    } else {
        setupNavDropdowns();
    }
})();
</script>
"""

for fpath in set(html_files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'setupNavDropdowns' not in content and '</body>' in content:
        new_content = content.replace('</body>', inline_dropdown_js + '\n</body>')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Inserted setupNavDropdowns inline script into all page files!")
