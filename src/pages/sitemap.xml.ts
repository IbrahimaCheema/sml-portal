import type { APIRoute } from 'astro';

const SITE_URL = 'https://www.sml.com.pk';

const pages = [
  { url: '', priority: '1.0', changefreq: 'daily' },
  { url: '/company-profile', priority: '0.9', changefreq: 'weekly' },
  { url: '/sugar', priority: '0.9', changefreq: 'weekly' },
  { url: '/biofuels', priority: '0.9', changefreq: 'weekly' },
  { url: '/shareholder-information', priority: '0.9', changefreq: 'weekly' },
  { url: '/contact-us', priority: '0.9', changefreq: 'monthly' },
  { url: '/company-history', priority: '0.8', changefreq: 'monthly' },
  { url: '/board-of-directors', priority: '0.8', changefreq: 'monthly' },
  { url: '/financial-reports', priority: '0.8', changefreq: 'weekly' },
  { url: '/certifications', priority: '0.8', changefreq: 'monthly' },
  { url: '/careers', priority: '0.8', changefreq: 'weekly' },
  { url: '/associated-companies', priority: '0.7', changefreq: 'monthly' },
  { url: '/corporate-social-responsibility', priority: '0.7', changefreq: 'monthly' },
  { url: '/health-safety-environment', priority: '0.7', changefreq: 'monthly' },
  { url: '/awards-and-accolades', priority: '0.7', changefreq: 'monthly' },
  { url: '/quality-assurance', priority: '0.7', changefreq: 'monthly' },
  { url: '/historical-reports', priority: '0.7', changefreq: 'monthly' },
  { url: '/shareholding-pattern', priority: '0.7', changefreq: 'monthly' },
  { url: '/free-float-of-the-shares', priority: '0.7', changefreq: 'monthly' },
  { url: '/corporate-strategy', priority: '0.7', changefreq: 'monthly' },
  { url: '/mission-and-vision', priority: '0.7', changefreq: 'monthly' },
  { url: '/corporate-briefing-session', priority: '0.7', changefreq: 'monthly' },
  { url: '/blog', priority: '0.7', changefreq: 'weekly' },
  { url: '/sitemap', priority: '0.5', changefreq: 'monthly' }
];

export const GET: APIRoute = async () => {
  const lastmod = new Date().toISOString().split('T')[0];

  const xmlContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
${pages
  .map(
    (page) => `  <url>
    <loc>${SITE_URL}${page.url}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${page.priority}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(xmlContent, {
    status: 200,
    headers: {
      'Content-Type': 'application/xml; charset=utf-8'
    }
  });
};
