import fs from 'fs';
import path from 'path';
import https from 'https';
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

const rawPosts = [
  {
    id: 'financial-results-half-year-31-mar-2026',
    title: 'Financial results for the Half Year Ended 31 Mar 2026',
    date: '2026-05-25',
    displayDate: '25 May 2026',
    category: 'Financial Results',
    excerpt: 'Condensed interim financial information and operational performance highlights of Shakarganj Limited for the half year ended 31 March 2026.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2026/07/SML-2026.03.3111-Q2_page-0002-350x204.jpg',
    r2Filename: 'news_2026_q2_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2026.03.31-Q2.pdf'
  },
  {
    id: 'notice-extraordinary-general-meeting-may-2026',
    title: 'Notice of Extraordinary General Meeting',
    date: '2026-05-08',
    displayDate: '8 May 2026',
    category: 'Shareholder Notice',
    excerpt: 'Notice is hereby given that an Extraordinary General Meeting (EGM) of Shakarganj Limited will be held to transact special corporate business.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2018/04/egm-350x204.png',
    r2Filename: 'news_egm_2026_thumb.png',
    linkUrl: '/shareholder-information',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-EGM-2026.pdf'
  },
  {
    id: 'corporate-briefing-session-2025',
    title: 'Corporate Briefing Session 2025',
    date: '2026-02-27',
    displayDate: '27 February 2026',
    category: 'Investor Relations',
    excerpt: 'Shakarganj Limited hosted its annual Corporate Briefing Session to present financial performance and strategic vision for FY 2025.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2025/02/corp-brief-350x204.png',
    r2Filename: 'news_corp_brief_2025_thumb.png',
    linkUrl: '/shareholder-information',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-CBS-2025.pdf'
  },
  {
    id: 'quarterly-report-31-december-2025',
    title: 'Quarterly Report for the Period Ended 31 December 2025',
    date: '2026-02-10',
    displayDate: '10 February 2026',
    category: 'Financial Results',
    excerpt: 'Un-audited financial statements of Shakarganj Limited for the first quarter ended 31 December 2025.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2026/02/SML-2025.12.31-Q1_page-0001-350x204.jpg',
    r2Filename: 'news_2025_q1_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2025.12.31-Q1.pdf'
  },
  {
    id: 'notice-board-meeting-feb-2026',
    title: 'Notice of Board of Directors Meeting',
    date: '2026-02-03',
    displayDate: '3 February 2026',
    category: 'Corporate Notice',
    excerpt: 'Meeting of the Board of Directors of Shakarganj Limited scheduled to consider quarterly financial statements.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2018/02/board-meeting-350x204.jpg',
    r2Filename: 'news_board_meeting_thumb.jpg',
    linkUrl: '/shareholder-information'
  },
  {
    id: 'annual-report-30-september-2025',
    title: 'Annual Report for the Year Ended 30 September 2025',
    date: '2026-01-19',
    displayDate: '19 January 2026',
    category: 'Financial Results',
    excerpt: 'Comprehensive audited annual financial statements and directors report of Shakarganj Limited for the year ended 30 September 2025.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2026/01/SML5.09.30thumb.jpg',
    r2Filename: 'news_annual_2025_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2025-Annual-Report.pdf'
  },
  {
    id: 'notice-annual-general-meeting-jan-2026',
    title: 'Notice of Annual General Meeting',
    date: '2026-01-16',
    displayDate: '16 January 2026',
    category: 'Shareholder Notice',
    excerpt: 'Notice is hereby given that the Annual General Meeting of Shakarganj Limited will be held on Thursday, 12 February 2026.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2018/01/agm-new-1-350x204.jpg',
    r2Filename: 'news_agm_thumb.jpg',
    linkUrl: '/shareholder-information'
  },
  {
    id: 'financial-results-3rd-quarter-30-june-2025',
    title: 'Financial results for the 3rd Quarter Ended 30 June 2025',
    date: '2025-07-30',
    displayDate: '30 July 2025',
    category: 'Financial Results',
    excerpt: 'Un-audited financial accounts of Shakarganj Limited for the third quarter ended 30 June 2025.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2025/07/SML-2025.06.30-Q3.pdf_news-350x204.jpg',
    r2Filename: 'news_2025_q3_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2025.06.30-Q3.pdf'
  },
  {
    id: 'notice-board-meeting-july-2025',
    title: 'Notice of Board of Directors Meeting',
    date: '2025-07-23',
    displayDate: '23 July 2025',
    category: 'Corporate Notice',
    excerpt: 'Meeting of the Board of Directors of Shakarganj Limited to review Q3 accounts.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2018/02/board-meeting-350x204.jpg',
    r2Filename: 'news_board_meeting_thumb_2.jpg',
    linkUrl: '/shareholder-information'
  },
  {
    id: 'financial-results-half-year-31-mar-2025',
    title: 'Financial results for the Half Year Ended 31 Mar 2025',
    date: '2025-05-30',
    displayDate: '30 May 2025',
    category: 'Financial Results',
    excerpt: 'Interim report and financial results for the half year ended 31 March 2025.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2025/05/mar-2025-350x204.jpg',
    r2Filename: 'news_2025_q2_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2025.03.31-Q2.pdf'
  },
  {
    id: 'notice-board-meeting-may-2025',
    title: 'Notice of Board of Directors Meeting',
    date: '2025-05-21',
    displayDate: '21 May 2025',
    category: 'Corporate Notice',
    excerpt: 'Board meeting notice for reviewing half-yearly financial statements.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2018/02/board-meeting-350x204.jpg',
    r2Filename: 'news_board_meeting_thumb_3.jpg',
    linkUrl: '/shareholder-information'
  },
  {
    id: 'corporate-briefing-session-2024',
    title: 'Corporate Briefing Session 2024',
    date: '2025-02-20',
    displayDate: '20 February 2025',
    category: 'Investor Relations',
    excerpt: 'Shakarganj Limited corporate presentation for analysts and investors reviewing performance.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2025/02/corp-brief-350x204.png',
    r2Filename: 'news_corp_brief_2024_thumb.png',
    linkUrl: '/shareholder-information'
  },
  {
    id: 'quarterly-report-31-december-2024',
    title: 'Quarterly Report for the Period Ended 31 December 2024',
    date: '2025-01-30',
    displayDate: '30 January 2025',
    category: 'Financial Results',
    excerpt: 'Financial accounts for the first quarter ended 31 December 2024.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2025/01/SML-2024.12.31-Q1_news-350x204.jpg',
    r2Filename: 'news_2024_q1_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2024.12.31-Q1.pdf'
  },
  {
    id: 'annual-report-30-september-2024',
    title: 'Annual Report for the Year Ended 30 September 2024',
    date: '2025-01-10',
    displayDate: '10 January 2025',
    category: 'Financial Results',
    excerpt: 'Audited Annual Financial Statements of Shakarganj Limited for FY 2024.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2025/01/Annual_2024_feature02-350x204.jpg',
    r2Filename: 'news_annual_2024_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2024-Annual-Report.pdf'
  },
  {
    id: 'notice-annual-general-meeting-jan-2025',
    title: 'Notice Of Annual General Meeting',
    date: '2025-01-06',
    displayDate: '6 January 2025',
    category: 'Shareholder Notice',
    excerpt: 'Notice of Annual General Meeting for shareholders of Shakarganj Limited.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2018/01/agm-new-1-350x204.jpg',
    r2Filename: 'news_agm_2025_thumb.jpg',
    linkUrl: '/shareholder-information'
  },
  {
    id: 'financial-results-3rd-quarter-30-june-2024',
    title: 'Financial results for the 3rd Quarter Ended 30 June 2024',
    date: '2024-07-30',
    displayDate: '30 July 2024',
    category: 'Financial Results',
    excerpt: 'Quarterly financial report of Shakarganj Limited for Q3 ended 30 June 2024.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2024/07/SML-2024.06.30-Q3_news-350x204.jpg',
    r2Filename: 'news_2024_q3_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2024.06.30-Q3.pdf'
  },
  {
    id: 'financial-results-half-year-31-mar-2024',
    title: 'Financial results for the Half Year Ended 31 Mar 2024',
    date: '2024-05-30',
    displayDate: '30 May 2024',
    category: 'Financial Results',
    excerpt: 'Interim financial information of Shakarganj Limited for half year ended 31 March 2024.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2024/06/SML-2024.03.31-Q2_page-0001-1-350x204.jpg',
    r2Filename: 'news_2024_q2_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2024.03.31-Q2.pdf'
  },
  {
    id: 'corporate-briefing-session-fy-2023',
    title: 'Corporate Briefing Session FY 2023',
    date: '2024-03-20',
    displayDate: '20 March 2024',
    category: 'Investor Relations',
    excerpt: 'Corporate Briefing Session for investors and shareholders on FY 2023 financial metrics.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2024/03/corp_briefing-350x204.png',
    r2Filename: 'news_corp_brief_2023_thumb.png',
    linkUrl: '/shareholder-information'
  },
  {
    id: 'quarterly-report-31-december-2023',
    title: 'Quarterly Report for the Period Ended 31 December 2023',
    date: '2024-02-07',
    displayDate: '7 February 2024',
    category: 'Financial Results',
    excerpt: 'Un-audited report for the first quarter ended 31 December 2023.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2024/02/news-dec2023-350x204.jpg',
    r2Filename: 'news_2023_q1_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2023.12.31-Q1.pdf'
  },
  {
    id: 'annual-report-30-september-2023',
    title: 'Annual Report for the Year Ended 30 September 2023',
    date: '2024-02-06',
    displayDate: '6 February 2024',
    category: 'Financial Results',
    excerpt: 'Annual audited financial accounts and reports of Shakarganj Limited for FY 2023.',
    wpImage: 'https://www.sml.com.pk/wp-content/uploads/2024/02/news-sep2023-350x204.jpg',
    r2Filename: 'news_annual_2023_thumb.jpg',
    linkUrl: '/financial-reports',
    pdfUrl: 'https://docs.sml.com.pk/docs/SML-2023-Annual-Report.pdf'
  }
];

