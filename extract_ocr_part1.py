from pdf2image import convert_from_path
import pytesseract

pages = convert_from_path("tabel_scan.pdf", 300)

for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page, config="--psm 6")
    print(f"\n--- Page {i+1} ---")
    print(text)
