import os
import json
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Lokasi database JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "inventory.json")

def get_data():
    if os.path.exists(DB_PATH):
        try:
            with open(DB_PATH, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_data(data):
    with open(DB_PATH, 'w') as f:
        json.dump(data, f, indent=4)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Grace's Dashboard</title>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f1f5f9; padding: 40px; color: #1e293b; }
        .container { width: 100%; max-width: 500px; margin: auto; }
        .summary-card { 
            background: linear-gradient(135deg, #6366f1 0%, #4338ca 100%); 
            color: white; border-radius: 16px; padding: 25px; 
            margin-bottom: 30px; box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.3);
        }
        .input-section {
            background: white; border-radius: 12px; padding: 20px; margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        input { width: 92%; padding: 10px; margin: 5px 0; border: 1px solid #ddd; border-radius: 6px; }
        button { 
            width: 100%; padding: 10px; background: #6366f1; color: white; 
            border: none; border-radius: 6px; cursor: pointer; font-weight: bold; margin-top: 10px;
        }
        button:hover { background: #4338ca; }
        .inventory-card { 
            background: white; border-radius: 12px; padding: 18px; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 12px; 
            display: flex; justify-content: space-between; align-items: center;
        }
        .stock-badge { padding: 6px 12px; border-radius: 8px; font-weight: 700; font-size: 0.75rem; }
        .status-ok { background: #dcfce7; color: #15803d; }
        .status-low { background: #fee2e2; color: #b91c1c; }
    </style>
</head>
<body>
    <div class="container">
        <h2>⌨️ Grace's Keyboard Vault</h2>
        
        <div class="input-section">
            <h4 style="margin-top:0">Tambah Barang Baru</h4>
            <form action="/add" method="POST">
                <input type="text" name="item" placeholder="Nama Barang (contoh: TTC Gold Pink)" required>
                <input type="number" name="stock" placeholder="Jumlah Stok" required>
                <input type="number" name="price" placeholder="Harga Satuan" required>
                <button type="submit">Simpan ke Inventory</button>
            </form>
        </div>

        <div class="summary-card">
            <div style="font-size: 0.875rem; opacity: 0.9;">Total Asset Value</div>
            <div style="font-size: 2rem; font-weight: 800;">Rp {{ "{:,.0f}".format(total_value) }}</div>
        </div>

        <div id="list">
            {% for item in data %}
            <div class="inventory-card">
                <div>
                    <div style="font-weight: 600;">{{ item.item }}</div>
                    <div style="font-size: 0.8rem; color: #64748b;">Rp {{ "{:,.0f}".format(item.price) }}</div>
                </div>
                <div class="stock-badge {{ 'status-low' if item.stock <= 5 else 'status-ok' }}">
                    {{ item.stock }} PCS
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    data = get_data()
    total = sum(item.get('stock', 0) * item.get('price', 0) for item in data)
    return render_template_string(HTML_TEMPLATE, data=data, total_value=total)

@app.route('/add', methods=['POST'])
def add_item():
    # Ambil data dari form HTML
    new_item = {
        "item": request.form.get('item'),
        "stock": int(request.form.get('stock')),
        "price": int(request.form.get('price'))
    }
    
    # Ambil data lama, tambah yang baru, lalu simpan
    data = get_data()
    data.append(new_item)
    save_data(data)
    
    # Kembali ke halaman utama
    return redirect('/')

if __name__ == "__main__":
    app.run(port=5000)