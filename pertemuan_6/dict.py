belanja = [
    {"buah":"semangka", "harga":120000},
    {"buah":"nanas", "harga":10000},
    {"buah":"pepaya", "harga":120000},
    ]

total_belanjaan = 0
for item in belanja:
    total_belanjaan += item["harga"]

print("Total Belanja : ", total_belanjaan)