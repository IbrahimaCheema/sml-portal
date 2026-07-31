import os

company_info_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile of Board of Directors & Corporate Information | Shakarganj Limited</title>
    <meta name="description" content="Board of Directors profiles, Audit Committee, HR & Remuneration Committee, Risk Management, Executive Leadership and Corporate Governance at Shakarganj Limited (SML).">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Top Info Bar -->
    <div class="top-bar">
        <div class="container top-bar-content">
            <div class="top-info">
                <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Executive Floor, IT Tower, Hali Road, Gulberg III, Lahore</span>
                <span class="divider">|</span>
                <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> UAN: +92 42 111 111 765</span>
            </div>
            <div class="top-actions">
                <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark/light theme">
                    <svg class="sun-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
                    <svg class="moon-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
                </button>
            </div>
        </div>
    </div>

    <!-- Live PSX Stock Bar -->
    <div class="stock-bar">
        <div class="container stock-flex">
            <div class="stock-badge">
                <span class="pulse-dot"></span>
                <strong>PSX: SML</strong>
            </div>
            <div class="stock-ticker">
                <span class="stock-item">Current Price: <strong id="stockPrice">Rs. 100.00</strong></span>
                <span class="stock-item change negative" id="stockChange">▼ -1.44 (-1.42%)</span>
                <span class="stock-item">LDCP: <strong id="stockLdcp">101.44</strong></span>
                <span class="stock-item">Volume: <strong id="stockVolume">91 shares</strong></span>
            </div>
        </div>
    </div>

    <!-- Navigation Header -->
    <header class="navbar">
        <div class="container navbar-content">
            <a href="index.html" class="brand-logo">
                <img src="/images/logo.png" alt="Shakarganj Limited Logo" style="height: 48px; width: auto;">
            </a>
            
            <nav class="nav-menu" id="navMenu">
                <a href="index.html" class="nav-link">Home</a>
                
                <!-- About Us Dropdown -->
                <div class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" role="button">About Us <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></a>
                    <div class="dropdown-menu">
                        <a href="about.html#company-profile" class="dropdown-item">Company's Profile</a>
                        <a href="about.html#associated-companies" class="dropdown-item">Associated Companies</a>
                    </div>
                </div>

                <!-- Divisions Dropdown -->
                <div class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" role="button">Divisions <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></a>
                    <div class="dropdown-menu">
                        <a href="divisions.html#sugar" class="dropdown-item">Sugar</a>
                        <a href="divisions.html#biofuel" class="dropdown-item">Bio Fuels</a>
                    </div>
                </div>

                <!-- Investor Relations Dropdown (Active) -->
                <div class="nav-item dropdown active">
                    <a class="nav-link dropdown-toggle" role="button">Investor Relations <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></a>
                    <div class="dropdown-menu">
                        <a href="company-information.html" class="dropdown-item" style="color: var(--primary); font-weight: 700;">Profile of Board of Directors</a>
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
                    <a class="nav-link dropdown-toggle" role="button">Sustainability <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></a>
                    <div class="dropdown-menu">
                        <a href="sustainability.html#hse" class="dropdown-item">Health Safety Environment</a>
                        <a href="sustainability.html#csr" class="dropdown-item">CSR</a>
                        <a href="sustainability.html#quality-assurance" class="dropdown-item">Quality Assurance</a>
                    </div>
                </div>

                <!-- Media Dropdown -->
                <div class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" role="button">Media <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></a>
                    <div class="dropdown-menu">
                        <a href="index.html#notices" class="dropdown-item">Notices & Updates</a>
                        <a href="index.html#notices" class="dropdown-item">Press Releases & News</a>
                    </div>
                </div>

                <a href="contact.html" class="nav-link">Contact Us</a>
            </nav>

            <button class="hamburger" id="hamburger" aria-label="Toggle navigation">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>

    <!-- Page Header Banner -->
    <section style="background: linear-gradient(135deg, #003318, #005a2b); padding: 4rem 0 4.5rem; color: #ffffff; text-align: center;">
        <div class="container">
            <span style="background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25); padding: 0.35rem 1rem; border-radius: var(--radius-full); font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #ffffff;">Corporate Governance</span>
            <h1 style="font-size: 3rem; margin: 1rem 0 0.5rem; font-family: var(--font-heading); font-weight: 800; color: #ffffff !important; text-shadow: 0 4px 14px rgba(0,0,0,0.3);">Profile of Board of Directors</h1>
            <p style="font-size: 1.15rem; color: rgba(255,255,255,0.9); max-width: 780px; margin: 0 auto; line-height: 1.6;">Steered by experienced industrial leaders committed to high governance standards, transparency, and sustainable corporate growth.</p>
        </div>
    </section>

    <!-- Interactive Navigation Tabs Section -->
    <section style="padding: 3.5rem 0 5rem; background-color: var(--bg-main);">
        <div class="container">
            
            <!-- Category Tabs Selector -->
            <div style="display: flex; justify-content: center; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 3rem;" id="govTabButtons">
                <button class="gov-tab-btn active" onclick="switchGovTab('board')">Board of Directors</button>
                <button class="gov-tab-btn" onclick="switchGovTab('audit')">Audit Committee</button>
                <button class="gov-tab-btn" onclick="switchGovTab('hr')">HR & Remuneration</button>
                <button class="gov-tab-btn" onclick="switchGovTab('risk')">Risk Management</button>
                <button class="gov-tab-btn" onclick="switchGovTab('mgmt')">Executive Management</button>
                <button class="gov-tab-btn" onclick="switchGovTab('mgmt-cmte')">Management Committees</button>
            </div>

            <!-- Tab 1: Board of Directors -->
            <div id="tab-board" class="gov-tab-content active">
                <div style="text-align: center; margin-bottom: 2.5rem;">
                    <h2 class="gov-section-title">Board of Directors</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Fostering long-term strategic vision, compliance, and stakeholder value.</p>
                </div>

                <div class="directors-grid">
                    <!-- Director 1 -->
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/01/Untitled-240-x-321-px-302-x-584-px-3-1.png" alt="Mr. Manzoor Hussain">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Manzoor Hussain</h3>
                            <span class="role-badge">Chairman</span>
                            <p class="role-sub">Non-Executive Director</p>
                            <p class="joined-date">Joined Board: 2023</p>
                            <div class="address-box">
                                <strong class="address-label">Address:</strong><br>
                                Chak No. 77/5-L, P.O Chak No. 78/5-L, Tehsil & Distt. Sahiwal
                            </div>
                        </div>
                    </div>

                    <!-- Director 2 -->
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-07-at-11.35.50-AM-scaled-302x584.jpeg" alt="Mr. Muhammad Pervez Akhtar">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Muhammad Pervez Akhtar</h3>
                            <span class="role-badge">Chief Executive Officer</span>
                            <p class="role-sub">Executive Director & CEO</p>
                            <p class="joined-date">Joined Board: 2026</p>
                            <div class="address-box">
                                <strong class="address-label">Address:</strong><br>
                                Executive Floor, IT Tower, 73 E 1, Hali Road, Gulberg III, Lahore
                            </div>
                        </div>
                    </div>

                    <!-- Director 3 -->
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/01/Untitled-240-x-321-px-302-x-584-px-4.png" alt="Mr. Ali Altaf Saleem">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Ali Altaf Saleem</h3>
                            <span class="role-badge">Deputy CEO</span>
                            <p class="role-sub">Executive Director</p>
                            <p class="joined-date">Joined Board: 2010</p>
                            <div class="address-box">
                                <strong class="address-label">Address:</strong><br>
                                Executive Floor, IT Tower, 73 E 1, Hali Road, Gulberg III, Lahore
                            </div>
                        </div>
                    </div>

                    <!-- Director 4 -->
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2026/07/Baber_Zaman.png" alt="Mr. Baber Zaman">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Baber Zaman</h3>
                            <span class="role-badge">Director</span>
                            <p class="role-sub">Non-Executive Director</p>
                            <p class="joined-date">Joined Board: 2026</p>
                            <div class="address-box">
                                <strong class="address-label">Address:</strong><br>
                                Gulberg Greens Residencia, Islamabad
                            </div>
                        </div>
                    </div>

                    <!-- Director 5 -->
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2025/08/Adil-Qureshi.jpg" alt="Mr. Muhammad Adil Qureshi">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Muhammad Adil Qureshi</h3>
                            <span class="role-badge">Director</span>
                            <p class="role-sub">Independent Director</p>
                            <p class="joined-date">Joined Board: 2025</p>
                            <div class="address-box">
                                <strong class="address-label">Address:</strong><br>
                                Madina Town, Faisalabad
                            </div>
                        </div>
                    </div>

                    <!-- Director 6 -->
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-31-302x584.png" alt="Mr. Mustapha Altaf Saleem">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Mustapha Altaf Saleem</h3>
                            <span class="role-badge">Director</span>
                            <p class="role-sub">Executive Director</p>
                            <p class="joined-date">Joined Board: 2023</p>
                            <div class="address-box">
                                <strong class="address-label">Address:</strong><br>
                                Executive Floor, IT Tower, 73 E 1, Hali Road, Gulberg III, Lahore
                            </div>
                        </div>
                    </div>

                    <!-- Director 7 -->
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-34.png" alt="Mrs. Sana Atif">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mrs. Sana Atif</h3>
                            <span class="role-badge">Director</span>
                            <p class="role-sub">Independent Director</p>
                            <p class="joined-date">Joined Board: 2023</p>
                            <div class="address-box">
                                <strong class="address-label">Address:</strong><br>
                                Abdullah Gardens, Faisalabad
                            </div>
                        </div>
                    </div>

                    <!-- Director 8 -->
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2026/07/Waqas_Shafeeq.png" alt="Mr. Waqas Shafeeq">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Waqas Shafeeq</h3>
                            <span class="role-badge">Director</span>
                            <p class="role-sub">Non-Executive Director</p>
                            <p class="joined-date">Joined Board: 2026</p>
                            <div class="address-box">
                                <strong class="address-label">Address:</strong><br>
                                Punjab Small Industrial State Society, Bedian Road, Lahore
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tab 2: Audit Committee -->
            <div id="tab-audit" class="gov-tab-content">
                <div style="text-align: center; margin-bottom: 2.5rem;">
                    <h2 class="gov-section-title">Audit Committee</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Ensuring rigorous financial reporting, internal controls, and statutory audit integrity.</p>
                </div>
                <div class="directors-grid">
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-34.png" alt="Mrs. Sana Atif">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mrs. Sana Atif</h3>
                            <span class="role-badge">Chairperson</span>
                            <p class="role-sub">Independent Director</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/01/Untitled-240-x-321-px-302-x-584-px-3-1.png" alt="Mr. Manzoor Hussain">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Manzoor Hussain</h3>
                            <span class="role-badge">Member</span>
                            <p class="role-sub">Non-Executive Director</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2025/08/Adil-Qureshi.jpg" alt="Mr. Muhammad Adil Qureshi">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Muhammad Adil Qureshi</h3>
                            <span class="role-badge">Member</span>
                            <p class="role-sub">Independent Director</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tab 3: HR & Remuneration -->
            <div id="tab-hr" class="gov-tab-content">
                <div style="text-align: center; margin-bottom: 2.5rem;">
                    <h2 class="gov-section-title">HR & Remuneration and Nomination Committee</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Overseeing executive succession planning, talent development, and compensation structures.</p>
                </div>
                <div class="directors-grid">
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-34.png" alt="Mrs. Sana Atif">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mrs. Sana Atif</h3>
                            <span class="role-badge">Chairperson</span>
                            <p class="role-sub">Independent Director</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-31-302x584.png" alt="Mr. Mustapha Altaf Saleem">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Mustapha Altaf Saleem</h3>
                            <span class="role-badge">Member</span>
                            <p class="role-sub">Executive Director</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2025/08/Adil-Qureshi.jpg" alt="Mr. Muhammad Adil Qureshi">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Muhammad Adil Qureshi</h3>
                            <span class="role-badge">Member</span>
                            <p class="role-sub">Independent Director</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tab 4: Risk Management -->
            <div id="tab-risk" class="gov-tab-content">
                <div style="text-align: center; margin-bottom: 2.5rem;">
                    <h2 class="gov-section-title">Risk Management Committee of the Board</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Evaluating operational, market, and enterprise risk frameworks across all divisions.</p>
                </div>
                <div class="directors-grid">
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2025/08/Adil-Qureshi.jpg" alt="Mr. Muhammad Adil Qureshi">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Muhammad Adil Qureshi</h3>
                            <span class="role-badge">Chairman</span>
                            <p class="role-sub">Independent Director</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/01/Untitled-240-x-321-px-302-x-584-px-4.png" alt="Mr. Ali Altaf Saleem">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Ali Altaf Saleem</h3>
                            <span class="role-badge">Member</span>
                            <p class="role-sub">Executive Director</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-34.png" alt="Mrs. Sana Atif">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mrs. Sana Atif</h3>
                            <span class="role-badge">Member</span>
                            <p class="role-sub">Independent Director</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tab 5: Executive Management -->
            <div id="tab-mgmt" class="gov-tab-content">
                <div style="text-align: center; margin-bottom: 2.5rem;">
                    <h2 class="gov-section-title">The Management</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Senior executive leadership steering day-to-day operations and strategic execution.</p>
                </div>
                <div class="directors-grid">
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-07-at-11.35.50-AM-scaled-302x584.jpeg" alt="Mr. Muhammad Pervez Akhtar">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Muhammad Pervez Akhtar</h3>
                            <span class="role-badge">CEO</span>
                            <p class="role-sub">Chief Executive Officer</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/01/Untitled-240-x-321-px-302-x-584-px-4.png" alt="Mr. Ali Altaf Saleem">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Ali Altaf Saleem</h3>
                            <span class="role-badge">Deputy CEO</span>
                            <p class="role-sub">Deputy Chief Executive Officer</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-31-302x584.png" alt="Mr. Mustapha Altaf Saleem">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Mustapha Altaf Saleem</h3>
                            <span class="role-badge">Vice President</span>
                            <p class="role-sub">Vice President (Operations)</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-07-at-11.53.46-AM-1-302x584.jpeg" alt="Mr. Asif Ali">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Asif Ali</h3>
                            <span class="role-badge">Company Secretary</span>
                            <p class="role-sub">Company Secretary</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-07-at-11.53.46-AM-302x584.jpeg" alt="Mr. Muhammad Asif">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Muhammad Asif</h3>
                            <span class="role-badge">CFO</span>
                            <p class="role-sub">Chief Financial Officer</p>
                        </div>
                    </div>
                    <div class="director-card">
                        <div class="director-img-box">
                            <img src="https://www.sml.com.pk/wp-content/uploads/2025/08/cheema_SML.png" alt="Mr. Ibrahim A. Cheema">
                        </div>
                        <div class="director-info">
                            <h3 class="director-name">Mr. Ibrahim A. Cheema</h3>
                            <span class="role-badge">CIO</span>
                            <p class="role-sub">Chief Information Officer</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tab 6: Management Committees -->
            <div id="tab-mgmt-cmte" class="gov-tab-content">
                <div style="text-align: center; margin-bottom: 2.5rem;">
                    <h2 class="gov-section-title">Management Committees</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Operational, strategy, and technology execution committees.</p>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 2.5rem;">
                    <!-- Executive Committee -->
                    <div style="background-color: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2rem; box-shadow: var(--shadow-md);">
                        <h3 style="font-size: 1.5rem; color: var(--primary); margin-bottom: 1.25rem; font-weight: 700;">Executive Committee</h3>
                        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1.5rem;">
                            <div style="display: flex; align-items: center; gap: 1rem; background: var(--bg-alt); padding: 1rem; border-radius: var(--radius-md);">
                                <div style="font-weight: 700; color: var(--text-main);">Mr. Muhammad Saifullah<br><span style="font-size: 0.8rem; color: var(--primary);">Chairman</span></div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 1rem; background: var(--bg-alt); padding: 1rem; border-radius: var(--radius-md);">
                                <div style="font-weight: 700; color: var(--text-main);">Mr. Muhammad Pervez Akhtar<br><span style="font-size: 0.8rem; color: var(--primary);">Member</span></div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 1rem; background: var(--bg-alt); padding: 1rem; border-radius: var(--radius-md);">
                                <div style="font-weight: 700; color: var(--text-main);">Mr. Mustapha Altaf Saleem<br><span style="font-size: 0.8rem; color: var(--primary);">Member</span></div>
                            </div>
                        </div>
                    </div>

                    <!-- Business Strategy Committee -->
                    <div style="background-color: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2rem; box-shadow: var(--shadow-md);">
                        <h3 style="font-size: 1.5rem; color: var(--primary); margin-bottom: 1.25rem; font-weight: 700;">Business Strategy Committee</h3>
                        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1.5rem;">
                            <div style="display: flex; align-items: center; gap: 1rem; background: var(--bg-alt); padding: 1rem; border-radius: var(--radius-md);">
                                <div style="font-weight: 700; color: var(--text-main);">Mr. Ali Altaf Saleem<br><span style="font-size: 0.8rem; color: var(--primary);">Chairman</span></div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 1rem; background: var(--bg-alt); padding: 1rem; border-radius: var(--radius-md);">
                                <div style="font-weight: 700; color: var(--text-main);">Mr. Muhammad Pervez Akhtar<br><span style="font-size: 0.8rem; color: var(--primary);">Member</span></div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 1rem; background: var(--bg-alt); padding: 1rem; border-radius: var(--radius-md);">
                                <div style="font-weight: 700; color: var(--text-main);">Mr. Muhammad Asif<br><span style="font-size: 0.8rem; color: var(--primary);">Member</span></div>
                            </div>
                        </div>
                    </div>

                    <!-- System & Technology Committee -->
                    <div style="background-color: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2rem; box-shadow: var(--shadow-md);">
                        <h3 style="font-size: 1.5rem; color: var(--primary); margin-bottom: 1.25rem; font-weight: 700;">System & Technology Committee</h3>
                        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1.5rem;">
                            <div style="display: flex; align-items: center; gap: 1rem; background: var(--bg-alt); padding: 1rem; border-radius: var(--radius-md);">
                                <div style="font-weight: 700; color: var(--text-main);">Mr. Muhammad Pervez Akhtar<br><span style="font-size: 0.8rem; color: var(--primary);">Chairman</span></div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 1rem; background: var(--bg-alt); padding: 1rem; border-radius: var(--radius-md);">
                                <div style="font-weight: 700; color: var(--text-main);">Mr. Muhammad Asif<br><span style="font-size: 0.8rem; color: var(--primary);">Member</span></div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 1rem; background: var(--bg-alt); padding: 1rem; border-radius: var(--radius-md);">
                                <div style="font-weight: 700; color: var(--text-main);">Mr. Ibrahim A. Cheema<br><span style="font-size: 0.8rem; color: var(--primary);">Member</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <img src="/images/logo.png" alt="Shakarganj Logo" class="footer-logo">
                    <p>Shakarganj Limited is a leading Pakistani industrial conglomerate specializing in high-grade sugar manufacturing and bio-ethanol energy production.</p>
                </div>
                <div class="footer-links">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="divisions.html">Divisions</a></li>
                        <li><a href="investors.html">Investor Relations</a></li>
                        <li><a href="company-information.html">Board of Directors</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Corporate Office</h4>
                    <p>Executive Floor, IT Tower, Hali Road, Gulberg III, Lahore, Pakistan</p>
                    <p><strong>UAN:</strong> +92 42 111 111 765</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Shakarganj Limited. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <style>
        .gov-section-title {
            font-size: 2.25rem !important;
            color: var(--primary) !important;
            font-weight: 800 !important;
        }
        .gov-tab-btn {
            background-color: var(--bg-surface) !important;
            color: var(--text-main) !important;
            border: 1.5px solid var(--border-color) !important;
            padding: 0.65rem 1.35rem !important;
            border-radius: var(--radius-full) !important;
            font-size: 0.9rem !important;
            font-weight: 700 !important;
            cursor: pointer !important;
            transition: all 200ms ease !important;
            box-shadow: var(--shadow-sm) !important;
        }
        .gov-tab-btn.active, .gov-tab-btn:hover {
            background-color: var(--primary) !important;
            color: #ffffff !important;
            border-color: var(--primary) !important;
            box-shadow: 0 4px 14px rgba(0, 90, 43, 0.3) !important;
        }
        .gov-tab-content {
            display: none;
        }
        .gov-tab-content.active {
            display: block;
            animation: fadeInTab 300ms ease forwards;
        }
        @keyframes fadeInTab {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .directors-grid {
            display: grid !important;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)) !important;
            gap: 2rem !important;
        }
        .director-card {
            background-color: var(--bg-surface) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: var(--radius-xl) !important;
            overflow: hidden !important;
            box-shadow: var(--shadow-md) !important;
            transition: transform 250ms ease, box-shadow 250ms ease !important;
            display: flex !important;
            flex-direction: column !important;
        }
        .director-card:hover {
            transform: translateY(-5px) !important;
            box-shadow: var(--shadow-lg) !important;
            border-color: var(--primary-light) !important;
        }
        .director-img-box {
            width: 100% !important;
            height: 450px !important;
            overflow: hidden !important;
            background-color: #0b1e36 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }
        .director-img-box img {
            width: 100% !important;
            height: 100% !important;
            object-fit: contain !important;
            object-position: center bottom !important;
            transition: transform 300ms ease !important;
        }
        .director-card:hover .director-img-box img {
            transform: scale(1.03) !important;
        }
        .director-info {
            padding: 1.5rem !important;
            display: flex !important;
            flex-direction: column !important;
            flex: 1 !important;
        }
        .director-name {
            font-size: 1.25rem !important;
            color: var(--primary) !important;
            margin-bottom: 0.5rem !important;
            font-weight: 800 !important;
            display: block !important;
        }
        .role-badge {
            display: inline-block !important;
            align-self: flex-start !important;
            background-color: var(--primary) !important;
            color: #ffffff !important;
            padding: 0.25rem 0.75rem !important;
            border-radius: var(--radius-full) !important;
            font-size: 0.75rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.6rem !important;
            box-shadow: 0 2px 8px rgba(0, 90, 43, 0.2) !important;
        }
        .role-sub {
            font-size: 0.925rem !important;
            color: var(--text-main) !important;
            font-weight: 700 !important;
            margin-bottom: 0.25rem !important;
        }
        .joined-date {
            font-size: 0.8rem !important;
            color: var(--text-muted) !important;
            margin-bottom: 1.1rem !important;
        }
        .address-box {
            margin-top: auto !important;
            font-size: 0.825rem !important;
            color: var(--text-muted) !important;
            background-color: var(--bg-alt) !important;
            padding: 0.85rem !important;
            border-radius: var(--radius-md) !important;
            line-height: 1.45 !important;
            border: 1px solid var(--border-color) !important;
        }
        .address-label {
            color: var(--primary) !important;
            font-weight: 700 !important;
        }
    </style>

    <script>
        function switchGovTab(tabId) {
            document.querySelectorAll('.gov-tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.gov-tab-content').forEach(c => c.classList.remove('active'));

            const targetBtn = event.currentTarget;
            const targetContent = document.getElementById('tab-' + tabId);

            if (targetBtn) targetBtn.classList.add('active');
            if (targetContent) targetContent.classList.add('active');
        }
    </script>

    <script src="main.js"></script>
</body>
</html>"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\company-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\company-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\company-information.html'
]

for t in targets:
    with open(t, 'w', encoding='utf-8') as f:
        f.write(company_info_html)

print("Successfully restored high-contrast names, section titles, and active tab button styles!")
