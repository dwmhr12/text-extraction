import pdfplumber

with pdfplumber.open("tabel_scan.pdf") as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):  
        print(f"\n--- Page {page_num} ---")
        print(page.extract_text())

        tables = page.extract_tables()
        for table in tables:
            print("Tabel Ditemukan: ")
            for row in table:  
                print(row)
