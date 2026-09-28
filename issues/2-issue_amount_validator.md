# [Feature] Validasi Nominal Transaksi

## Deskripsi

Setelah nomor rekening divalidasi, sistem juga harus memastikan nominal transaksi berada dalam batas yang diizinkan bank. Nominal nol, negatif, atau melebihi limit harian tidak boleh diproses karena dapat menimbulkan kerugian maupun penyalahgunaan.

## Alur Kerja Git & GitHub Issue

Alur yang harus diikuti: **issue -> branch -> implementasi -> commit -> pull request -> ci -> merge**.

1. **Buat GitHub Issue** menggunakan [GitHub CLI](https://cli.github.com/) (`gh`) berdasarkan dokumen ini:

   ```bash
   gh issue create \
     --title "[Feature] Validasi Nominal Transaksi" \
     --body-file issues/2-issue_amount_validator.md \
     --label "feature"
   ```

   Catat nomor issue yang dihasilkan (misal `#2`), lalu gunakan nomor tersebut pada branch dan pesan commit.

2. **Buat branch baru** dari `main` dengan format `feature/issue-2-amount-validator`:

   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/issue-2-amount-validator
   ```

## Tugas

1. Buat sebuah fungsi `is_amount_valid(amount: int | float) -> bool` di dalam `src/main.py`.
2. Nominal dianggap valid jika berada dalam rentang **Rp10.000 sampai Rp50.000.000** (inklusif).
3. Fungsi harus menolak input yang bukan angka (misal string) serta nilai `bool` (ingat: di Python `True` adalah turunan `int`).
4. Simpan batas minimum dan maksimum sebagai konstanta (misal `MIN_NOMINAL` dan `MAX_NOMINAL`), bukan _magic number_ di dalam fungsi.

## Kriteria Penerimaan SQA (Acceptance Criteria)

Buat _Unit Test_ di `tests/test_main.py` menggunakan `pytest.mark.parametrize` yang mencakup:

- **Positive Case:** `10000` (batas bawah), `250000`, `50000000` (batas atas) (Harus `True`)
- **Negative Case:** `0`, `-5000`, `9999` (di bawah batas), `50000001` (di atas batas), `"10000"` (string), `True` (bool) (Harus `False`)

## Instruksi CI/CD

Pastikan Anda menjalankan `uv run pytest` di lokal Anda sebelum membuat _Pull Request_. Pipeline GitHub Actions harus hijau (lulus tes).

Setelah implementasi selesai:

1. `git add . && git commit -m "feat: tambah validasi nominal transaksi"`
2. `git push origin feature/issue-2-amount-validator`
3. Buka _Pull Request_ dari branch tersebut ke `main`.
4. Tunggu pipeline CI (GitHub Actions) berjalan dan pastikan statusnya **hijau/lulus**.
5. Setelah PR di-_review_ dan CI lulus, lakukan _merge_ ke `main`.
