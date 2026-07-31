import os

shareholder_info_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shareholder's Information | Investor Relations | Shakarganj Limited</title>
    <meta name="description" content="Official Shareholder Information, Share Registrar details, Election of Directors 2026, SECP Complaint Portal, Unclaimed Dividend, Code of Conduct, Policies Register, Compliance Certificate, and Gender Pay Gap Statement for Shakarganj Limited (SML).">
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
                        <a href="board-of-directors.html" class="dropdown-item">Profile of Board of Directors</a>
                        <a href="shareholders-information.html" class="dropdown-item" style="color: var(--primary); font-weight: 700;">Shareholder's Information</a>
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

    <!-- Page Header Banner (Compact Height) -->
    <section style="background: linear-gradient(135deg, #003318, #005a2b); padding: 2.25rem 0 2.5rem; color: #ffffff; text-align: center;">
        <div class="container">
            <span style="background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25); padding: 0.35rem 1rem; border-radius: var(--radius-full); font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #ffffff;">Investor Relations</span>
            <h1 style="font-size: 2.35rem; margin: 0.5rem 0 0.35rem; font-family: var(--font-heading); font-weight: 800; color: #ffffff !important; text-shadow: 0 2px 8px rgba(0,0,0,0.3);">Shareholder's Information</h1>
            <p style="font-size: 1rem; color: rgba(255,255,255,0.88); max-width: 720px; margin: 0 auto; line-height: 1.5;">Essential statutory information, share registrar contacts, statutory policies, dividend registers, and SECP regulatory compliance statements.</p>
        </div>
    </section>

    <!-- Quick Jump Navigation Pill Bar -->
    <div style="background-color: var(--bg-surface); border-bottom: 1px solid var(--border-color); padding: 1rem 0; position: sticky; top: 72px; z-index: 90; box-shadow: var(--shadow-sm);">
        <div class="container" style="display: flex; gap: 0.65rem; overflow-x: auto; scrollbar-width: none; -webkit-overflow-scrolling: touch;">
            <a href="#investor-contact" class="jump-pill">Investor Contact & Registrar</a>
            <a href="#unclaimed-dividends" class="jump-pill highlight">Unclaimed Dividends</a>
            <a href="#governance-policies" class="jump-pill highlight">Policies & Code of Conduct</a>
            <a href="#compliance-gender" class="jump-pill highlight">Compliance & Gender Pay Gap</a>
            <a href="#election-directors" class="jump-pill">Election of Directors</a>
            <a href="#stock-listing" class="jump-pill">Stock Exchange Listing</a>
            <a href="#advisors-bankers" class="jump-pill">Advisors & Bankers</a>
        </div>
    </div>

    <!-- Main Content Flow (All Sections Visible) -->
    <main style="padding: 2.5rem 0 4rem; background-color: var(--bg-main);">
        <div class="container" style="display: flex; flex-direction: column; gap: 3.5rem;">

            <!-- SECTION 1: Investor Contact & Share Registrar -->
            <section id="investor-contact">
                <div style="margin-bottom: 1.75rem;">
                    <h2 class="sh-section-title">1. Investor Contact & Share Registrar</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Direct contact channels for corporate secretarial assistance and share transfer inquiries.</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
                    
                    <!-- Company Secretary Card -->
                    <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2rem; box-shadow: var(--shadow-md);">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.25rem;">
                            <div style="width: 48px; height: 48px; border-radius: var(--radius-md); background: rgba(0, 90, 43, 0.1); color: var(--primary); display: flex; align-items: center; justify-content: center;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                            </div>
                            <div>
                                <span style="font-size: 0.8rem; font-weight: 700; color: var(--primary); text-transform: uppercase;">Corporate Office</span>
                                <h3 style="font-size: 1.35rem; color: var(--primary); font-weight: 800; margin: 0;">Company Secretary</h3>
                            </div>
                        </div>
                        <h4 style="font-size: 1.15rem; color: var(--text-main); font-weight: 700; margin-bottom: 0.75rem;">Mr. Asif Ali</h4>
                        <div style="display: flex; flex-direction: column; gap: 0.6rem; font-size: 0.95rem; color: var(--text-muted);">
                            <p style="margin: 0;"><strong style="color: var(--text-main);">Email:</strong> <a href="mailto:asif.ali@shakarganj.com.pk" style="color: var(--primary); font-weight: 600; text-decoration: none;">asif.ali@shakarganj.com.pk</a></p>
                            <p style="margin: 0;"><strong style="color: var(--text-main);">Telephone:</strong> +92 47 111 111 765</p>
                            <p style="margin: 0;"><strong style="color: var(--text-main);">Fax:</strong> +92 47 763 1011</p>
                        </div>
                    </div>

                    <!-- Share Registrar Card -->
                    <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2rem; box-shadow: var(--shadow-md);">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.25rem;">
                            <div style="width: 48px; height: 48px; border-radius: var(--radius-md); background: rgba(0, 90, 43, 0.1); color: var(--primary); display: flex; align-items: center; justify-content: center;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                            </div>
                            <div>
                                <span style="font-size: 0.8rem; font-weight: 700; color: var(--primary); text-transform: uppercase;">Share Transfer Agent</span>
                                <h3 style="font-size: 1.35rem; color: var(--primary); font-weight: 800; margin: 0;">Share Registrar</h3>
                            </div>
                        </div>
                        <h4 style="font-size: 1.15rem; color: var(--text-main); font-weight: 700; margin-bottom: 0.35rem;">M/s CorpTec Associates (Private) Limited</h4>
                        <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0.75rem;">503-E, Johar Town, Lahore, Pakistan</p>
                        <div style="display: flex; flex-direction: column; gap: 0.6rem; font-size: 0.95rem; color: var(--text-muted);">
                            <p style="margin: 0;"><strong style="color: var(--text-main);">Email:</strong> <a href="mailto:info@corptec.com.pk" style="color: var(--primary); font-weight: 600; text-decoration: none;">info@corptec.com.pk</a></p>
                            <p style="margin: 0;"><strong style="color: var(--text-main);">Telephone:</strong> +92 42 3517 0336 – 37</p>
                            <p style="margin: 0;"><strong style="color: var(--text-main);">Fax:</strong> +92 42 3517 0338</p>
                        </div>
                    </div>

                </div>

                <!-- SECP Investor Complaint Section -->
                <div style="background: linear-gradient(135deg, var(--bg-surface), var(--bg-alt)); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2.25rem; box-shadow: var(--shadow-md);">
                    <div style="display: flex; align-items: center; justify-content: space-between; gap: 2rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
                        <div style="display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap;">
                            <img src="/images/secp2021.png" alt="SECP Investor Complaints Portal" style="max-height: 55px; width: auto; background: #ffffff; padding: 6px 14px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
                            <div>
                                <h3 style="font-size: 1.35rem; color: var(--primary); font-weight: 800; margin-bottom: 0.25rem;">SECP Investor Complaint Portal (SDMS)</h3>
                                <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0;">Securities and Exchange Commission of Pakistan Service Desk Management System</p>
                            </div>
                        </div>
                        <a href="https://sdms.secp.gov.pk/" target="_blank" rel="noopener noreferrer" style="background: var(--primary); color: #ffffff; text-decoration: none; padding: 0.75rem 1.5rem; border-radius: var(--radius-full); font-weight: 700; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 4px 12px rgba(0, 90, 43, 0.25);">
                            Lodge Complaint at SECP Portal <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                        </a>
                    </div>
                    <div style="background: rgba(0, 90, 43, 0.05); border-left: 4px solid var(--primary); padding: 1.25rem 1.5rem; border-radius: 0 var(--radius-md) var(--radius-md) 0; font-size: 0.925rem; color: var(--text-main); line-height: 1.6;">
                        <strong>SECP Redressal Disclaimer:</strong> In case your complaint has not been properly redressed by us, you may lodge your complaint with the Securities and Exchange Commission of Pakistan (the “SECP”). Please note that SECP will entertain only those complaints which were at first directly requested to be redressed by the company and the company has failed to redress the same.
                    </div>
                </div>
            </section>

            <!-- SECTION 2: Unclaimed Dividends -->
            <section id="unclaimed-dividends">
                <div style="margin-bottom: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.35rem;">
                        <span class="section-badge">Statutory Dividend Record</span>
                        <h2 class="sh-section-title" style="margin: 0;">2. Unclaimed Dividends</h2>
                    </div>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Detail of unpaid and unclaimed dividend accounts maintained as per Section 244 of the Companies Act, 2017.</p>
                </div>

                <div class="statutory-hero-card">
                    <div style="display: flex; align-items: flex-start; gap: 1.5rem; flex-wrap: wrap;">
                        <div class="doc-icon-box-large">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                        </div>
                        <div style="flex: 1; min-width: 260px;">
                            <h3 style="font-size: 1.35rem; color: var(--primary); font-weight: 800; margin-bottom: 0.5rem;">Detail of Pending / Unclaimed Dividend 2023</h3>
                            <p style="color: var(--text-muted); font-size: 0.975rem; line-height: 1.6; margin-bottom: 1.25rem;">Shareholders are requested to inspect the official register of pending and unclaimed dividend payments to claim outstanding warrants. For assistance in revalidation, contact our Share Registrar M/s CorpTec Associates.</p>
                            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                                <a href="/docs/shareholder/Detail-of-Pending-Dividend-2023.pdf" target="_blank" class="action-btn-primary">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Download Unclaimed Dividend PDF (2023)
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SECTION 3: Governance Policies & Code of Conduct -->
            <section id="governance-policies">
                <div style="margin-bottom: 1.5rem;">
                    <h2 class="sh-section-title">3. Governance Policies & Code of Conduct</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Official ethical standards, director obligations, and corporate policies register approved by the Board.</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
                    
                    <!-- Code of Conduct Card -->
                    <div class="statutory-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box-md">PDF</div>
                            <div>
                                <h3 style="font-size: 1.25rem; color: var(--primary); font-weight: 800; margin: 0;">Code of Conduct</h3>
                                <span style="font-size: 0.8rem; color: var(--text-muted);">Ethical & Professional Standards</span>
                            </div>
                        </div>
                        <p style="color: var(--text-muted); font-size: 0.925rem; line-height: 1.55; margin-bottom: 1.5rem;">Comprehensive principles governing ethical behavior, insider trading prohibitions, conflict of interest management, and director compliance.</p>
                        <a href="/docs/shareholder/Code-of-Conduct.pdf" target="_blank" class="action-btn-outline">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Download Code of Conduct PDF
                        </a>
                    </div>

                    <!-- Policies Register Card -->
                    <div class="statutory-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box-md">PDF</div>
                            <div>
                                <h3 style="font-size: 1.25rem; color: var(--primary); font-weight: 800; margin: 0;">Policies Register</h3>
                                <span style="font-size: 0.8rem; color: var(--text-muted);">Board Approved Framework</span>
                            </div>
                        </div>
                        <p style="color: var(--text-muted); font-size: 0.925rem; line-height: 1.55; margin-bottom: 1.5rem;">Master register of corporate governance policies including risk management, whistleblowing, whistleblower protection, and audit oversight.</p>
                        <a href="/docs/shareholder/Policies-Register.pdf" target="_blank" class="action-btn-outline">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Download Policies Register PDF
                        </a>
                    </div>

                </div>
            </section>

            <!-- SECTION 4: Compliance Certificate & Gender Pay Gap Statement -->
            <section id="compliance-gender">
                <div style="margin-bottom: 1.5rem;">
                    <h2 class="sh-section-title">4. Compliance Certificate & Circular Declarations</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">SECP website compliance certification and mandatory circular disclosure statements.</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
                    
                    <!-- Website Compliance Certificate -->
                    <div class="statutory-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box-md" style="background: rgba(0, 90, 43, 0.1); color: var(--primary);">CERT</div>
                            <div>
                                <h3 style="font-size: 1.2rem; color: var(--primary); font-weight: 800; margin: 0;">Website Compliance Certificate</h3>
                                <span style="font-size: 0.8rem; color: var(--text-muted);">SECP Regulatory Certification (Sep 2025)</span>
                            </div>
                        </div>
                        <p style="color: var(--text-muted); font-size: 0.925rem; line-height: 1.55; margin-bottom: 1.5rem;">Official certification attesting full compliance of Shakarganj Limited web portal with SECP statutory requirements under SRO 634(I)/2014.</p>
                        <a href="/docs/shareholder/Website_Compliance_Certificate_Sep_2025.pdf" target="_blank" class="action-btn-outline">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Download Compliance Certificate PDF
                        </a>
                    </div>

                    <!-- Gender Pay Gap Statement -->
                    <div class="statutory-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box-md" style="background: rgba(0, 90, 43, 0.1); color: var(--primary);">SECP</div>
                            <div>
                                <h3 style="font-size: 1.2rem; color: var(--primary); font-weight: 800; margin: 0;">Gender Pay Gap Statement</h3>
                                <span style="font-size: 0.8rem; color: var(--text-muted);">Under SECP Circular 10 of 2024</span>
                            </div>
                        </div>
                        <p style="color: var(--text-muted); font-size: 0.925rem; line-height: 1.55; margin-bottom: 1.5rem;">Mandatory disclosure under SECP Circular No. 10 of 2024 highlighting equal remuneration commitment, gender diversity, and wage equity metrics.</p>
                        <a href="/docs/shareholder/Gende_Pay_Gap_Statement_2025.pdf" target="_blank" class="action-btn-outline">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Download Gender Pay Gap Statement PDF
                        </a>
                    </div>

                </div>
            </section>

            <!-- SECTION 5: Election of Directors 2026 -->
            <section id="election-directors">
                <div style="margin-bottom: 1.75rem;">
                    <h2 class="sh-section-title">5. Election of Directors 2026</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Statutory notices, candidate profiles, proxy forms, voter lists, and scrutinizer reports for the 2026 Board Election held on 01 June 2026.</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem;">
                    
                    <!-- Notice u/s 159(4) -->
                    <div class="doc-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box">PDF</div>
                            <div>
                                <h4 class="doc-title">Notice u/s 159(4) of Companies Act 2017</h4>
                                <span class="doc-meta">Statutory Publication</span>
                            </div>
                        </div>
                        <div class="doc-btn-group">
                            <a href="/docs/shareholder/Notice-159-english-2026.pdf" target="_blank" class="doc-btn primary">English PDF</a>
                            <a href="/docs/shareholder/Notice-159-Urdu-2026.pdf" target="_blank" class="doc-btn outline">Urdu PDF</a>
                        </div>
                    </div>

                    <!-- Notice of EOGM -->
                    <div class="doc-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box">PDF</div>
                            <div>
                                <h4 class="doc-title">Notice of Extraordinary General Meeting</h4>
                                <span class="doc-meta">EOGM Notice 2026</span>
                            </div>
                        </div>
                        <div class="doc-btn-group">
                            <a href="/docs/shareholder/eogm-2026-e.pdf" target="_blank" class="doc-btn primary">English PDF</a>
                            <a href="/docs/shareholder/eogm-2026-u.pdf" target="_blank" class="doc-btn outline">Urdu PDF</a>
                        </div>
                    </div>

                    <!-- Form of Proxy -->
                    <div class="doc-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box">PDF</div>
                            <div>
                                <h4 class="doc-title">Form of Proxy</h4>
                                <span class="doc-meta">Voting Authorization Form</span>
                            </div>
                        </div>
                        <div class="doc-btn-group">
                            <a href="/docs/shareholder/eogm-proxy-2026-e.pdf" target="_blank" class="doc-btn primary">English Proxy</a>
                            <a href="/docs/shareholder/eogm-proxy-2026-u.pdf" target="_blank" class="doc-btn outline">Urdu Proxy</a>
                        </div>
                    </div>

                    <!-- Profiles of Candidates -->
                    <div class="doc-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box" style="background: rgba(0,90,43,0.15); color: var(--primary);">WEB</div>
                            <div>
                                <h4 class="doc-title">Profiles of Candidates</h4>
                                <span class="doc-meta">Board of Directors Profiles</span>
                            </div>
                        </div>
                        <div class="doc-btn-group">
                            <a href="board-of-directors.html" class="doc-btn primary" style="grid-column: span 2;">View Profiles & Governance</a>
                        </div>
                    </div>

                    <!-- List of Shareholders -->
                    <div class="doc-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box">PDF</div>
                            <div>
                                <h4 class="doc-title">List of Shareholders for EOGM</h4>
                                <span class="doc-meta">Contact Secretary for Login Details</span>
                            </div>
                        </div>
                        <div class="doc-btn-group">
                            <a href="/docs/shareholder/List-of-Shareholders-for-EOGM.pdf" target="_blank" class="doc-btn primary" style="grid-column: span 2;">Download Shareholders List</a>
                        </div>
                    </div>

                    <!-- Election Results 2026 -->
                    <div class="doc-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box">PDF</div>
                            <div>
                                <h4 class="doc-title">Election Results 2026</h4>
                                <span class="doc-meta">Official Voting Results</span>
                            </div>
                        </div>
                        <div class="doc-btn-group">
                            <a href="/docs/shareholder/results2026.pdf" target="_blank" class="doc-btn primary" style="grid-column: span 2;">View Official Results PDF</a>
                        </div>
                    </div>

                    <!-- Report of Scrutinizer -->
                    <div class="doc-card">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div class="doc-icon-box">PDF</div>
                            <div>
                                <h4 class="doc-title">Report of Scrutinizer 2026</h4>
                                <span class="doc-meta">Independent Audit & Scrutiny</span>
                            </div>
                        </div>
                        <div class="doc-btn-group">
                            <a href="/docs/shareholder/Report-of-Scrutinizer-2026.pdf" target="_blank" class="doc-btn primary" style="grid-column: span 2;">Download Scrutinizer Report</a>
                        </div>
                    </div>

                </div>
            </section>

            <!-- SECTION 6: Stock Exchange Listing -->
            <section id="stock-listing">
                <div style="margin-bottom: 1.75rem;">
                    <h2 class="sh-section-title">6. Stock Exchange Listing</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Traded on the Pakistan Stock Exchange (PSX) under symbol SML in Sugar & Allied Industries.</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
                    <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2rem; box-shadow: var(--shadow-md);">
                        <h3 style="font-size: 1.35rem; color: var(--primary); font-weight: 800; margin-bottom: 1rem;">Pakistan Stock Exchange (PSX)</h3>
                        <p style="color: var(--text-muted); font-size: 0.975rem; line-height: 1.6; margin-bottom: 1.5rem;">Shakarganj Limited is a listed public limited company. Daily equity stock quotes are published across leading financial newspapers and digital stock portals under 'Sugar & Allied Industries'.</p>
                        <div style="background: var(--bg-alt); padding: 1.25rem; border-radius: var(--radius-md); margin-bottom: 1.5rem; border: 1px solid var(--border-color);">
                            <p style="margin: 0 0 0.5rem; font-size: 0.9rem; color: var(--text-muted);">Trading Symbol:</p>
                            <p style="margin: 0; font-size: 1.75rem; font-weight: 800; color: var(--primary); font-family: var(--font-heading);">SML</p>
                        </div>
                        <a href="https://dps.psx.com.pk/company/SML" target="_blank" rel="noopener noreferrer" style="background: var(--primary); color: #ffffff; text-decoration: none; padding: 0.75rem 1.5rem; border-radius: var(--radius-full); font-weight: 700; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 0.5rem;">
                            View SML on PSX Data Portal <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                        </a>
                    </div>

                    <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2rem; box-shadow: var(--shadow-md);">
                        <h3 style="font-size: 1.35rem; color: var(--primary); font-weight: 800; margin-bottom: 1rem;">Stock Analytics & Screening</h3>
                        <p style="color: var(--text-muted); font-size: 0.975rem; line-height: 1.6; margin-bottom: 1.5rem;">Access fundamental financial performance, historical stock performance, volume data, and equity snapshots for Shakarganj Limited.</p>
                        <div style="display: flex; flex-direction: column; gap: 1rem;">
                            <a href="http://www.scstrade.com/StockScreening/SS_CompanySnapShot.aspx?symbol=SML" target="_blank" rel="noopener noreferrer" style="background: var(--bg-alt); color: var(--primary); border: 1px solid var(--border-color); text-decoration: none; padding: 0.85rem 1.25rem; border-radius: var(--radius-md); font-weight: 700; font-size: 0.9rem; display: flex; align-items: center; justify-content: space-between;">
                                SCS Trade Company Snapshot <span>→</span>
                            </a>
                            <a href="investors.html#financial-highlights" style="background: var(--bg-alt); color: var(--primary); border: 1px solid var(--border-color); text-decoration: none; padding: 0.85rem 1.25rem; border-radius: var(--radius-md); font-weight: 700; font-size: 0.9rem; display: flex; align-items: center; justify-content: space-between;">
                                SML Financial Highlights Vault <span>→</span>
                            </a>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SECTION 7: Advisors & Bankers -->
            <section id="advisors-bankers">
                <div style="margin-bottom: 1.75rem;">
                    <h2 class="sh-section-title">7. Advisors & Bankers</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem;">Statutory auditors, legal counsel, banking partners, and financial literacy initiatives.</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
                    
                    <!-- Statutory Auditors -->
                    <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 1.75rem; box-shadow: var(--shadow-md);">
                        <span style="font-size: 0.8rem; font-weight: 700; color: var(--primary); text-transform: uppercase;">External Audit</span>
                        <h3 style="font-size: 1.25rem; color: var(--primary); font-weight: 800; margin: 0.35rem 0 0.75rem;">Auditors</h3>
                        <p style="font-size: 1rem; color: var(--text-main); font-weight: 700; margin: 0;">M/s. Kreston Hyder Bhimji & Co.</p>
                        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">Chartered Accountants</p>
                    </div>

                    <!-- Legal Advisors -->
                    <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 1.75rem; box-shadow: var(--shadow-md);">
                        <span style="font-size: 0.8rem; font-weight: 700; color: var(--primary); text-transform: uppercase;">Legal Counsel</span>
                        <h3 style="font-size: 1.25rem; color: var(--primary); font-weight: 800; margin: 0.35rem 0 0.75rem;">Legal Advisors</h3>
                        <p style="font-size: 0.95rem; color: var(--text-main); font-weight: 700; margin: 0 0 0.35rem;">Masud & Mirza Associates</p>
                        <p style="font-size: 0.95rem; color: var(--text-main); font-weight: 700; margin: 0;">Siddiqui Bari Kasuri & Co.</p>
                    </div>

                    <!-- Bankers -->
                    <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 1.75rem; box-shadow: var(--shadow-md);">
                        <span style="font-size: 0.8rem; font-weight: 700; color: var(--primary); text-transform: uppercase;">Financial Partners</span>
                        <h3 style="font-size: 1.25rem; color: var(--primary); font-weight: 800; margin: 0.35rem 0 0.75rem;">Bankers</h3>
                        <p style="font-size: 0.95rem; color: var(--text-main); font-weight: 700; margin: 0 0 0.35rem;">MCB Bank Limited</p>
                        <p style="font-size: 0.95rem; color: var(--text-main); font-weight: 700; margin: 0;">National Bank of Pakistan</p>
                    </div>

                </div>

                <!-- SECP JamaPunji Portal Card -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 2rem; box-shadow: var(--shadow-md); display: flex; align-items: center; justify-content: space-between; gap: 2rem; flex-wrap: wrap;">
                    <div style="display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap;">
                        <img src="/images/jama-punji.png" alt="SECP JamaPunji Financial Literacy Portal" style="max-height: 55px; width: auto; background: #ffffff; padding: 6px 12px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
                        <div>
                            <h3 style="font-size: 1.3rem; color: var(--primary); font-weight: 800; margin-bottom: 0.25rem;">SECP JamaPunji Financial Literacy Initiative</h3>
                            <p style="font-size: 0.925rem; color: var(--text-muted); margin: 0;">Promoting investor awareness, financial education, and capital market safety in Pakistan.</p>
                        </div>
                    </div>
                    <a href="http://www.jamapunji.pk/" target="_blank" rel="noopener noreferrer" style="background: var(--primary); color: #ffffff; text-decoration: none; padding: 0.75rem 1.5rem; border-radius: var(--radius-full); font-weight: 700; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 0.5rem;">
                        Visit JamaPunji Portal <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                    </a>
                </div>
            </section>

        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-content">
            <div class="footer-bottom">
                <p>&copy; 2026 Shakarganj Limited. All Rights Reserved.</p>
                <div class="legal-links"><a href="index.html">Home</a> | <a href="contact.html">Contact Us</a></div>
            </div>
        </div>
    </footer>

    <style>
        .sh-section-title {
            font-size: 2rem !important;
            color: var(--primary) !important;
            font-weight: 800 !important;
        }
        .jump-pill {
            background-color: var(--bg-alt);
            color: var(--text-main);
            border: 1px solid var(--border-color);
            padding: 0.45rem 1rem;
            border-radius: var(--radius-full);
            font-size: 0.85rem;
            font-weight: 700;
            text-decoration: none;
            white-space: nowrap;
            transition: all 150ms ease;
        }
        .jump-pill:hover {
            background-color: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }
        .jump-pill.highlight {
            border-color: var(--primary);
            color: var(--primary);
            background-color: rgba(0, 90, 43, 0.06);
        }
        .section-badge {
            background: rgba(0, 90, 43, 0.1);
            color: var(--primary);
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 800;
            text-transform: uppercase;
        }
        .statutory-hero-card {
            background: var(--bg-surface);
            border: 1.5px solid var(--primary-light);
            border-radius: var(--radius-xl);
            padding: 2.25rem;
            box-shadow: var(--shadow-md);
        }
        .doc-icon-box-large {
            width: 58px;
            height: 58px;
            border-radius: var(--radius-lg);
            background: rgba(0, 90, 43, 0.1);
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .action-btn-primary {
            background-color: var(--primary);
            color: #ffffff;
            text-decoration: none;
            padding: 0.75rem 1.35rem;
            border-radius: var(--radius-md);
            font-weight: 700;
            font-size: 0.9rem;
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            transition: background 150ms ease;
            box-shadow: 0 4px 12px rgba(0, 90, 43, 0.2);
        }
        .action-btn-primary:hover {
            background-color: var(--primary-dark);
        }
        .statutory-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            padding: 1.85rem;
            box-shadow: var(--shadow-md);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .doc-icon-box-md {
            width: 46px;
            height: 46px;
            border-radius: var(--radius-md);
            background: rgba(220, 38, 38, 0.1);
            color: #dc2626;
            font-weight: 800;
            font-size: 0.75rem;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .action-btn-outline {
            background-color: var(--bg-alt);
            color: var(--primary);
            border: 1px solid var(--border-color);
            text-decoration: none;
            padding: 0.65rem 1.15rem;
            border-radius: var(--radius-md);
            font-weight: 700;
            font-size: 0.875rem;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 150ms ease;
        }
        .action-btn-outline:hover {
            border-color: var(--primary);
            background-color: rgba(0, 90, 43, 0.08);
        }
        .doc-card {
            background: var(--bg-surface) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: var(--radius-lg) !important;
            padding: 1.5rem !important;
            box-shadow: var(--shadow-sm) !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
        }
        .doc-icon-box {
            width: 44px !important;
            height: 44px !important;
            border-radius: var(--radius-md) !important;
            background: rgba(220, 38, 38, 0.1) !important;
            color: #dc2626 !important;
            font-weight: 800 !important;
            font-size: 0.75rem !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            flex-shrink: 0 !important;
        }
        .doc-title {
            font-size: 1.05rem !important;
            color: var(--text-main) !important;
            font-weight: 700 !important;
            margin: 0 0 0.2rem 0 !important;
            line-height: 1.35 !important;
        }
        .doc-meta {
            font-size: 0.8rem !important;
            color: var(--text-muted) !important;
            display: block !important;
        }
        .doc-btn-group {
            display: grid !important;
            grid-template-columns: 1fr 1fr !important;
            gap: 0.75rem !important;
            margin-top: 1rem !important;
        }
        .doc-btn {
            text-decoration: none !important;
            padding: 0.55rem 0.85rem !important;
            border-radius: var(--radius-md) !important;
            font-size: 0.825rem !important;
            font-weight: 700 !important;
            text-align: center !important;
            transition: all 150ms ease !important;
        }
        .doc-btn.primary {
            background-color: var(--primary) !important;
            color: #ffffff !important;
        }
        .doc-btn.primary:hover {
            background-color: var(--primary-dark) !important;
        }
        .doc-btn.outline {
            background-color: var(--bg-alt) !important;
            color: var(--primary) !important;
            border: 1px solid var(--border-color) !important;
        }
        .doc-btn.outline:hover {
            border-color: var(--primary) !important;
            background-color: rgba(0, 90, 43, 0.05) !important;
        }
    </style>

    <script src="main.js"></script>
</body>
</html>"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\shareholders-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\shareholders-information.html'
]

for t in targets:
    with open(t, 'w', encoding='utf-8') as f:
        f.write(shareholder_info_html)

print("Updated shareholders-information page so ALL 5 statutory sections are prominently visible in the main flow!")
