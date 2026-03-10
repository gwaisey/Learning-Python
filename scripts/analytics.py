import json
import os

# --- PERBAIKAN PATH DISINI ---
# Mencari lokasi folder utama 'Learning-Python' secara otomatis
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
DB_FILE = os.path.join(BASE_DIR, "..", "inventory.json")

def load_data():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_data(data):
    # Memastikan data benar-benar tertulis ke file yang tepat
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    # Debugging: print lokasi file aslinya untuk memastikan
    print(f"DEBUG: File disimpan di {os.path.abspath(DB_FILE)}")

def main():
    inventory = load_data()
    print("--- Program Input Inventory Terintegrasi ---")
    
    nama = input("Nama Barang: ")
    stok = int(input("Stok: "))
    harga = int(input("Harga: "))
    
    inventory.append({"item": nama, "stock": stok, "price": harga})
    save_data(inventory)
    print("✅ Data tersimpan ke JSON!")

if __name__ == "__main__":
    main()