import { execSync } from 'child_process';

function downloadFile(url, destPath) {
  try {
    execSync(`curl.exe -k -s "${url}" -o "${destPath}"`);
    if (fs.existsSync(destPath) && fs.statSync(destPath).size > 0) {
      return Promise.resolve();
    }
  } catch (err) {
    return Promise.reject(err);
  }
  return Promise.resolve();
}

async function processNews() {
  const tempDir = path.resolve('temp_news_assets');
  if (!fs.existsSync(tempDir)) {
    fs.mkdirSync(tempDir, { recursive: true });
  }

  const finalPosts = [];

  for (const item of rawPosts) {
    const localPath = path.join(tempDir, item.r2Filename);
    console.log(`Downloading ${item.wpImage}...`);
    try {
      await downloadFile(item.wpImage, localPath);
      console.log(`Uploading ${item.r2Filename} to R2...`);
      const fileBuffer = fs.readFileSync(localPath);
      const ext = path.extname(item.r2Filename).toLowerCase();
      const contentType = ext === '.png' ? 'image/png' : 'image/jpeg';

      await r2Client.send(new PutObjectCommand({
        Bucket: BUCKET_NAME,
        Key: `images/${item.r2Filename}`,
        Body: fileBuffer,
        ContentType: contentType
      }));

      const r2Url = `${PUBLIC_DOMAIN}/images/${item.r2Filename}`;

      finalPosts.push({
        id: item.id,
        title: item.title,
        date: item.date,
        displayDate: item.displayDate,
        category: item.category,
        excerpt: item.excerpt,
        featuredImage: r2Url,
        linkUrl: item.linkUrl,
        pdfUrl: item.pdfUrl || null
      });
      console.log(`Successfully processed ${item.id} -> ${r2Url}`);
    } catch (err) {
      console.error(`Failed processing ${item.id}:`, err.message);
      finalPosts.push({
        id: item.id,
        title: item.title,
        date: item.date,
        displayDate: item.displayDate,
        category: item.category,
        excerpt: item.excerpt,
        featuredImage: `${PUBLIC_DOMAIN}/images/report_2026_q2_thumb.jpg`,
        linkUrl: item.linkUrl,
        pdfUrl: item.pdfUrl || null
      });
    }
  }

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

export const newsPosts: NewsPost[] = ${JSON.stringify(finalPosts, null, 2)};
`;

  const targetTsFile = path.resolve('src/data/newsPosts.ts');
  const targetDir = path.dirname(targetTsFile);
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  fs.writeFileSync(targetTsFile, tsContent, 'utf-8');
  console.log(`Generated newsPosts.ts with ${finalPosts.length} posts successfully at ${targetTsFile}`);
}

processNews();
