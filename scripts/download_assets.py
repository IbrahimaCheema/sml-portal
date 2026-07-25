import os
import urllib.request

images = [
  ("https://www.sml.com.pk/wp-content/uploads/2023/10/Untitled-design-4.png", "logo.png"),
  ("https://www.sml.com.pk/wp-content/uploads/2023/10/Untitled-design-6.png", "footer-logo.png"),
  ("https://www.sml.com.pk/wp-content/uploads/2023/11/SML-Logo-Icon-100x100.png", "sml-icon.png"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/02/slide_1.jpg", "slide_1.jpg"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/02/slider_2_new.jpg", "slide_2.jpg"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/02/slider_3_new.jpg", "slide_3.jpg"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/02/slider_4_new.jpg", "slide_4.jpg"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/02/sugar-cane-processed-sugar-image2-350x250.jpg", "segment-sugar.jpg"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/02/cotton-940x360-350x250.jpg", "segment-textile.jpg"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/02/sustainability-main-page-image-350x250.jpg", "segment-sustainability.jpg"),
  ("https://www.sml.com.pk/wp-content/uploads/2023/10/white-sugar-1-1-592x485.png", "product-white-sugar.png"),
  ("https://www.sml.com.pk/wp-content/uploads/2023/10/brown-sugar-592x471.png", "product-brown-sugar.png"),
  ("https://www.sml.com.pk/wp-content/uploads/2026/07/SML-2026.03.3111-Q2_page-0002-350x250.jpg", "notice-q2-2026.jpg"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/04/egm-350x245.png", "notice-egm.png"),
  ("https://www.sml.com.pk/wp-content/uploads/2025/02/corp-brief-350x250.png", "notice-corp-brief.png"),
  ("https://www.sml.com.pk/wp-content/uploads/2026/02/SML-2025.12.31-Q1_page-0001-350x250.jpg", "notice-q1-2025.jpg"),
  ("https://www.sml.com.pk/wp-content/uploads/2021/04/secp2021.png", "secp2021.png"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/03/jama-punji.png", "jama-punji.png"),
  ("https://www.sml.com.pk/wp-content/uploads/2018/02/cropped-SML-Logo-Icon-32x32.png", "favicon.png")
]

dest_dir = os.path.join(os.getcwd(), "public", "images")
os.makedirs(dest_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for url, filename in images:
    filepath = os.path.join(dest_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(filepath, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed {filename}: {e}")

print("Assets download complete.")
