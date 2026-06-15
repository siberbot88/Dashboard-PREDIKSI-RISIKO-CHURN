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

## Metodologi dan Hasil Analisis
### Teknologi dan Algoritma
- **Bahasa dan Pustaka** : Python, Pandas, Scikit-Learn, Matplotlib.
- **Algoritma Model** : Random Forest Classifier.
- **Platform Antarmuka** : Streamlit.

### Tahapan Proses (Pipeline)
1. **Pembersihan Data (Data Cleaning)** : Penanganan nilai kosong dan standardisasi format data.
2. **Exploratory Data Analysis (EDA)** : Pencarian pola dan korelasi antara variabel demografis dan persepsi layanan terhadap status *churn*.
3. **Pemodelan Machine Learning** : Pengujian dan komparasi berbagai algoritma (Decision Tree, KNN, Logistic Regression, Random Forest).
4. **Penilaian Risiko (Risk Scoring & Segmentation)** : Perhitungan probabilitas churn dan pengelompokan pelanggan (High, Medium, Low Risk) berdasarkan batas persentil statistik.
5. **Penentuan Reason Code** : Ekstraksi variabel paling bermasalah pada masing-masing pelanggan (contoh: *Time Risk*, *Promo Risk*).
6. **Perumusan Strategi (CRAM)** : Pemetaan pelanggan ke tindakan nyata berbasis profil risiko.

### Ringkasan Temuan
Model Random Forest terbukti memberikan metrik evaluasi terbaik (F1-Score: 0.818). Hasil prediksi menunjukkan bahwa sekitar 14% dari pelanggan masuk ke dalam kategori **High Risk** (risiko tinggi untuk churn). Mayoritas pelanggan berisiko tinggi tersebut masuk ke dalam segmen **Time Risk**, yang mengindikasikan bahwa keterlambatan pengiriman dan hilangnya penghematan waktu adalah alasan utama ketidakpuasan. Strategi retensi difokuskan pada perbaikan SLA waktu pengantaran, kompensasi keterlambatan, serta peningkatan efisiensi layanan secara keseluruhan.


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
