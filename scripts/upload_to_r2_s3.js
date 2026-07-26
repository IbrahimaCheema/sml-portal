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

const existingR2Objects = new Map();

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

async function fetchR2State() {
  console.log('--- Fetching Cloudflare R2 Bucket Inventory ---');
  let token;
  do {
    const listResp = await s3Client.send(new ListObjectsV2Command({
      Bucket: BUCKET_NAME,
      ContinuationToken: token,
    }));
    if (listResp.Contents) {
      for (const item of listResp.Contents) {
        if (item.Key) existingR2Objects.set(item.Key, item.Size);
      }
    }
    token = listResp.NextContinuationToken;
  } while (token);
  console.log(`✓ Inventory loaded: ${existingR2Objects.size} objects in R2 bucket.`);
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
      const remoteSize = existingR2Objects.get(relativePath);
      if (remoteSize !== undefined && remoteSize === stat.size) {
        continue;
      }

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
      await new Promise(resolve => setTimeout(resolve, 20));
    }
  }
}

async function sanitizeStaleR2Assets() {
  console.log('\n--- Sanitizing Stale & Obsolete Objects in Cloudflare R2 ---');
  for (const [key] of existingR2Objects) {
    let shouldDelete = false;

    if (key.startsWith('images/')) {
      const relativeFile = key.replace('images/', '');
      const localFile = path.resolve('public/images', relativeFile);
      if (!fs.existsSync(localFile)) shouldDelete = true;
    } else if (key.startsWith('fonts/')) {
      const relativeFile = key.replace('fonts/', '');
      const localFile = path.resolve('public/fonts', relativeFile);
      if (!fs.existsSync(localFile)) shouldDelete = true;
    } else if (key.startsWith('docs/')) {
      const relativeFile = key.replace('docs/', '');
      const localFile = path.resolve('public/docs', relativeFile);
      if (!fs.existsSync(localFile)) shouldDelete = true;
    } else if (key.endsWith('.html') || key.endsWith('.css') || key.endsWith('.js') || key.startsWith('_astro/')) {
      shouldDelete = true;
    }

    if (shouldDelete) {
      console.log(`🗑️ Deleting stale/obsolete object from R2 -> ${key}...`);
      await s3Client.send(new DeleteObjectCommand({
        Bucket: BUCKET_NAME,
        Key: key,
      }));
      console.log(`✓ Sanitized/Removed ${key}`);
      await new Promise(resolve => setTimeout(resolve, 20));
    }
  }
}

async function main() {
  console.log(`Syncing media, PDFs & fonts to Cloudflare R2 bucket: ${BUCKET_NAME}...`);
  await fetchR2State();

  const imagesDir = path.resolve('public/images');
  if (fs.existsSync(imagesDir)) {
    await uploadFolder(imagesDir, 'images');
  }

  const docsDir = path.resolve('public/docs');
  if (fs.existsSync(docsDir)) {
    await uploadFolder(docsDir, 'docs');
  }

  const fontsDir = path.resolve('public/fonts');
  if (fs.existsSync(fontsDir)) {
    await uploadFolder(fontsDir, 'fonts');
  }

  await sanitizeStaleR2Assets();

  console.log('\n🎉 CLOUDFLARE R2 BUCKET IS NOW 100% SANITIZED AND SYNCED!');
}

main().catch(err => {
  console.error('❌ R2 Media Sync & Sanitization Failed:', err);
  process.exit(1);
});
