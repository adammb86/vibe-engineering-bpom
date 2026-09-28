# [Security] Hashing PIN Transaksi

## Deskripsi

PIN transaksi adalah kredensial paling sensitif dalam sistem perbankan. Menyimpan PIN dalam bentuk _plain text_ adalah celah keamanan fatal (OWASP Top 10 – _Cryptographic Failures_). PIN harus divalidasi formatnya lalu di-_hash_ dengan algoritma yang aman sebelum nantinya disimpan ke dalam _database_.

## Alur Kerja Git & GitHub Issue

Alur yang harus diikuti: **issue -> branch -> implementasi -> commit -> pull request -> ci -> merge**.

1. **Buat GitHub Issue** menggunakan [GitHub CLI](https://cli.github.com/) (`gh`) berdasarkan dokumen ini:

   ```bash
   gh issue create \
     --title "[Security] Hashing PIN Transaksi" \
     --body-file issues/3-issue_pin_hash.md \
     --label "security"
   ```

   Catat nomor issue yang dihasilkan (misal `#3`), lalu gunakan nomor tersebut pada branch dan pesan commit.

2. **Buat branch baru** dari `main` dengan format `feature/issue-3-pin-hash`:

   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/issue-3-pin-hash
   ```

## Tugas

1. Pastikan pustaka `bcrypt` sudah terdaftar di dependensi proyek (jika belum, tambahkan dengan `uv add bcrypt`).
2. Buat fungsi `hash_pin(pin: str) -> str` di dalam `src/main.py`:
   - PIN wajib **tepat 6 digit angka**; jika tidak, fungsi harus melempar `ValueError`.
   - Gunakan `bcrypt.hashpw` dengan _salt_ dari `bcrypt.gensalt()`.
3. Buat fungsi `verify_pin(plain_pin: str, hashed_pin: str) -> bool` menggunakan `bcrypt.checkpw`.

## Kriteria Penerimaan SQA (Acceptance Criteria)

Buat _Unit Test_ di `tests/test_main.py` untuk memastikan:

- Hasil dari `hash_pin` tidak sama dengan PIN aslinya.
- Dua kali pemanggilan `hash_pin` dengan PIN yang sama menghasilkan _hash_ yang berbeda (membuktikan penggunaan _salt_).
- Fungsi `verify_pin` mengembalikan `True` jika disuntikkan PIN asli dan _hash_-nya.
- Fungsi `verify_pin` mengembalikan `False` jika disuntikkan PIN yang salah.
- Gunakan `pytest.mark.parametrize` dan `pytest.raises(ValueError)` untuk PIN tidak valid: `12345` (5 digit), `1234567` (7 digit), `12ab56` (mengandung huruf).

## Instruksi CI/CD

Pastikan Anda menjalankan `uv run pytest` di lokal Anda sebelum membuat _Pull Request_. Pipeline GitHub Actions harus hijau (lulus tes).

Setelah implementasi selesai:

1. `git add . && git commit -m "feat: tambah hashing PIN transaksi"`
2. `git push origin feature/issue-3-pin-hash`
3. Buka _Pull Request_ dari branch tersebut ke `main`.
4. Tunggu pipeline CI (GitHub Actions) berjalan dan pastikan statusnya **hijau/lulus**.
5. Setelah PR di-_review_ dan CI lulus, lakukan _merge_ ke `main`.
