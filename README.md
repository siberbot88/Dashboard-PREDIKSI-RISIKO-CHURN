# Prediksi Risiko Churn dan Strategi CRM Layanan Food Delivery

## Deskripsi Proyek
Proyek ini dikembangkan untuk memprediksi probabilitas berhenti berlangganan (churn) dari pelanggan layanan pesan antar makanan (food delivery). Pendekatan yang digunakan mencakup pemodelan machine learning (Random Forest) untuk mengidentifikasi pemicu utama churn, segmentasi profil risiko pelanggan, serta perumusan langkah taktis Customer Relationship Management (CRM) melalui kerangka Customer Retention Action Matrix (CRAM).

## Struktur Direktori
- `app.py` : Berkas utama untuk eksekusi antarmuka dashboard interaktif berbasis Streamlit.
- `data/` : Direktori penyimpanan dataset mentah serta dataset hasil pemrosesan.
- `notebooks/` : Memuat dokumen Jupyter Notebook yang mendokumentasikan alur kerja dari pembersihan data, Exploratory Data Analysis (EDA), pelatihan model, hingga penyusunan matriks CRM.
- `outputs/` : Direktori luaran untuk model yang telah dilatih, metrik evaluasi, daftar prioritas pelanggan, serta visualisasi data.
- `reports/` : Berisi catatan analisis, struktur proyek, dan laporan akhir hasil temuan.
- `requirements.txt` : Daftar dependensi pustaka Python yang dibutuhkan oleh aplikasi.

## Fitur Utama Aplikasi
1. **Prediksi dan Segmentasi Risiko** : Menampilkan distribusi probabilitas pelanggan yang terbagi dalam kategori High Risk, Medium Risk, dan Low Risk.
2. **Analisis Kepentingan Fitur (Feature Importance)** : Mengidentifikasi variabel yang memiliki pengaruh terbesar terhadap keputusan pelanggan untuk tidak melakukan pembelian ulang.
3. **Daftar Prioritas Pelanggan (Customer Priority Table)** : Mengurutkan pelanggan berdasarkan skor risiko beserta alasan spesifik (Reason Code) untuk setiap individu.
4. **Strategi CRM (CRM Strategy Matrix)** : Rekomendasi aksi retensi pelanggan beserta kanal komunikasi yang dianjurkan sesuai dengan profil risiko pelanggan.

## Panduan Instalasi dan Penggunaan Lokal
1. Pastikan lingkungan Python telah terpasang.
2. Instal seluruh dependensi yang diperlukan dengan menjalankan perintah:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan dashboard secara lokal dengan perintah:
   ```bash
   streamlit run app.py
   ```

## Lingkungan Deployment
Aplikasi ini telah disesuaikan dengan standar *relative path* agar dapat langsung diterapkan (deploy) menggunakan layanan Streamlit Community Cloud dengan merujuk pada repositori GitHub.
