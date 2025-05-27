from constants_bank import AccountType, ClientType
from models_bank import Bank, Client


def main():
    bank = Bank("All Money of The World")
    bank_2 = Bank("Mono")
    client = Client(name="Bobby", client_type=ClientType.PERSON)
    bank.open_account(client, account_type=AccountType.DEBIT_CARD)
    bank_2.open_account(client, account_type=AccountType.MORTGAGE)

    client_legal = Client(name="HP", client_type=ClientType.LEGAL)
    bank_2.open_account(client_legal, account_type=AccountType.CREDIT)

    # da = DepositAccount(AccountType.DEBIT_CARD, client)
    # ca = CreditAccount(AccountType.CURRENT, client)
    client_legal.accounts = []

    print(bank <= bank_2)

    pass


if __name__ == "__main__":
    main()
