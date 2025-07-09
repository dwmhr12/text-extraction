from unstructured.partition.pdf import partition_pdf

elements = partition_pdf(
    filename="tabel_scan.pdf",
    strategy="hi_res",                  # pakai OCR dan layout analysis
    infer_table_structure=True,        
    languages=["ind", "eng"],           # bahasa OCR
)

# Lihat hasilnya
for el in elements:
    print(f"\n== {el.category} ==")
    print(el.text[:300])  
