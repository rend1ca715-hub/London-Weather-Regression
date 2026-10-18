from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Memuat model hasil training
model = joblib.load("london_weather_tg_model.pkl")

# Daftar fitur yang dibutuhkan model
fitur = [
    "TX", "TN", "SS", "SD", "RR", "QQ", "PP",
    "HU", "CC", "YEAR", "MONTH", "DAY", "DAY_OF_YEAR"
]

@app.route("/")
def home():
    return "London Weather Regression API berhasil dijalankan!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Data JSON tidak ditemukan"}), 400

    if not all(kolom in data for kolom in fitur):
        return jsonify({"error": "Ada fitur yang belum diisi"}), 400

    input_data = pd.DataFrame(
        [[data[kolom] for kolom in fitur]],
        columns=fitur
    )

    hasil = model.predict(input_data)

    return jsonify({
        "prediksi_TG": float(hasil[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
