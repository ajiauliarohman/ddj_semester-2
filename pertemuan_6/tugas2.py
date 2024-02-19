data_penjualan =[
    {"produk":"baju","jumlah":20},
    {"produk":"celana","jumlah":15},
    {"produk":"sepatu","jumlah":25},
    {"produk":"tas","jumlah":10},
    ]

total_belanjaan = 0
for item in data_penjualan:
    total_belanjaan += item["jumlah"]

print("Total Belanja : ", total_belanjaan)