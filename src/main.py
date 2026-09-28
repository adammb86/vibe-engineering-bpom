"""Aplikasi FastAPI untuk layanan transaksi perbankan.

Kerangka awal; fitur ditambahkan bertahap sesuai GitHub Issue yang sudah divalidasi.
"""

import re

ACCOUNT_NUMBER_PATTERN = re.compile(r"[0-9]{10}")


def is_account_number_valid(account_number: str) -> bool:
    """Nomor rekening valid jika tepat 10 digit angka (0-9)."""
    if not isinstance(account_number, str):
        return False
    return ACCOUNT_NUMBER_PATTERN.fullmatch(account_number) is not None
