from enum import IntEnum, StrEnum
from typing import Self


class AccountType(IntEnum):
    CURRENT = 0
    DEBIT_CARD = 1
    MORTGAGE = 2
    AUTO_LOAN = 3
    CREDIT = 4

    @classmethod
    def is_debit_type(cls, account_type: Self) -> bool:
        is_debit = account_type in {cls.CURRENT, cls.DEBIT_CARD}
        return is_debit


class ClientType(StrEnum):
    PERSON = "person"
    LEGAL = "legal"
