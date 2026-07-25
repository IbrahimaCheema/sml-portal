import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
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
  if (ext === '.html') return 'text/html';
  if (ext === '.css') return 'text/css';
  if (ext === '.js') return 'application/javascript';
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

      console.log(`Uploading -> ${relativePath} (${mimeType})...`);
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

async function main() {
  console.log(`Starting R2 upload to bucket: ${BUCKET_NAME}...`);
  
  // 1. Upload public images to images/
  const imagesDir = path.resolve('public/images');
  if (fs.existsSync(imagesDir)) {
    console.log('\n--- Uploading public/images ---');
    await uploadFolder(imagesDir, 'images');
  }

  // 2. Upload dist static site assets
  const distDir = path.resolve('dist');
  if (fs.existsSync(distDir)) {
    console.log('\n--- Uploading dist static site ---');
    await uploadFolder(distDir, '');
  }

  console.log('\n🎉 ALL MEDIA & STATIC ASSETS UPLOADED TO CLOUDFLARE R2 BUCKET docs.sml.com.pk SUCCESSFULLY!');
}

main().catch(err => {
  console.error('❌ R2 Upload Failed:', err);
  process.exit(1);
});
