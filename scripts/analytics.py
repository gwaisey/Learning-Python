# Program Analisis Inventory & Keuangan Keyboard - Grace Mae
inventory_data = [
    {"item": "Ajazz AK820 Max", "stock": 5, "price": 750000},
    {"item": "Haimu Heartbeat Silent", "stock": 90, "price": 7000},
    {"item": "TTC Frozen Silent V2", "stock": 8, "price": 9500},
    {"item": "PBT Keycaps Dye-Sub", "stock": 12, "price": 350000},
    {"item": "Krytox 205g0 Lube", "stock": 3, "price": 85000}
]

def analyze_inventory(data):
    print("=== ⌨️  KEBOARD ASSET ANALYTICS BY GRACE ===")
    print(f"{'Item':<25} | {'Stock':<5} | {'Total Value':>15}")
    print("-" * 55)
    
    grand_total = 0
    total_items = 0

    for product in data:
        # Hitung nilai per produk
        subtotal = product['stock'] * product['price']
        grand_total += subtotal
        total_items += product['stock']
        
        # Tentukan warning stok
        alert = "⚠️ " if product['stock'] <= 5 else "✅ "
        
        print(f"{alert + product['item']:<25} | {product['stock']:<5} | Rp{subtotal:>14,}")

    print("-" * 55)
    print(f"Total Unit Barang : {total_items} pcs")
    print(f"Total Nilai Aset  : Rp{grand_total:>14,}")
    print("=" * 55)

if __name__ == "__main__":
    analyze_inventory(inventory_data)