import os, urllib.request

pdfs = {
    "https://www.sml.com.pk/wp-content/uploads/2024/03/Detail-of-Pending-Dividend-2023.pdf": "Detail-of-Pending-Dividend-2023.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/05/Notice-159-english-2026.pdf": "Notice-159-english-2026.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/05/Notice-159-Urdu-2026.pdf": "Notice-159-Urdu-2026.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/05/eogm-2026-e.pdf": "eogm-2026-e.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/05/eogm-2026-u.pdf": "eogm-2026-u.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/05/eogm-proxy-2026-e.pdf": "eogm-proxy-2026-e.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/05/eogm-proxy-2026-u.pdf": "eogm-proxy-2026-u.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2023/05/List-of-Shareholders-for-EOGM.pdf": "List-of-Shareholders-for-EOGM.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/06/results2026.pdf": "results2026.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/06/Report-of-Scrutinizer-2026.pdf": "Report-of-Scrutinizer-2026.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2020/12/Code-of-Conduct.pdf": "Code-of-Conduct.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2020/12/Policies-Register.pdf": "Policies-Register.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/02/Website_Compliance_Certificate_Sep_2025.pdf": "Website_Compliance_Certificate_Sep_2025.pdf",
    "https://www.sml.com.pk/wp-content/uploads/2026/02/Gende_Pay_Gap_Statement_2025.pdf": "Gende_Pay_Gap_Statement_2025.pdf"
}

imgs = {
    "https://www.sml.com.pk/wp-content/uploads/2021/04/secp2021.png": "secp2021.png",
    "https://www.sml.com.pk/wp-content/uploads/2018/03/jama-punji.png": "jama-punji.png"
}

doc_dirs = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\docs\shareholder',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\docs\shareholder',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\docs\shareholder'
]

img_dirs = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\images',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\images',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\images'
]

for d in doc_dirs + img_dirs:
    os.makedirs(d, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("Downloading shareholder PDFs...")
for remote_url, fname in pdfs.items():
    for d in doc_dirs:
        dest_path = os.path.join(d, fname)
        if not os.path.exists(dest_path):
            try:
                req = urllib.request.Request(remote_url, headers=headers)
                with urllib.request.urlopen(req) as resp, open(dest_path, 'wb') as out_f:
                    out_f.write(resp.read())
                print(f"Downloaded PDF {fname} -> {d}")
            except Exception as e:
                print(f"Failed to download PDF {fname}: {e}")

print("Downloading shareholder images...")
for remote_url, fname in imgs.items():
    for d in img_dirs:
        dest_path = os.path.join(d, fname)
        if not os.path.exists(dest_path):
            try:
                req = urllib.request.Request(remote_url, headers=headers)
                with urllib.request.urlopen(req) as resp, open(dest_path, 'wb') as out_f:
                    out_f.write(resp.read())
                print(f"Downloaded Image {fname} -> {d}")
            except Exception as e:
                print(f"Failed to download Image {fname}: {e}")

print("Shareholder asset download completed!")
