import fs from 'fs';
import path from 'path';
import https from 'https';

const images = [
  { url: 'https://www.sml.com.pk/wp-content/uploads/2023/10/Untitled-design-4.png', name: 'logo.png' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2023/10/Untitled-design-6.png', name: 'footer-logo.png' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2023/11/SML-Logo-Icon-100x100.png', name: 'sml-icon.png' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/02/slide_1.jpg', name: 'slide_1.jpg' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/02/slider_2_new.jpg', name: 'slide_2.jpg' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/02/slider_3_new.jpg', name: 'slide_3.jpg' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/02/slider_4_new.jpg', name: 'slide_4.jpg' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/02/sugar-cane-processed-sugar-image2-350x250.jpg', name: 'segment-sugar.jpg' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/02/cotton-940x360-350x250.jpg', name: 'segment-textile.jpg' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/02/sustainability-main-page-image-350x250.jpg', name: 'segment-sustainability.jpg' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2023/10/white-sugar-1-1-592x485.png', name: 'product-white-sugar.png' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2023/10/brown-sugar-592x471.png', name: 'product-brown-sugar.png' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2026/07/SML-2026.03.3111-Q2_page-0002-350x250.jpg', name: 'notice-q2-2026.jpg' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/04/egm-350x245.png', name: 'notice-egm.png' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2025/02/corp-brief-350x250.png', name: 'notice-corp-brief.png' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2026/02/SML-2025.12.31-Q1_page-0001-350x250.jpg', name: 'notice-q1-2025.jpg' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2021/04/secp2021.png', name: 'secp2021.png' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/03/jama-punji.png', name: 'jama-punji.png' },
  { url: 'https://www.sml.com.pk/wp-content/uploads/2018/02/cropped-SML-Logo-Icon-32x32.png', name: 'favicon.png' }
];

const destDir = path.join(process.cwd(), 'public', 'images');
if (!fs.existsSync(destDir)) {
  fs.mkdirSync(destDir, { recursive: true });
}

function downloadFile(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    https.get(url, (response) => {
      if (response.statusCode >= 300 && response.statusCode < 400 && response.headers.location) {
        return downloadFile(response.headers.location, dest).then(resolve).catch(reject);
      }
      response.pipe(file);
      file.on('finish', () => {
        file.close(resolve);
      });
    }).on('error', (err) => {
      fs.unlink(dest, () => {});
      reject(err);
    });
  });
}

async function main() {
  console.log('Downloading assets...');
  for (const img of images) {
    const dest = path.join(destDir, img.name);
    try {
      await downloadFile(img.url, dest);
      console.log(`Downloaded ${img.name}`);
    } catch (e) {
      console.error(`Failed to download ${img.name}:`, e.message);
    }
  }
  console.log('Done downloading assets.');
}

main();
