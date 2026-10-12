# Dasar Dasar Python untuk Analisis Data

Project ini merangkum Module 1 sampai Module 3 dari course Introduction to Data Analysis Using Python (Google Data Analytics Professional Certificate). Semua latihan dijalankan ulang dari awal sampai akhir lewat satu script: `analyze_fundamentals.py`.

## Materi yang dipelajari

1. Sintaks dan tipe data: variabel, string, integer, float, boolean, dan konversi tipe
2. Fungsi: definisi fungsi, parameter, dan nilai kembali
3. Kondisional: percabangan if, elif, dan else
4. While loop: perulangan dengan kondisi, termasuk fungsi timer sederhana
5. For loop: iterasi list, penghitung skor feedback pelanggan, dan validasi ID
6. String: penggabungan, pemotongan, ekstraksi ID toko, dan method string

## Cara menjalankan

```bash
python analyze_fundamentals.py
```

Script akan mencetak semua hasil latihan, menyimpan 4 chart di folder `charts/`, dan menulis ringkasan angka di `findings.json`.

## Hasil utama

* Fungsi `score_counter` mengelompokkan 200 skor feedback jadi 86 negatif, 17 netral, dan 97 positif
* Fungsi `id_validator` menemukan 115 dari 120 ID tidak terverifikasi (95.83 persen)
* Ekstraksi ID toko dari kode "TOKO/042/BALI" menghasilkan "042"

## Struktur folder

* `analyze_fundamentals.py`: script utama berisi semua latihan
* `charts/`: 4 visualisasi hasil latihan
* `data/`: file teks Zen of Python dari materi course
* `findings.json`: ringkasan angka hasil eksekusi
