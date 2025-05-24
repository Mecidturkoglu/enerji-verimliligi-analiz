# enerji-verimliligi-analiz
<!DOCTYPE html>
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
