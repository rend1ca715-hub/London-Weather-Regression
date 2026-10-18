# London Weather Regression

## Deskripsi Proyek

London Weather Regression merupakan proyek machine learning yang bertujuan untuk memprediksi temperatur udara (`TG`) berdasarkan data cuaca London. Proyek ini menggunakan model regresi yang telah dilatih menggunakan data cuaca periode 1979–2023.

## Tujuan

Proyek ini bertujuan untuk menerapkan metode regresi dalam memprediksi temperatur udara berdasarkan variabel cuaca dan informasi tanggal.

## Teknologi yang Digunakan

- Python
- Pandas
- Scikit-learn
- Joblib
- Flask
- cURL

## Komponen Proyek

- `app.py` atau `testing_deploy.py`: Program API untuk menjalankan prediksi temperatur.
- `requirements.txt`: Daftar library yang diperlukan.
- `london_weather_tg_model.pkl`: Model machine learning yang telah dilatih.
- `data.json`: Contoh data input untuk pengujian API.
- `london_weather_data_1979_to_2023.csv`: Dataset cuaca London.
- Notebook Jupyter (`.ipynb`): Dokumentasi proses pengolahan data dan pemodelan, jika tersedia.

## Cara Menjalankan Program

1. Instal library yang diperlukan:

   `pip install -r requirements.txt`

2. Jalankan API melalui terminal:

   `python testing_deploy.py`

   Jika nama file yang digunakan adalah `app.py`, jalankan `python app.py`.

3. Buka alamat berikut pada browser untuk memeriksa apakah API berjalan:

   `http://127.0.0.1:5000`

## Pengujian Prediksi

API menyediakan endpoint `/predict` dengan metode `POST`. Data input dikirim dalam format JSON menggunakan file `data.json`.

Contoh perintah pengujian melalui Windows PowerShell:

`curl.exe -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" --data-binary "@data.json"`

Jika berhasil, API akan mengembalikan hasil prediksi dalam format JSON dengan atribut `prediksi_TG`.

## Status Proyek

API telah berhasil dijalankan dan diuji secara lokal. Deployment online belum dikonfirmasi.

## Dataset

Dataset berisi catatan cuaca London periode 1979–2023 dan digunakan sebagai sumber data dalam pengembangan model prediksi temperatur.
