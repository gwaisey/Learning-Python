def analyze_inventory(data):
    print("\n" + "="*55)
    print("=== ⌨️  KEYBOARD ASSET ANALYTICS BY GRACE ===")
    print(f"{'Item':<25} | {'Stock':<5} | {'Total Value':>15}")
    print("-" * 55)
    
    grand_total = 0
    for product in data:
        subtotal = product['stock'] * product['price']
        grand_total += subtotal
        alert = "⚠️ " if product['stock'] <= 5 else "✅ "
        print(f"{alert + product['item']:<25} | {product['stock']:<5} | Rp{subtotal:>14,}")

    print("-" * 55)
    print(f"Total Nilai Aset  : Rp{grand_total:>14,}")
    print("=" * 55 + "\n")

def main():
    # Kita mulai dengan list kosong
    my_inventory = []
    
    print("Selamat Datang di Program Input Inventory Grace!")
    
    while True:
        print("\n[1] Tambah Barang Baru")
        print("[2] Lihat Laporan & Selesai")
        print("[q] Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            nama = input("Nama komponen keyboard: ")
            stok = int(input("Jumlah stok (angka): "))
            harga = int(input("Harga per unit (angka): "))
            
            # Memasukkan data ke dalam list
            my_inventory.append({"item": nama, "stock": stok, "price": harga})
            print(f"✅ {nama} berhasil ditambahkan!")
            
        elif pilihan == '2':
            if not my_inventory:
                print("Inventory masih kosong, isi dulu yuk!")
            else:
                analyze_inventory(my_inventory)
                break # Keluar dari loop setelah cetak laporan
                
        elif pilihan.lower() == 'q':
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()