from typing import Type, Self
from uuid import uuid4
from abc import ABC, abstractmethod

from constants_bank import AccountType, ClientType


class Client:
    def __init__(self, name: str, client_type: ClientType):
        self.name = name.title().strip()
        self.type = client_type
        self.accounts: list["Account"] = []

    def __str__(self):
        return f"<Client {self.name}, {self.type}"


class Account(ABC):
    @abstractmethod
    def __str__(self):
        pass

    def __init__(self, account_type: AccountType, client: Client, bank: "Bank"):
        self.type = account_type
        self.client = client
        self.id = uuid4()
        self.__balance = 0
        self.bank = bank

    @property
    def balance(self):
        return self.__balance


class DepositAccount(Account):
    def __str__(self) -> str:
        return f"<DepositAccount: {self.id.hex} in {self.bank}>"

    def __init__(self, account_type: AccountType, client: Client, bank: "Bank"):
        if not AccountType.is_debit_type(account_type):
            raise ValueError("Incorrect account type provided")
        super().__init__(account_type, client, bank)


class CreditAccount(Account):
    def __str__(self):
        return f"<CreditAccount: {self.id.hex} belongs to {self.client} in {self.bank}>"

    def __init__(self, account_type: AccountType, client: Client, bank: "Bank"):
        if AccountType.is_debit_type(account_type):
            raise ValueError("Incorrect account type provided")
        super().__init__(account_type, client, bank)

        max_loan = 100_000 if client.type == ClientType.PERSON else 1_000_000
        self.max_loan = max_loan


class Bank:
    def __init__(self, name: str):
        self.name = name.upper()
        self.accounts: list[Account] = []

    def __str__(self) -> str:
        return f"<Bank: '{self.name}'>"

    def open_account(self, client: Client, account_type: AccountType) -> Account:
        # if AccountType.is_debit_type(account_type):
        #     account = DepositAccount(account_type=account_type, client=client)
        # else:
        #     account = CreditAccount(account_type=account_type, client=client)
        account_class: Type[Account] = (
            # account_class: DepositAccount | CreditAccount = (
            DepositAccount
            if AccountType.is_debit_type(account_type)
            else CreditAccount
        )
        account = account_class(account_type=account_type, client=client, bank=self)
        self.accounts.append(account)
        client.accounts.append(account)
        self._operate_files()
        return account

    __repr__ = __str__

    def __eq__(self, other: Self):
        return len(self.accounts) == len(other.accounts)

    def __gt__(self, other):
        return len(self.accounts) > len(other.accounts)

    def __ge__(self, other):
        return len(self.accounts) >= len(other.accounts)

    def _operate_files(self):
        print("operate files")
