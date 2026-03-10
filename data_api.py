from flask import Flask, render_template_string

app = Flask(__name__)

# Data inventory keyboard kamu
inventory_data = [
    {"item": "Ajazz AK820 Max", "stock": 5},
    {"item": "TTC Frozen Silent", "stock": 15},
    {"item": "Haimu Heartbeat Silent", "stock": 90}
]

# Ini HTML & CSS yang tadi, kita masukan ke dalam variable
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Grace's Keyboard Vault</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f8fafc; display: flex; justify-content: center; padding: 40px; }
        .container { width: 100%; max-width: 400px; }
        .inventory-card { 
            background: white; border-radius: 12px; padding: 20px; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 16px; 
            border-left: 5px solid #6366f1; display: flex; justify-content: space-between; 
        }
        .stock-badge { 
            background: #e0e7ff; color: #4338ca; padding: 4px 12px; 
            border-radius: 20px; font-weight: bold; 
        }
        .low-stock { background: #fee2e2; color: #b91c1c; }
    </style>
</head>
<body>
    <div class="container">
        <h2>⌨️ My Keyboard Inventory</h2>
        {% for item in data %}
        <div class="inventory-card">
            <span><strong>{{ item.item }}</strong></span>
            <span class="stock-badge {{ 'low-stock' if item.stock <= 5 else '' }}">
                {{ item.stock }} Units
            </span>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # Menampilkan HTML langsung dari Python
    return render_template_string(HTML_TEMPLATE, data=inventory_data)

if __name__ == "__main__":
    app.run(port=5000)