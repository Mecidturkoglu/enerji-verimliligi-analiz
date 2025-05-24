from flask import Flask, render_template, request
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

    prompt = f"""
    Bir enerji verimliliği uzmanı olarak aşağıdaki ekipmanı değerlendir:

    Firma: {firma}
    Ekipman Türü: {ekipman}
    Enerji Tüketimi: {kwh} kWh/gün
    Çalışma Süresi: {saat} saat/gün

    Bu bilgilerle enerji verimliliği açısından kısa bir analiz ve öneri ver.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    yorum = response["choices"][0]["message"]["content"]
    return f"<h2>Yapay Zeka Yorumu:</h2><p>{yorum}</p><br><a href='/'>Geri Dön</a>"

if __name__ == '__main__':
    app.run(debug=True)
