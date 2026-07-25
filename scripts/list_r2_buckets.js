import { S3Client, ListBucketsCommand } from '@aws-sdk/client-s3';

const ACCOUNT_ID = '9594508e0e41ab8192d129114cd8a539';
const ACCESS_KEY_ID = 'aab38b2efd2c96025f8815869503c4bc';
const SECRET_ACCESS_KEY = '3248746e1537c3372c9c04714c5680a2b678630c58516000fd306f9e04941d41';

const s3Client = new S3Client({
  region: 'auto',
  endpoint: `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: ACCESS_KEY_ID,
    secretAccessKey: SECRET_ACCESS_KEY,
  },
  forcePathStyle: true,
});

async function main() {
  const result = await s3Client.send(new ListBucketsCommand({}));
  console.log('R2 Buckets List:');
  console.log(result.Buckets);
}

main().catch(console.error);
