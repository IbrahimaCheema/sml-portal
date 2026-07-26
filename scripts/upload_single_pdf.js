import fs from 'fs';
import { execSync } from 'child_process';
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

const ACCOUNT_ID = '9594508e0e41ab8192d129114cd8a539';
const ACCESS_KEY_ID = 'aab38b2efd2c96025f8815869503c4bc';
const SECRET_ACCESS_KEY = '3248746e1537c3372c9c04714c5680a2b678630c58516000fd306f9e04941d41';

const r2 = new S3Client({
  region: 'auto',
  endpoint: `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: { accessKeyId: ACCESS_KEY_ID, secretAccessKey: SECRET_ACCESS_KEY },
  forcePathStyle: true
});

execSync('curl.exe -k -s "https://www.sml.com.pk/wp-content/uploads/2025/07/Notice_BOD_072025.pdf" -o "temp_bod_jul2025.pdf"');
const buf = fs.readFileSync('temp_bod_jul2025.pdf');

r2.send(new PutObjectCommand({
  Bucket: 'sml-uploads',
  Key: 'docs/SML-Board-Meeting-Notice-July-2025.pdf',
  Body: buf,
  ContentType: 'application/pdf'
})).then(() => {
  console.log('✓ Successfully uploaded July 2025 BOD Notice PDF to R2!');
});
