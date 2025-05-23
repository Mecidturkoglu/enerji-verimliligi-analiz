# enerji-verimliligi-analiz
import os
from zipfile import ZipFile

# Klasör ve dosya yapısı
project_name = "enerji_verimliligi_analiz"
base_path = f"/mnt/data/{project_name}"
os.makedirs(base_path, exist_ok=True)

# HTML dosyası
index_html = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>Enerji Verimliliği Analizi</title>
</head>
<body>
  <h1>Enerji Verimliliği Formu</h1>
  <form action="/analiz" method="post">
    Firma Adı: <input type="text" name="firma"><br><br>
    Ekipman Türü: 
    <select name="ekipman">
      <option value="Pompa">Pompa</option>
      <option value="Motor">Motor</option>
      <option value="Fan">Fan</option>
    </select><br><br>
    Enerji Tüketimi (kWh/gün): <input type="number" name="kwh"><br><br>
    Çalışma Süresi (saat/gün): <input type="number" name="saat"><br><br>
    <button type="submit">Analiz Et</button>
  </form>
</body>
</html>
"""
templates_path = os.path.join(base_path, "templates")
os.makedirs(templates_path, exist_ok=True)
with open(os.path.join(templates_path, "index.html"), "w") as f:
    f.write(index_html)

# Python dosyası (Flask backend)
app_py = """from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "OPENAI_API_KEY"  # Buraya kendi API anahtarınızı yazın

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/analiz', methods=['POST'])
def analiz():
    firma = request.form['firma']
    ekipman = request.form['ekipman']
    kwh = request.form['kwh']
    saat = request.form['saat']
    
    prompt = f\"\"\"
    Bir enerji verimliliği uzmanı olarak aşağıdaki ekipmanı değerlendir:

    Firma: {firma}
    Ekipman Türü: {ekipman}
    Enerji Tüketimi: {kwh} kWh/gün
    Çalışma Süresi: {saat} saat/gün

    Bu bilgilerle enerji verimliliği açısından kısa bir analiz ve öneri ver.
    \"\"\"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    yorum = response["choices"][0]["message"]["content"]
    return f"<h2>Yapay Zeka Yorumu:</h2><p>{yorum}</p><br><a href='/'>Geri Dön</a>"

if __name__ == '__main__':
    app.run(debug=True)
"""
with open(os.path.join(base_path, "app.py"), "w") as f:
    f.write(app_py)

# requirements.txt
requirements_txt = """flask
openai
"""
with open(os.path.join(base_path, "requirements.txt"), "w") as f:
    f.write(requirements_txt)

# Projeyi zip dosyasına çevir
zip_path = f"/mnt/data/{project_name}.zip"
with ZipFile(zip_path, "w") as zipf:
    for root, dirs, files in os.walk(base_path):
        for file in files:
            filepath = os.path.join(root, file)
            zipf.write(filepath, os.path.relpath(filepath, base_path))

zip_path
