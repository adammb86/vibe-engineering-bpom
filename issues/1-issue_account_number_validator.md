# [Feature] Validasi Nomor Rekening

## Deskripsi

Sistem transaksi perbankan kita belum memiliki validasi apa pun terhadap input pengguna. Langkah pertama adalah memastikan nomor rekening tujuan yang dimasukkan memiliki format yang benar sebelum transaksi diproses, agar tidak terjadi salah transfer akibat salah ketik.

## Alur Kerja Git & GitHub Issue

Alur yang harus diikuti: **issue -> branch -> implementasi -> commit -> pull request -> ci -> merge**.

1. **Buat GitHub Issue** menggunakan [GitHub CLI](https://cli.github.com/) (`gh`) berdasarkan dokumen ini:

   ```bash
   gh issue create \
     --title "[Feature] Validasi Nomor Rekening" \
     --body-file issues/1-issue_account_number_validator.md \
     --label "feature"
   ```

   Catat nomor issue yang dihasilkan (misal `#1`), lalu gunakan nomor tersebut pada branch dan pesan commit.

2. **Buat branch baru** dari `main` dengan format `feature/issue-1-account-number-validator`:

   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/issue-1-account-number-validator
   ```

## Tugas

1. Buat sebuah fungsi `is_account_number_valid(account_number: str) -> bool` di dalam `src/main.py`.
2. Nomor rekening dianggap valid jika **tepat 10 karakter** dan **hanya berisi digit angka** (`0-9`). Angka nol di depan tetap diperbolehkan. Anda bisa menggunakan _Regular Expression_ (Regex), misalnya `^\d{10}$`.

## Kriteria Penerimaan SQA (Acceptance Criteria)

Buat _Unit Test_ di `tests/test_main.py` menggunakan `pytest.mark.parametrize` yang mencakup:

- **Positive Case:** `1234567890`, `0012345678` (Harus `True`)
- **Negative Case:** `123456789` (9 digit), `12345678901` (11 digit), `12345abcde` (mengandung huruf), `1234 56789` (mengandung spasi), `-123456789` (mengandung simbol), `""` (string kosong) (Harus `False`)

## Instruksi CI/CD

Pastikan Anda menjalankan `uv run pytest` di lokal Anda sebelum membuat _Pull Request_. Pipeline GitHub Actions harus hijau (lulus tes).

Setelah implementasi selesai:

1. `git add . && git commit -m "feat: tambah validasi nomor rekening"`
2. `git push origin feature/issue-1-account-number-validator`
3. Buka _Pull Request_ dari branch tersebut ke `main`.
4. Tunggu pipeline CI (GitHub Actions) berjalan dan pastikan statusnya **hijau/lulus**.
5. Setelah PR di-_review_ dan CI lulus, lakukan _merge_ ke `main`.
