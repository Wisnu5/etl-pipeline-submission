# 🧩 ETL Pipeline Submission

Proyek ini adalah implementasi pipeline ETL (Extract, Transform, Load) yang dikembangkan untuk submission Dicoding. Pipeline ini mengekstrak data produk dari `fashion-studio.dicoding.dev`, melakukan transformasi sesuai kebutuhan, dan memuat hasilnya ke dalam file CSV, Google Sheets, dan database PostgreSQL.

---

## 🗂️ Struktur Proyek

```
submission-pemda/
├── main.py                   # Script utama untuk menjalankan pipeline ETL
├── requirements.txt          # Daftar dependensi Python
├── submission.txt            # Instruksi untuk menjalankan pipeline & pengujian
├── products.csv              # Output data hasil transformasi dalam format CSV
├── google-sheets-api.json    # Kredensial Google API (tidak diunggah ke GitHub)
├── utils/                    # Modul fungsional untuk ETL
│   ├── __init__.py
│   ├── extract.py            # Modul ekstraksi data
│   ├── transform.py          # Modul transformasi data
│   ├── load.py               # Modul pemuatan data
├── tests/                    # Modul pengujian unit
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
```

---

## 🧰 Persyaratan

Pastikan kamu telah menginstal:

1. **Python 3.11** atau versi terbaru
2. **PostgreSQL** (dengan database bernama `etl_submission` dan user `postgres`)
3. **Kredensial Google Cloud**: file `google-sheets-api.json` dari Google Cloud Console dengan Google Sheets & Drive API aktif

---

## ⚙️ Setup Proyek

1. **Clone Repository:**
   ```bash
   git clone https://github.com/username/etl-pipeline-submission.git
   cd submission-pemda
   ```

2. **Buat & Aktifkan Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/macOS
   venv\Scripts\activate        # Windows
   ```

3. **Install Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Siapkan Database PostgreSQL:**
   ```bash
   psql -U postgres
   ```

5. **Buat Database:**
   ```sql
   CREATE DATABASE etl_submission;
   ```

---

## 🚀 Menjalankan Pipeline

1. **Jalankan Pipeline:**
   ```bash
   python main.py
   ```

2. **Menjalankan Unit Test:**
   ```bash
   pytest tests
   ```

3. **Menjalankan Test dengan Coverage:**
   ```bash
   coverage run -m pytest tests
   coverage report
   ```

---
## Kontribusi
Terbuka untuk kontribusi! Jika ingin berkontribusi, silakan buat pull request dan jelaskan perubahan yang Anda lakukan secara jelas.
