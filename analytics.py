# Program Analisis Inventory Mechanical Keyboard - Grace Mae
inventory_data = [
    {"item": "Ajazz AK820 Max", "stock": 5, "price": 750000},
    {"item": "Haimu Heartbeat Silent", "stock": 90, "price": 7000},
    {"item": "TTC Frozen Silent V2", "stock": 8, "price": 9500},
    {"item": "PBT Keycaps Dye-Sub", "stock": 12, "price": 350000},
    {"item": "Krytox 205g0 Lube", "stock": 3, "price": 85000}
]

def analyze_stock(data):
    print("=== ⌨️ Laporan Inventory Keyboard Grace ⌨️ ===")
    print("-" * 50)
    for product in data:
        # Menentukan status berdasarkan jumlah stok
        status = "STOCK AMAN" if product['stock'] > 10 else "RESTOCK SEGERA!"
        
        # Kalkulasi nilai aset
        total_value = product['stock'] * product['price']
        
        # Print dengan formatting yang rapi
        print(f"Item  : {product['item']:<25}")
        print(f"Status: {status:<15} | Aset: Rp{total_value:>10,}")
        print("-" * 50)

if __name__ == "__main__":
    analyze_stock(inventory_data)