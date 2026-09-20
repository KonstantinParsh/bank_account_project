from datetime import datetime

from src.bank_account.account import BankAccount
from src.bank_account.exceptions import BankAccountError

SEPARATOR = "=" * 50


def print_summary(accounts: dict) -> None:
    """Печатает сводку по всем счетам."""
    print(SEPARATOR)
    print("СВОДКА ПО СЧЕТАМ")
    print(SEPARATOR)
    for account in accounts.values():
        print(f"{account.get_holder()} | {account.get_balance():.2f}")
    print(SEPARATOR)


def main() -> None:
    print(SEPARATOR)
    print("СИСТЕМА СОЗДАНИЯ ТЕСТОВЫХ СЧЕТОВ")
    print(f"Время запуска: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(SEPARATOR)

    accounts = {
        "Alice": BankAccount("Alice", 1000.0),
        "Bob": BankAccount("Bob", 500.0),
        "Charlie": BankAccount("Charlie", 2500.0),
        "Diana": BankAccount("Diana", 750.0),
        "Eve": BankAccount("Eve", 3000.0),
        "Frank": BankAccount("Frank", 100.0),
    }

    print("[1] Начальное состояние:")
    print_summary(accounts)

    print("[2] Выполнение операций:")

    operations = [
        ("Alice", "deposit", 150.50),
        ("Bob", "withdraw", 200.0),
        ("Frank", "withdraw", 500.0),
        ("Eve", "deposit", 450.0),
        ("Charlie", "withdraw", 100.0),
    ]

    for holder, action, amount in operations:
        account = accounts[holder]
        verb = "пополнил" if action == "deposit" else "снял"
        try:
            if action == "deposit":
                account.deposit(amount)
            else:
                account.withdraw(amount)
            print(f"✓ {holder} {verb} на {amount:.2f}")
        except BankAccountError as e:
            print(f"✗ Ошибка у {holder}: {e}")

    print("[3] Итоговое состояние:")
    print_summary(accounts)

    print("✅ Скрипт успешно выполнен!")


if __name__ == "__main__":
    main()