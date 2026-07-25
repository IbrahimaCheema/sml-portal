import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const BUCKET_NAME = 'docs.sml.com.pk';
const IMAGES_DIR = path.resolve('public/images');

if (!fs.existsSync(IMAGES_DIR)) {
  console.error(`Directory not found: ${IMAGES_DIR}`);
  process.exit(1);
}

console.log(`Uploading media files to Cloudflare R2 bucket: ${BUCKET_NAME}...`);

const files = fs.readdirSync(IMAGES_DIR);
for (const file of files) {
  const filePath = path.join(IMAGES_DIR, file);
  if (fs.statSync(filePath).isFile()) {
    const destination = `images/${file}`;
    console.log(`Uploading ${file} -> ${destination}...`);
    try {
      execSync(`npx wrangler r2 object put "${BUCKET_NAME}/${destination}" --file="${filePath}"`, { stdio: 'inherit' });
    } catch (err) {
      console.error(`Failed to upload ${file}:`, err.message);
    }
  }
}

console.log('R2 Upload process complete.');
