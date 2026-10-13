import fs from 'fs';

const content = fs.readFileSync('src/layouts/Layout.astro', 'utf-8');

// Extract rawTranslationList and translate logic
const startIndex = content.indexOf('const rawTranslationList = [');
const endIndex = content.indexOf('];', startIndex);
if (startIndex === -1 || endIndex === -1) {
  console.error('Failed to match rawTranslationList');
  process.exit(1);
}
const arrayCode = content.substring(startIndex + 'const rawTranslationList = '.length, endIndex + 1);
const rawTranslationList = eval(arrayCode);
const sortedTranslations = [...rawTranslationList].sort((a, b) => b[0].length - a[0].length);
const exactTranslationMap = new Map();
for (const [en, ur] of sortedTranslations) {
  exactTranslationMap.set(en.trim(), ur);
}

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function translateText(val) {
  if (!val || !val.trim()) return val;
  const trimmed = val.trim();
  if (exactTranslationMap.has(trimmed)) {
    const lead = val.match(/^\s*/)[0];
    const trail = val.match(/\s*$/)[0];
    return lead + exactTranslationMap.get(trimmed) + trail;
  }
  let result = val;
  for (let i = 0; i < sortedTranslations.length; i++) {
    const en = sortedTranslations[i][0];
    const ur = sortedTranslations[i][1];
    if (result.includes(en)) {
      result = result.replace(new RegExp(escapeRegex(en), 'g'), ur);
    }
  }
  return result;
}

const testCases = [
  ['Notice of Board of Directors Meeting', 'بورڈ آف ڈائریکٹرز کے اجلاس کا نوٹس'],
  ['Board Meeting Other Than Financial Results', 'بورڈ کا اجلاس (بغیر مالیاتی نتائج)'],
  ['Transmission of Quarterly Report for the Period Ended June 30, 2026', '30 جون 2026ء کو ختم ہونے والے عرصے کی سہ ماہی رپورٹ کی ترسیل'],
  ['Financial results for the Half Year Ended 31 Mar 2026', '31 مارچ 2026ء کو ختم ہونے والے نصف سال کے مالیاتی نتائج'],
  ['Awards and Accolades', 'اعزازات اور انعامات'],
  ['Certifications', 'سرٹیفیکیشنز'],
  ["Company's Own Complaint Handling Cell", 'کمپنی کا اپنا شکایات سیل'],
  ['Registration / NTN', 'رجسٹریشن / این ٹی این'],
  ['Company Registration Number', 'کمپنی رجسٹریشن نمبر'],
  ['National Tax Number', 'قومی ٹیکس نمبر (NTN)'],
  ['Sales Tax Number', 'سیلز ٹیکس نمبر'],
  ['Corporate Sitemap', 'کارپوریٹ سائٹ میپ'],
  ['Search portal...', 'پورٹل تلاش کریں...'],
  ['Updated on: 26 July, 2026', 'آخری اپ ڈیٹ: 26 جولائی 2026ء'],
  ['22 July 2026', '22 جولائی 2026ء'],
  ['30 July 2026', '30 جولائی 2026ء'],
  ['23 September 2026', '23 ستمبر 2026ء'],
  ['Corporate Notice', 'کارپوریٹ نوٹس'],
  ['Financial Results', 'مالیاتی نتائج']
];

let failed = 0;
for (const [input, expected] of testCases) {
  const actual = translateText(input);
  if (actual !== expected) {
    console.error(`FAILED: "${input}"\nExpected: "${expected}"\nGot:      "${actual}"`);
    failed++;
  } else {
    console.log(`PASS: "${input}" -> "${actual}"`);
  }
}

if (failed === 0) {
  console.log('\nALL 19 VERIFICATION TESTS PASSED 100%!');
  process.exit(0);
} else {
  console.error(`\n${failed} TESTS FAILED`);
  process.exit(1);
}
