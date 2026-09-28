# [Database] Integrasi Penyimpanan Transaksi ke MySQL

## Deskripsi

Setelah nomor rekening dan nominal divalidasi serta PIN di-_hash_, data transaksi harus disimpan ke dalam sistem basis data yang persisten agar dapat diaudit. Kita akan menggunakan MySQL untuk kebutuhan ini.

## Alur Kerja Git & GitHub Issue

Alur yang harus diikuti: **issue -> branch -> implementasi -> commit -> pull request -> ci -> merge**.

1. **Buat GitHub Issue** menggunakan [GitHub CLI](https://cli.github.com/) (`gh`) berdasarkan dokumen ini:

   ```bash
   gh issue create \
     --title "[Database] Integrasi Penyimpanan Transaksi ke MySQL" \
     --body-file issues/4-issue_insert_transaction_to_mysql.md \
     --label "database"
   ```

   Catat nomor issue yang dihasilkan (misal `#4`), lalu gunakan nomor tersebut pada branch dan pesan commit.

2. **Buat branch baru** dari `main` dengan format `feature/issue-4-mysql-integration`:

   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/issue-4-mysql-integration
   ```

## Tugas

1. Pastikan `pymysql` sudah terdaftar di dependensi proyek (jika belum, tambahkan dengan `uv add pymysql`).
2. Buat fungsi `simpan_transaksi_ke_db(nomor_rekening: str, nominal: float, hashed_pin: str) -> bool` di `src/main.py`:
   - Validasi `nomor_rekening` dengan `is_account_number_valid` dan `nominal` dengan `is_amount_valid` sebelum menyimpan; kembalikan `False` jika tidak valid.
   - Tolak `hashed_pin` yang bukan _hash_ bcrypt (misal PIN _plain text_ `"123456"`); PIN mentah tidak boleh pernah tersimpan.
   - Gunakan _parameterized query_ (`cursor.execute(sql, params)`) untuk mencegah SQL Injection.
3. Gunakan _Environment Variables_ (`os.getenv`) untuk konfigurasi kredensial _database_ (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`) agar aman.
4. Buat file `docker-compose.yml` untuk memutar _container_ MySQL secara lokal.

## Kriteria Penerimaan SQA (Integration Testing)

- Buat _fixture_ di `pytest` untuk melakukan **Setup** (membuat tabel sementara `transaksi`) dan **Teardown** (menghapus tabel setelah tes selesai).
- Buat tes yang mensimulasikan penyimpanan transaksi valid ke MySQL dan memverifikasi (menggunakan `SELECT`) bahwa data benar-benar tersimpan, termasuk bahwa kolom PIN berisi _hash_, bukan PIN asli.
- Gunakan `pytest.mark.parametrize` untuk data tidak valid (nomor rekening salah, nominal di luar batas, PIN belum di-_hash_): fungsi harus mengembalikan `False` dan tidak ada baris baru di tabel.
- Pastikan _pipeline_ CI di `.github/workflows/ci.yml` diperbarui untuk menggunakan _Service Container_ MySQL.

## Instruksi CI/CD

Pastikan Anda menjalankan `uv run pytest` di lokal Anda (dengan `docker-compose up -d` untuk database) sebelum membuat _Pull Request_. Pipeline GitHub Actions harus hijau (lulus tes).

Setelah implementasi selesai:

1. `git add . && git commit -m "feat: tambah integrasi penyimpanan transaksi ke MySQL"`
2. `git push origin feature/issue-4-mysql-integration`
3. Buka _Pull Request_ dari branch tersebut ke `main`.
4. Tunggu pipeline CI (GitHub Actions) berjalan dan pastikan statusnya **hijau/lulus**.
5. Setelah PR di-_review_ dan CI lulus, lakukan _merge_ ke `main`.
