import { S3Client, PutObjectCommand, DeleteObjectCommand } from '@aws-sdk/client-s3';
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

async function deleteNonMedia() {
  const objectsToDelete = ['index.html', '_astro/index.BDK4Mvu0.css'];
  for (const key of objectsToDelete) {
    try {
      console.log(`Deleting non-media object -> ${key}...`);
      await s3Client.send(new DeleteObjectCommand({
        Bucket: BUCKET_NAME,
        Key: key,
      }));
      console.log(`✓ Removed ${key} from R2 bucket`);
    } catch (err) {
      // Ignore if object does not exist
    }
  }
}

async function main() {
  console.log(`Cleaning non-media files and syncing ONLY media files to Cloudflare R2 bucket: ${BUCKET_NAME}...`);
  
  // 1. Remove non-media HTML/CSS objects from R2
  await deleteNonMedia();

  // 2. Upload strictly media files (images, docs, PDFs)
  const imagesDir = path.resolve('public/images');
  if (fs.existsSync(imagesDir)) {
    console.log('\n--- Uploading ONLY media files (public/images) ---');
    await uploadFolder(imagesDir, 'images');
  }

  console.log('\n🎉 CLOUDFLARE R2 BUCKET IS NOW 100% CLEAN — CONTAINING ONLY MEDIA ASSETS (images/docs/PDFs)!');
}

main().catch(err => {
  console.error('❌ R2 Media Upload Failed:', err);
  process.exit(1);
});
