"""Unit test untuk `main.py`.

Kerangka awal; test ditambahkan bertahap mengikuti tiap GitHub Issue.
"""

import pytest

from main import is_account_number_valid


@pytest.mark.parametrize(
    "account_number",
    ["1234567890", "0012345678"],
)
def test_is_account_number_valid_positive(account_number):
    assert is_account_number_valid(account_number) is True


@pytest.mark.parametrize(
    "account_number",
    [
        "123456789",  # 9 digit
        "12345678901",  # 11 digit
        "12345abcde",  # mengandung huruf
        "1234 56789",  # mengandung spasi
        "-123456789",  # mengandung simbol
        "",  # string kosong
    ],
)
def test_is_account_number_valid_negative(account_number):
    assert is_account_number_valid(account_number) is False


@pytest.mark.parametrize("account_number", [1234567890, None])
def test_is_account_number_valid_non_string(account_number):
    assert is_account_number_valid(account_number) is False
