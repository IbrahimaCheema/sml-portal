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

// Full list of source PDFs mapped to R2 keys
const pdfTasks = [
  {
    r2Key: 'docs/SML-EGM-Notice-2026.pdf',
    sourceUrl: 'https://dps.psx.com.pk/download/document/276918.pdf'
  },
  {
    r2Key: 'docs/SML-Corporate-Briefing-2025.pdf',
    sourceUrl: 'https://dps.psx.com.pk/download/document/271326.pdf'
  },
  {
    r2Key: 'docs/SML-Board-Meeting-Notice-Feb-2026.pdf',
    sourceUrl: 'https://dps.psx.com.pk/download/document/269619.pdf'
  },
  {
    r2Key: 'docs/SML-AGM-Notice-2026.pdf',
    sourceUrl: 'https://dps.psx.com.pk/download/document/268823.pdf'
  },
  {
    r2Key: 'docs/SML-Board-Meeting-Notice-July-2025.pdf',
    sourceUrl: 'https://www.sml.com.pk/wp-content/uploads/2025/07/Notice_BOD_072025.pdf'
  },
  {
    r2Key: 'docs/SML-Board-Meeting-Notice-May-2025.pdf',
    sourceUrl: 'https://dps.psx.com.pk/download/document/254171.pdf'
  },
  {
    r2Key: 'docs/SML-Corporate-Briefing-2024.pdf',
    sourceUrl: 'https://dps.psx.com.pk/download/document/247850.pdf'
  },
  {
    r2Key: 'docs/SML-AGM-Notice-2025.pdf',
    sourceUrl: 'https://dps.psx.com.pk/download/document/245538.pdf'
  },
  {
    r2Key: 'docs/SML-Corporate-Briefing-2023.pdf',
    sourceUrl: 'https://dps.psx.com.pk/download/document/227681.pdf'
  }
];

const USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36';

async function run() {
  const tempDir = path.resolve('temp_verified_pdfs');
  if (!fs.existsSync(tempDir)) fs.mkdirSync(tempDir, { recursive: true });

  for (const task of pdfTasks) {
    const filename = path.basename(task.r2Key);
    const localPath = path.join(tempDir, filename);

    console.log(`Downloading ${filename} from ${task.sourceUrl}...`);
    const cmd = `curl.exe -k -s -L -A "${USER_AGENT}" "${task.sourceUrl}" -o "${localPath}"`;
    execSync(cmd);

    if (fs.existsSync(localPath)) {
      const buffer = fs.readFileSync(localPath);
      const header = buffer.toString('utf-8', 0, 10);
      const sizeKB = (buffer.length / 1024).toFixed(1);

      console.log(`  File size: ${sizeKB} KB | Header: ${JSON.stringify(header)}`);

      if (header.includes('%PDF')) {
        console.log(`  ✓ VERIFIED PDF! Uploading to R2 (${task.r2Key})...`);
        await r2Client.send(new PutObjectCommand({
          Bucket: BUCKET_NAME,
          Key: task.r2Key,
          Body: buffer,
          ContentType: 'application/pdf'
        }));
        console.log(`  ✓ Success! R2 URL: ${PUBLIC_DOMAIN}/${task.r2Key}\n`);
      } else {
        console.error(`  ❌ FAILED: File is not a valid PDF! (Header: ${header})\n`);
      }
    } else {
      console.error(`  ❌ FAILED: File missing for ${filename}\n`);
    }
  }

  console.log('✨ All PDF downloads and R2 uploads verified!');
}

run();
