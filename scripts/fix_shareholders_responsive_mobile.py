import glob

responsive_css = """
/* ==========================================================================
   Comprehensive Mobile & Tablet Responsive Media Queries for Shareholder's Info
   ========================================================================== */

/* Tablet Screens (max-width: 992px) */
@media (max-width: 992px) {
    main .container {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
    }
    
    .sh-sidebar {
        position: relative !important;
        top: 0 !important;
        margin-bottom: 1rem !important;
    }

    .sh-sidebar-card {
        padding: 1rem !important;
    }

    .sh-side-nav {
        flex-direction: row !important;
        overflow-x: auto !important;
        scroll-behavior: smooth !important;
        -webkit-overflow-scrolling: touch !important;
        padding-bottom: 0.5rem !important;
    }

    .side-nav-item {
        white-space: nowrap !important;
        flex-shrink: 0 !important;
        padding: 0.5rem 0.75rem !important;
        font-size: 0.825rem !important;
    }
}

/* Mobile Screens (max-width: 768px) */
@media (max-width: 768px) {
    .sh-section-card {
        padding: 1.25rem 1rem !important;
        border-radius: var(--radius-lg) !important;
    }

    .sh-section-header {
        gap: 0.85rem !important;
        margin-bottom: 1.25rem !important;
        padding-bottom: 1rem !important;
    }

    .sh-section-badge {
        width: 36px !important;
        height: 36px !important;
        font-size: 0.95rem !important;
    }

    .sh-section-title {
        font-size: 1.35rem !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.3 !important;
    }

    .sh-section-desc {
        font-size: 0.875rem !important;
    }

    /* SECP Complaint Portal Box Mobile Stacking */
    .secp-portal-box {
        padding: 1.15rem 1rem !important;
    }

    .secp-portal-box > div:first-child {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 1rem !important;
    }

    .secp-portal-box img {
        max-height: 42px !important;
    }

    .secp-portal-box h3 {
        font-size: 1.15rem !important;
        word-break: break-word !important;
    }

    .btn-primary-pill, .btn-primary-action, .btn-outline-action {
        width: 100% !important;
        justify-content: center !important;
        box-sizing: border-box !important;
        font-size: 0.85rem !important;
        padding: 0.7rem 1rem !important;
    }

    /* Election Cards Mobile Layout */
    .election-item-card {
        padding: 1rem !important;
    }

    .election-btn-row {
        grid-template-columns: 1fr !important;
        gap: 0.5rem !important;
    }

    .mini-btn-primary, .mini-btn-outline {
        width: 100% !important;
        grid-column: span 1 !important;
    }

    /* Info & Policy Cards Padding */
    .info-box-card, .policy-card, .statutory-hero-box {
        padding: 1.15rem 1rem !important;
    }

    .info-box-title, .policy-card-title {
        font-size: 1.1rem !important;
        word-break: break-word !important;
    }
}

/* Small Mobile Screens (max-width: 480px) */
@media (max-width: 480px) {
    .sh-section-title {
        font-size: 1.2rem !important;
    }
    
    .sh-section-header {
        flex-direction: column !important;
        align-items: flex-start !important;
    }

    .info-detail-list p {
        word-break: break-word !important;
        font-size: 0.875rem !important;
    }
}
"""

targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\shareholders-information.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\shareholders-information.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\shareholders-information.html'
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    if '/* Comprehensive Mobile & Tablet Responsive Media Queries for Shareholder\'s Info */' not in content:
        # Inject before </style>
        content = content.replace('</style>', responsive_css + '\n    </style>')
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)

print("Injected responsive mobile CSS media queries across all shareholder-information files!")
