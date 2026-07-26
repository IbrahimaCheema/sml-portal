import { S3Client, PutObjectCommand, DeleteObjectCommand, ListObjectsV2Command } from '@aws-sdk/client-s3';
import fs from 'fs';
import path from 'path';

const ACCOUNT_ID = '9594508e0e41ab8192d129114cd8a539';
const ACCESS_KEY_ID = 'aab38b2efd2c96025f8815869503c4bc';
const SECRET_ACCESS_KEY = '3248746e1537c3372c9c04714c5680a2b678630c58516000fd306f9e04941d41';
const BUCKET_NAME = 'sml-uploads';

const s3Client = new S3Client({
  region: 'auto',
  endpoint: `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: ACCESS_KEY_ID,
    secretAccessKey: SECRET_ACCESS_KEY,
  },
  forcePathStyle: true,
});

function getMimeType(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  if (ext === '.png') return 'image/png';
  if (ext === '.jpg' || ext === '.jpeg') return 'image/jpeg';
  if (ext === '.svg') return 'image/svg+xml';
  if (ext === '.webp') return 'image/webp';
  if (ext === '.ico') return 'image/x-icon';
  if (ext === '.pdf') return 'application/pdf';
  if (ext === '.woff') return 'font/woff';
  if (ext === '.woff2') return 'font/woff2';
  if (ext === '.ttf') return 'font/ttf';
  return 'application/octet-stream';
}

async function uploadFolder(localDir, s3Prefix = '') {
  const files = fs.readdirSync(localDir);
  for (const file of files) {
    const fullPath = path.join(localDir, file);
    const relativePath = s3Prefix ? `${s3Prefix}/${file}` : file;
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      await uploadFolder(fullPath, relativePath);
    } else {
      const fileBuffer = fs.readFileSync(fullPath);
      const mimeType = getMimeType(fullPath);

      console.log(`Uploading media -> ${relativePath} (${mimeType})...`);
      await s3Client.send(new PutObjectCommand({
        Bucket: BUCKET_NAME,
        Key: relativePath,
        Body: fileBuffer,
        ContentType: mimeType,
      }));
      console.log(`✓ Uploaded ${relativePath}`);
    }
  }
}

async function sanitizeStaleR2Assets() {
  console.log('\n--- Sanitizing Stale & Obsolete Objects in Cloudflare R2 ---');
  try {
    const listResp = await s3Client.send(new ListObjectsV2Command({
      Bucket: BUCKET_NAME
    }));

    if (listResp.Contents && listResp.Contents.length > 0) {
      for (const obj of listResp.Contents) {
        const key = obj.Key;
        if (!key) continue;

        let shouldDelete = false;

        // If key starts with images/
        if (key.startsWith('images/')) {
          const relativeFile = key.replace('images/', '');
          const localFile = path.resolve('public/images', relativeFile);
          if (!fs.existsSync(localFile)) {
            shouldDelete = true;
          }
        }
        // If key starts with fonts/
        else if (key.startsWith('fonts/')) {
          const relativeFile = key.replace('fonts/', '');
          const localFile = path.resolve('public/fonts', relativeFile);
          if (!fs.existsSync(localFile)) {
            shouldDelete = true;
          }
        }
        // If key starts with docs/
        else if (key.startsWith('docs/')) {
          const relativeFile = key.replace('docs/', '');
          const localFile = path.resolve('public/docs', relativeFile);
          if (!fs.existsSync(localFile)) {
            shouldDelete = true;
          }
        }
        // Delete non-media HTML/CSS/JS files
        else if (key.endsWith('.html') || key.endsWith('.css') || key.endsWith('.js') || key.startsWith('_astro/')) {
          shouldDelete = true;
        }

        if (shouldDelete) {
          console.log(`🗑️ Deleting stale/obsolete object from R2 -> ${key}...`);
          await s3Client.send(new DeleteObjectCommand({
            Bucket: BUCKET_NAME,
            Key: key,
          }));
          console.log(`✓ Sanitized/Removed ${key}`);
        }
      }
    }
  } catch (err) {
    console.error('Error during sanitization:', err);
  }
}

async function main() {
  console.log(`Cleaning non-media files and syncing ONLY media files, PDFs & fonts to Cloudflare R2 bucket: ${BUCKET_NAME}...`);
  
  // 1. Upload strictly media files (images)
  const imagesDir = path.resolve('public/images');
  if (fs.existsSync(imagesDir)) {
    console.log('\n--- Uploading ONLY media files (public/images) ---');
    await uploadFolder(imagesDir, 'images');
  }

  // 2. Upload PDFs (docs)
  const docsDir = path.resolve('public/docs');
  if (fs.existsSync(docsDir)) {
    console.log('\n--- Uploading PDFs & Documents (public/docs) ---');
    await uploadFolder(docsDir, 'docs');
  }

  // 3. Upload fonts
  const fontsDir = path.resolve('public/fonts');
  if (fs.existsSync(fontsDir)) {
    console.log('\n--- Uploading fonts (public/fonts) ---');
    await uploadFolder(fontsDir, 'fonts');
  }

  // 4. Sanitize obsolete files in R2
  await sanitizeStaleR2Assets();

  console.log('\n🎉 CLOUDFLARE R2 BUCKET IS NOW 100% SANITIZED AND SYNCED!');
}

main().catch(err => {
  console.error('❌ R2 Media Sync & Sanitization Failed:', err);
  process.exit(1);
});
