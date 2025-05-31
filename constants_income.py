from enum import IntEnum, StrEnum
from typing import Self


class AccountType(IntEnum):
    CURRENCY_USD = USD
    CURRENCY_UAH = UAH
    CURRENCY_CARD = CARD_DEBIT
