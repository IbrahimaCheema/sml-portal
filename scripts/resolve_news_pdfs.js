import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

const ACCOUNT_ID = '9594508e0e41ab8192d129114cd8a539';
const ACCESS_KEY_ID = 'aab38b2efd2c96025f8815869503c4bc';
const SECRET_ACCESS_KEY = '3248746e1537c3372c9c04714c5680a2b678630c58516000fd306f9e04941d41';
const BUCKET_NAME = 'sml-uploads';
const PUBLIC_DOMAIN = 'https://docs.sml.com.pk';

const r2Client = new S3Client({
  region: 'auto',
  endpoint: `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: ACCESS_KEY_ID,
    secretAccessKey: SECRET_ACCESS_KEY,
  },
  forcePathStyle: true,
});

// Mapping of posts to their WordPress URLs & R2 PDF filenames
const postsToScrape = [
  {
    id: 'financial-results-half-year-31-mar-2026',
    wpUrl: 'https://www.sml.com.pk/financial-results-for-the-half-year-ended-31-mar-2026/',
    r2PdfName: 'SML-2026.03.31-Q2.pdf'
  },
  {
    id: 'notice-extraordinary-general-meeting-may-2026',
    wpUrl: 'https://www.sml.com.pk/notice-of-extraordinary-general-meeting-3/',
    r2PdfName: 'SML-EGM-Notice-2026.pdf'
  },
  {
    id: 'corporate-briefing-session-2025',
    wpUrl: 'https://www.sml.com.pk/corporate-briefing-session-2025/',
    r2PdfName: 'SML-Corporate-Briefing-2025.pdf'
  },
  {
    id: 'quarterly-report-31-december-2025',
    wpUrl: 'https://www.sml.com.pk/quarterly-report-for-the-period-ended-31-december-2025/',
    r2PdfName: 'SML-2025.12.31-Q1.pdf'
  },
  {
    id: 'notice-board-meeting-feb-2026',
    wpUrl: 'https://www.sml.com.pk/notice-of-board-of-directors-meeting-11/',
    r2PdfName: 'SML-Board-Meeting-Notice-Feb-2026.pdf'
  },
  {
    id: 'annual-report-30-september-2025',
    wpUrl: 'https://www.sml.com.pk/annual-report-for-the-year-ended-30-september-2025/',
    r2PdfName: 'SML-2025-Annual-Report.pdf'
  },
  {
    id: 'notice-annual-general-meeting-jan-2026',
    wpUrl: 'https://www.sml.com.pk/notice-of-annual-general-meeting-6/',
    r2PdfName: 'SML-AGM-Notice-2026.pdf'
  },
  {
    id: 'financial-results-3rd-quarter-30-june-2025',
    wpUrl: 'https://www.sml.com.pk/financial-results-for-the-3rd-quarter-ended-30-june-2025/',
    r2PdfName: 'SML-2025.06.30-Q3.pdf'
  },
  {
    id: 'notice-board-meeting-july-2025',
    wpUrl: 'https://www.sml.com.pk/notice-of-board-of-directors-meeting-10/',
    r2PdfName: 'SML-Board-Meeting-Notice-July-2025.pdf'
  },
  {
    id: 'financial-results-half-year-31-mar-2025',
    wpUrl: 'https://www.sml.com.pk/financial-results-for-the-half-year-ended-31-mar-2025/',
    r2PdfName: 'SML-2025.03.31-Q2.pdf'
  },
  {
    id: 'notice-board-meeting-may-2025',
    wpUrl: 'https://www.sml.com.pk/notice-of-board-of-directors-meeting-9/',
    r2PdfName: 'SML-Board-Meeting-Notice-May-2025.pdf'
  },
  {
    id: 'corporate-briefing-session-2024',
    wpUrl: 'https://www.sml.com.pk/corporate-briefing-session-2024/',
    r2PdfName: 'SML-Corporate-Briefing-2024.pdf'
  },
  {
    id: 'quarterly-report-31-december-2024',
    wpUrl: 'https://www.sml.com.pk/quarterly-report-for-the-period-ended-31-december-2024/',
    r2PdfName: 'SML-2024.12.31-Q1.pdf'
  },
  {
    id: 'annual-report-30-september-2024',
    wpUrl: 'https://www.sml.com.pk/annual-report-for-the-year-ended-30-september-2024/',
    r2PdfName: 'SML-2024-Annual-Report.pdf'
  },
  {
    id: 'notice-annual-general-meeting-jan-2025',
    wpUrl: 'https://www.sml.com.pk/notice-of-annual-general-meeting-4/',
    r2PdfName: 'SML-AGM-Notice-2025.pdf'
  },
  {
    id: 'financial-results-3rd-quarter-30-june-2024',
    wpUrl: 'https://www.sml.com.pk/financial-results-for-the-3rd-quarter-ended-30-june-2024/',
    r2PdfName: 'SML-2024.06.30-Q3.pdf'
  },
  {
    id: 'financial-results-half-year-31-mar-2024',
    wpUrl: 'https://www.sml.com.pk/financial-results-for-the-half-year-ended-31-mar-2024/',
    r2PdfName: 'SML-2024.03.31-Q2.pdf'
  },
  {
    id: 'corporate-briefing-session-fy-2023',
    wpUrl: 'https://www.sml.com.pk/corporate-briefing-session-fy-2023/',
    r2PdfName: 'SML-Corporate-Briefing-2023.pdf'
  },
  {
    id: 'quarterly-report-31-december-2023',
    wpUrl: 'https://www.sml.com.pk/quarterly-report-for-the-period-ended-31-december-2023/',
    r2PdfName: 'SML-2023.12.31-Q1.pdf'
  },
  {
    id: 'annual-report-30-september-2023',
    wpUrl: 'https://www.sml.com.pk/annual-report-for-the-year-ended-30-september-2023/',
    r2PdfName: 'SML-2023-Annual-Report.pdf'
  }
];

function fetchHtml(url) {
  try {
    const html = execSync(`curl.exe -k -s "${url}"`).toString('utf-8');
    return html;
  } catch (e) {
    return '';
  }
}

function extractPdfUrl(html) {
  // Regex to match href="..." ending with .pdf or containing download/document
  const pdfMatch = html.match(/href=["'](https?:[^"']+\.pdf.*?)["']/i) || 
                   html.match(/href=["'](https?:\/\/(?:dps\.psx\.com\.pk|www\.sml\.com\.pk)[^"']+)["']/i);
  if (pdfMatch && pdfMatch[1]) {
    return pdfMatch[1];
  }
  return null;
}

function downloadPdf(pdfUrl, destPath) {
  console.log(`  Downloading PDF from: ${pdfUrl}`);
  execSync(`curl.exe -k -s "${pdfUrl}" -o "${destPath}"`);
}

async function run() {
  const tempDir = path.resolve('temp_news_pdfs');
  if (!fs.existsSync(tempDir)) fs.mkdirSync(tempDir, { recursive: true });

  const newsTsPath = path.resolve('src/data/newsPosts.ts');
  const newsPostsModule = await import('../src/data/newsPosts.ts');
  const posts = newsPostsModule.newsPosts;

  const pdfMap = new Map();

  for (const item of postsToScrape) {
    console.log(`Processing post: ${item.id} ...`);
    const html = fetchHtml(item.wpUrl);
    const pdfUrl = extractPdfUrl(html);
    if (pdfUrl) {
      console.log(`  Found PDF URL: ${pdfUrl}`);
      const localPdf = path.join(tempDir, item.r2PdfName);
      try {
        downloadPdf(pdfUrl, localPdf);
        if (fs.existsSync(localPdf) && fs.statSync(localPdf).size > 1000) {
          console.log(`  Uploading ${item.r2PdfName} to R2 (docs/${item.r2PdfName})...`);
          const pdfBuffer = fs.readFileSync(localPdf);
          await r2Client.send(new PutObjectCommand({
            Bucket: BUCKET_NAME,
            Key: `docs/${item.r2PdfName}`,
            Body: pdfBuffer,
            ContentType: 'application/pdf'
          }));
          const r2PdfUrl = `${PUBLIC_DOMAIN}/docs/${item.r2PdfName}`;
          pdfMap.set(item.id, r2PdfUrl);
          console.log(`  ✓ Successfully uploaded: ${r2PdfUrl}`);
        } else {
          console.log(`  File size too small or missing for ${item.id}`);
        }
      } catch (err) {
        console.error(`  Failed to download/upload PDF for ${item.id}:`, err.message);
      }
    } else {
      console.log(`  No PDF link found on page for ${item.id}`);
    }
  }

  // Update posts dataset
  const updatedPosts = posts.map(p => {
    if (pdfMap.has(p.id)) {
      return {
        ...p,
        pdfUrl: pdfMap.get(p.id)
      };
    }
    return p;
  });

  const tsContent = `// Auto-generated news posts dataset for Shakarganj Limited (2024 - 2026)
export interface NewsPost {
  id: string;
  title: string;
  date: string;
  displayDate: string;
  category: 'Financial Results' | 'Shareholder Notice' | 'Corporate Notice' | 'Investor Relations' | 'Company Updates';
  excerpt: string;
  featuredImage: string;
  linkUrl: string;
  pdfUrl?: string | null;
}

export const newsPosts: NewsPost[] = ${JSON.stringify(updatedPosts, null, 2)};
`;

  fs.writeFileSync(newsTsPath, tsContent, 'utf-8');
  console.log(`\n✅ Completed! Updated newsPosts.ts with ${pdfMap.size} resolved R2 PDF links.`);
}

run();
