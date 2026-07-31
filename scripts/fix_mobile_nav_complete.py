import os
import re

# 1. Update main.js in all locations
main_js_content = """/* ==========================================================================
   SHAKARGANJ LIMITED (SML) - REDESIGN INTERACTIVE LOGIC
   ========================================================================== */

function runInit() {
    try { initThemeToggle(); } catch (e) { console.error('Error initThemeToggle:', e); }
    try { initMobileNav(); } catch (e) { console.error('Error initMobileNav:', e); }
    try { initTabs(); } catch (e) { console.error('Error initTabs:', e); }
    try { initStockSimulation(); } catch (e) { console.error('Error initStockSimulation:', e); }
    try { initReportSearchAndFilter(); } catch (e) { console.error('Error initReportSearchAndFilter:', e); }
    try { initSiteSearch(); } catch (e) { console.error('Error initSiteSearch:', e); }
    try { initSugarCarousel(); } catch (e) { console.error('Error initSugarCarousel:', e); }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runInit);
} else {
    runInit();
}

/* --- 1. Theme Toggle (Dark / Light Mode) --- */
function initThemeToggle() {
    const themeBtn = document.getElementById('themeToggle');
    const savedTheme = localStorage.getItem('sml_theme') || 'light';
    
    document.documentElement.setAttribute('data-theme', savedTheme);

    if (themeBtn) {
        themeBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('sml_theme', newTheme);
        });
    }
}

/* --- 2. Mobile Drawer Navigation --- */
function initMobileNav() {
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');

    if (hamburger && navMenu) {
        // Toggle mobile drawer
        hamburger.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            navMenu.classList.toggle('active');
            hamburger.classList.toggle('open');
        });

        // Toggle mobile dropdown menus when tapping dropdown headers
        document.querySelectorAll('.nav-item.dropdown > .dropdown-toggle').forEach(toggle => {
            toggle.addEventListener('click', (e) => {
                if (window.innerWidth <= 992) {
                    e.preventDefault();
                    e.stopPropagation();
                    const parent = toggle.closest('.nav-item.dropdown');
                    if (parent) {
                        parent.classList.toggle('open');
                    }
                }
            });
        });

        // Close menu when clicking sub-links or regular nav links
        document.querySelectorAll('.nav-menu a:not(.dropdown-toggle), .dropdown-menu a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                hamburger.classList.remove('open');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navMenu.contains(e.target) && !hamburger.contains(e.target)) {
                navMenu.classList.remove('active');
                hamburger.classList.remove('open');
            }
        });
    }
}

/* --- 3. Interactive Tabs for About Section --- */
function initTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-tab');

            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));

            btn.classList.add('active');
            const targetPane = document.getElementById(targetId);
            if (targetPane) targetPane.classList.add('active');
        });
    });
}

/* --- 4. Live Stock Price Simulation --- */
function initStockSimulation() {
    const currentPriceEl = document.getElementById('stockCurrent');
    const changeEl = document.getElementById('stockChange');
    const ldcpEl = document.getElementById('stockLdcp');
    const volumeEl = document.getElementById('stockVolume');

    if (!currentPriceEl) return;

    let basePrice = 100.00;

    async function fetchRealPSXData() {
        try {
            const response = await fetch('/api/psx');
            if (response.ok) {
                const data = await response.json();
                if (currentPriceEl) currentPriceEl.textContent = 'Rs. ' + data.current;
                if (ldcpEl) ldcpEl.textContent = data.ldcp;
                if (volumeEl) volumeEl.textContent = data.volume;
                
                if (changeEl) {
                    changeEl.textContent = (parseFloat(data.change) >= 0 ? '▲ +' : '▼ ') + data.change + ' (' + data.percent + ')';
                    changeEl.className = 'stock-item change ' + (parseFloat(data.change) >= 0 ? 'positive' : 'negative');
                }
                return;
            }
        } catch (e) {
            // Fallback simulation
        }

        const delta = (Math.random() * 0.4 - 0.2).toFixed(2);
        const newPrice = Math.max(90.00, (basePrice + parseFloat(delta))).toFixed(2);
        const diff = (newPrice - 100.00).toFixed(2);
        const percent = ((diff / 100.00) * 100).toFixed(2);

        currentPriceEl.textContent = `Rs. ${newPrice}`;
        
        if (diff >= 0) {
            changeEl.textContent = `▲ +${diff} (+${percent}%)`;
            changeEl.className = 'stock-item change positive';
        } else {
            changeEl.textContent = `▼ ${diff} (${percent}%)`;
            changeEl.className = 'stock-item change negative';
        }
    }

    fetchRealPSXData();
    setInterval(fetchRealPSXData, 10000);
}

/* --- 5. Report Vault Search & Category Filter --- */
function initReportSearchAndFilter() {
    const searchInput = document.getElementById('reportSearch');
    const categoryBtns = document.querySelectorAll('.cat-btn');
    const reportCards = document.querySelectorAll('.report-card');

    if (!searchInput && categoryBtns.length === 0) return;

    function filterReports() {
        const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
        const activeCategoryBtn = document.querySelector('.cat-btn.active');
        const selectedCat = activeCategoryBtn ? activeCategoryBtn.getAttribute('data-cat') : 'all';

        reportCards.forEach(card => {
            const title = (card.querySelector('h4') ? card.querySelector('h4').textContent : '').toLowerCase();
            const year = (card.querySelector('.report-year') ? card.querySelector('.report-year').textContent : '').toLowerCase();
            const category = card.getAttribute('data-category') || 'all';

            const matchesSearch = title.includes(query) || year.includes(query);
            const matchesCategory = selectedCat === 'all' || category === selectedCat;

            if (matchesSearch && matchesCategory) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }

    if (searchInput) searchInput.addEventListener('input', filterReports);

    categoryBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            categoryBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            filterReports();
        });
    });
}

/* --- 6. Global Site & Document Search --- */
function initSiteSearch() {
    const input = document.getElementById('siteSearchInput');
    const dropdown = document.getElementById('siteSearchResults');

    if (!input || !dropdown) return;

    const searchableContent = [
        { title: "Company Profile", category: "About Us", url: "about.html#company-profile", type: "page" },
        { title: "Associated Companies", category: "About Us", url: "about.html#associated-companies", type: "page" },
        { title: "Sugar Division & Milling", category: "Divisions", url: "divisions.html#sugar", type: "page" },
        { title: "Bio Fuel & Ethanol Production", category: "Divisions", url: "divisions.html#biofuel", type: "page" },
        { title: "Board of Directors Profile", category: "Governance", url: "board-of-directors.html", type: "page" },
        { title: "Shareholder Information", category: "Investor Relations", url: "shareholders-information.html", type: "page" },
        { title: "Annual Report 2023 (PDF)", category: "Financial Vault", url: "docs/shareholder/Notice-159-english-2026.pdf", type: "document" },
        { title: "SECP Investor Complaint Portal", category: "Investor Relations", url: "https://sdms.secp.gov.pk/", type: "external" },
        { title: "Contact Information & Head Office", category: "Contact", url: "contact.html", type: "page" }
    ];

    input.addEventListener('input', () => {
        const query = input.value.trim().toLowerCase();
        if (query.length < 2) {
            dropdown.style.display = 'none';
            dropdown.innerHTML = '';
            return;
        }

        const matches = searchableContent.filter(item => 
            item.title.toLowerCase().includes(query) || item.category.toLowerCase().includes(query)
        );

        if (matches.length === 0) {
            dropdown.innerHTML = '<div class="no-results-box">No matching pages found for "' + query + '"</div>';
        } else {
            dropdown.innerHTML = matches.map(item => `
                <a href="${item.url}" class="search-result-item">
                    <div class="result-title">${item.title}</div>
                    <div class="result-badge">${item.category}</div>
                </a>
            `).join('');
        }

        dropdown.style.display = 'block';
    });

    document.addEventListener('click', (e) => {
        if (!input.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
        }
    });
}

/* --- 7. Sugar Division Carousel --- */
function initSugarCarousel() {
    const track = document.getElementById('sugarCarousel');
    const prevBtn = document.getElementById('sugarPrev');
    const nextBtn = document.getElementById('sugarNext');

    if (!track || !prevBtn || !nextBtn) return;

    let currentIndex = 0;
    const items = track.querySelectorAll('.sugar-item');
    const totalItems = items.length;

    if (totalItems === 0) return;

    function updateCarousel() {
        track.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % totalItems;
        updateCarousel();
    });

    prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + totalItems) % totalItems;
        updateCarousel();
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
        with open(p, 'w', encoding='utf-8') as f:
            f.write(main_js_content.strip())
        print(f"Updated JS at {p}")

# 2. Add bulletproof CSS for navbar at max-width: 992px in all CSS files
css_add = """
/* ==========================================================================
   BULLETPROOF RESPONSIVE MOBILE DRAWER & NAVBAR (Up to 992px)
   ========================================================================== */
