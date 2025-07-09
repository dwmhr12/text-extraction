from docling import Docling

# 1. Buka dokumen PDF
doc = Docling.from_file("dokumen_teks.pdf")

# 2. Loop semua elemen dalam dokumen
for node in doc.nodes:
    print(f"\n== Node Type: {node.type} ==")

    if node.type == "TextNode":
        print("📄 Teks:")
        print(node.text[:200])  

    elif node.type == "TableNode":
        print("📊 Tabel:")
        for row in node.table:
            print(row)

    elif node.type == "FigureNode":
        print("🖼️ Gambar (Figure) ditemukan")

    # Tambahan metadata
    print("📌 Metadata:", node.metadata)
