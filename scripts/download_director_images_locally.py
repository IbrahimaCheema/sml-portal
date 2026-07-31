import os, urllib.request, glob

director_images = {
    "https://www.sml.com.pk/wp-content/uploads/2024/01/Untitled-240-x-321-px-302-x-584-px-3-1.png": "manzoor-hussain.png",
    "https://www.sml.com.pk/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-07-at-11.35.50-AM-scaled-302x584.jpeg": "pervez-akhtar.jpeg",
    "https://www.sml.com.pk/wp-content/uploads/2024/01/Untitled-240-x-321-px-302-x-584-px-4.png": "ali-altaf-saleem.png",
    "https://www.sml.com.pk/wp-content/uploads/2026/07/Baber_Zaman.png": "baber-zaman.png",
    "https://www.sml.com.pk/wp-content/uploads/2025/08/Adil-Qureshi.jpg": "adil-qureshi.jpg",
    "https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-31-302x584.png": "mustapha-altaf-saleem.png",
    "https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-34.png": "sana-atif.png",
    "https://www.sml.com.pk/wp-content/uploads/2026/07/Waqas_Shafeeq.png": "waqas-shafeeq.png",
    "https://www.sml.com.pk/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-07-at-11.53.46-AM-1-302x584.jpeg": "asif-ali.jpeg",
    "https://www.sml.com.pk/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-07-at-11.53.46-AM-302x584.jpeg": "muhammad-asif.jpeg",
    "https://www.sml.com.pk/wp-content/uploads/2025/08/cheema_SML.png": "ibrahim-cheema.png",
    "https://www.sml.com.pk/wp-content/uploads/2024/02/Untitled-design-36.png": "muhammad-saifullah.png"
}

dirs = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\images\directors',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\images\directors',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\images\directors'
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("Downloading director images locally...")
for remote_url, fname in director_images.items():
    for d in dirs:
        dest_path = os.path.join(d, fname)
        if not os.path.exists(dest_path):
            try:
                req = urllib.request.Request(remote_url, headers=headers)
                with urllib.request.urlopen(req) as resp, open(dest_path, 'wb') as out_f:
                    out_f.write(resp.read())
                print(f"Downloaded {fname} -> {d}")
            except Exception as e:
                print(f"Failed to download {fname}: {e}")

# Replace all remote URL references in board-of-directors pages with local paths
targets = [
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\board-of-directors.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\public\board-of-directors.html',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\src\pages\board-of-directors.astro',
    r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-redesign\board-of-directors.html'
]

for t in targets:
    if not os.path.exists(t): continue
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for remote_url, fname in director_images.items():
        local_src = f"/images/directors/{fname}"
        content = content.replace(remote_url, local_src)
        
    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all board-of-directors files to point to local /images/directors/ assets!")