@media (max-width: 992px) {
    .hamburger {
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        width: 32px !important;
        height: 24px !important;
        background: transparent !important;
        border: none !important;
        cursor: pointer !important;
        z-index: 10001 !important;
        padding: 0 !important;
        margin-left: auto !important;
    }

    .hamburger span {
        display: block !important;
        width: 100% !important;
        height: 3px !important;
        background-color: var(--primary, #005a2b) !important;
        border-radius: 3px !important;
        transition: all 0.3s ease !important;
    }

    .hamburger.open span:nth-child(1) {
        transform: translateY(10.5px) rotate(45deg) !important;
    }

    .hamburger.open span:nth-child(2) {
        opacity: 0 !important;
    }

    .hamburger.open span:nth-child(3) {
        transform: translateY(-10.5px) rotate(-45deg) !important;
    }

    .nav-menu {
        position: fixed !important;
        top: 0 !important;
        left: -100% !important;
        width: 85vw !important;
        max-width: 360px !important;
        height: 100vh !important;
        background: #ffffff !important;
        flex-direction: column !important;
        align-items: stretch !important;
        justify-content: flex-start !important;
        padding: 80px 1.5rem 2rem !important;
        transition: left 0.35s ease-in-out !important;
        overflow-y: auto !important;
        z-index: 10000 !important;
        box-shadow: 4px 0 25px rgba(0,0,0,0.2) !important;
        display: flex !important;
    }

    .nav-menu.active {
        left: 0 !important;
    }

    .nav-menu .nav-link, 
    .nav-menu .dropdown-toggle {
        font-size: 1.05rem !important;
        padding: 0.75rem 1rem !important;
        color: #1a202c !important;
        border-bottom: 1px solid #edf2f7 !important;
        width: 100% !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
    }

    .nav-item.dropdown {
        width: 100% !important;
    }

    .nav-item.dropdown .dropdown-menu {
        position: static !important;
        box-shadow: none !important;
        border: none !important;
        background-color: #f7fafc !important;
        border-left: 3px solid #005a2b !important;
        border-radius: 4px !important;
        padding: 0.5rem 0 !important;
        margin: 0.25rem 0 0.5rem 0.5rem !important;
        display: none !important;
        width: calc(100% - 0.5rem) !important;
    }

    .nav-item.dropdown.open .dropdown-menu {
        display: block !important;
    }

    .navbar-content {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
        flex-wrap: nowrap !important;
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
        if 'BULLETPROOF RESPONSIVE MOBILE DRAWER' not in c:
            c += '\n' + css_add
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated CSS at {p}")

print("Complete update finished!")
