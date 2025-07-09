import fitz #alias dari pymupdf

def extract_text_pdf(file_path):
    doc = fitz.open(file_path)
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        print(f"\n--- Page {page_num} ---")
        print(text)

extract_text_pdf("tabel_scan.pdf")