from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

openai_api_key = os.getenv("OPENAI_API_KEY") or "senin_api_anahtarın"
client = openai.OpenAI(api_key=openai_api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    yorum = ""
    if request.method == "POST":
        ekipman = request.form["ekipman"]
        tuketim = request.form["tuketim"]
        mesaj = f"{ekipman} ekipmanının ölçülen enerji tüketimi: {tuketim} kWh. Bu değeri değerlendir ve enerji verimliliği açısından önerilerde bulun."

        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Sen bir enerji verimliliği uzmanısın. Verileri analiz et ve net öneriler sun."},
                    {"role": "user", "content": mesaj}
                ]
            )
            yorum = completion.choices[0].message.content.strip()
        except Exception as e:
            yorum = f"Hata oluştu: {str(e)}"

    return render_template("index.html", yorum=yorum)

if __name__ == "__main__":
    app.run(debug=True)
