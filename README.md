# London Weather Regression

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis data cuaca London dan membangun model machine learning untuk memprediksi nilai temperatur rata-rata harian (`TG`) berdasarkan fitur cuaca dan informasi tanggal.

Dataset yang digunakan mencakup data cuaca London dari tahun 1979 hingga 2023.

## Algoritma

Tiga algoritma regresi yang digunakan dalam proyek ini adalah:

1. **Linear Regression** sebagai model regresi dasar.
2. **Random Forest Regressor** untuk mempelajari hubungan nonlinier melalui kumpulan pohon keputusan.
3. **HistGradientBoosting Regressor** untuk membangun model boosting secara bertahap.

## Dataset

Dataset yang digunakan adalah `london_weather_data_1979_to_2023.csv`.

Target prediksi:
- `TG`: temperatur rata-rata harian sesuai definisi dan satuan pada sumber dataset.

Kolom tanggal diolah menjadi fitur kalender, sedangkan kolom penanda kualitas data tidak digunakan sebagai fitur prediksi.

## Tahapan Pengerjaan

1. Import library.
2. Membaca dan memahami dataset.
3. Eksplorasi data dan visualisasi.
4. Memeriksa missing values dan data duplikat.
5. Melakukan preprocessing.
6. Membagi data training dan testing berdasarkan urutan waktu.
7. Melatih tiga model regresi.
8. Mengevaluasi model menggunakan MAE, RMSE, dan R².
9. Membandingkan performa model dan menyimpan model terbaik.

## Evaluasi Model

- **MAE (Mean Absolute Error):** mengukur rata-rata kesalahan absolut prediksi.
- **RMSE (Root Mean Squared Error):** mengukur kesalahan prediksi dengan penalti lebih besar untuk kesalahan yang besar.
- **R² (Coefficient of Determination):** mengukur kemampuan model menjelaskan variasi target.

Model terbaik ditentukan berdasarkan nilai MAE terendah pada data pengujian.

## Struktur Repository

```text
london-weather-regression/
├── London_Weather_Regression.ipynb
├── london_weather_data_1979_to_2023.csv
├── requirements.txt
└── README.md
```

## Cara Menjalankan

1. Unduh atau clone repository ini.
2. Instal library yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

3. Pastikan file CSV berada di folder yang sama dengan notebook.
4. Buka notebook menggunakan Jupyter Notebook atau JupyterLab.
5. Jalankan cell secara berurutan.

## Catatan

Hasil evaluasi model ditentukan berdasarkan data dan proses eksperimen yang dijalankan. Performa masing-masing algoritma perlu dilihat dari hasil evaluasi aktual, bukan diasumsikan sebelumnya.