from pdf2image import convert_from_path
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image, ImageFont
import pandas as pd
import os

# ------------ PARAMETER ------------
PDF_PATH   = "halaman1.pdf"   
PAGE_IDX   = 0                    
DPI        = 300
LANG_OCR   = "latin"              # model Latin (untuk bahasa Indonesia)
FONT_PATH  = "fonts/OpenSans-Regular.ttf"  

# ------------ 1. Konversi PDF ➜ PNG ------------
pages = convert_from_path(PDF_PATH, dpi=DPI)
img_path = f"{os.path.splitext(PDF_PATH)[0]}_page{PAGE_IDX+1}.png"
pages[PAGE_IDX].save(img_path)
print(f"✅ Gambar disimpan sebagai: {img_path}")

# ------------ 2. Inisialisasi PaddleOCR ------------
ocr = PaddleOCR(use_angle_cls=True, lang=LANG_OCR, show_log=False)

# ------------ 3. Jalankan OCR ------------
result = ocr.ocr(img_path, cls=True)[0]  

# ------------ 4. Kumpulkan hasil teks + koordinat ------------
rows = []
for i, line in enumerate(result, 1):
    points, (text, score) = line
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    rows.append([i, text, score, min(xs), min(ys), max(xs), max(ys)])
    print(f"{i:>2}. {text}  (conf {score:.2f})")

# ------------ 5. Gambar hasil OCR ke gambar ------------
image  = Image.open(img_path).convert("RGB")
boxes  = [l[0] for l in result]
txts   = [l[1][0] for l in result]
scores = [l[1][1] for l in result]

# Gunakan font agar draw_ocr bisa jalan
vis_img = Image.fromarray(draw_ocr(image, boxes, txts, scores, font_path=FONT_PATH))
output_img_path = "hasil_draw_ocr.png"
vis_img.save(output_img_path)

# ------------ 6. Simpan hasil mentah ke CSV ------------
pd.DataFrame(
    rows, columns=["id", "text", "conf", "x0", "y0", "x1", "y1"]
).to_csv("ocr_raw.csv", index=False)

# ------------ 7. Selesai ------------
print("\n🎉 OCR selesai!")
print(f"✅ Gambar anotasi disimpan di : {output_img_path}")
print("✅ CSV teks mentah disimpan di  : ocr_raw.csv")
