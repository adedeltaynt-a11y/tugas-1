# PROGRAM DATA OBAT DI APOTEK

obat = [
    ["Paracetamol", 50, 5000],
    ["Amoxicillin", 30, 12000],
    ["Antasida", 15, 8000],
    ["Ibuprofen", 25, 10000],
    ["Cetirizine", 8, 7000],
    ["Vitamin C", 40, 6000],
    ["OBH", 12, 15000],
    ["Omeprazole", 5, 18000],
    ["Antalgin", 20, 9000],
    ["CTM", 3, 4000]
]

print("=== DATA OBAT APOTEK ===")

for data in obat:
    nama = data[0]
    stok = data[1]
    harga = data[2]

    print("\nNama Obat :", nama)
    print("Stok      :", stok)
    print("Harga     : Rp", harga)

    # Operator pembanding dan kondisional
    if stok == 0:
        print("Status    : Stok Habis")
    elif stok < 10:
        print("Status    : Stok Menipis")
    elif stok >= 10:
        print("Status    : Stok Tersedia")
    else:
        print("Status    : Periksa Stok")

print("\n=== PEMERIKSAAN SELESAI ===")