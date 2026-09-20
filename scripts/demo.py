from src.bank_account.account import BankAccount
from src.bank_account.exceptions import (
InsufficientFundsError,
InvalidAmountError,
NegativeInitialBalanceError
)
import time


def animate_loading(text: str):
    print(text, end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()


def main():
    print("-==- ДЕМОНСТРАЦИЯ РАБОТЫ БАНКОВСКОГО СЧЕТА -==-\n")

    print("\n---+ СОЗДАНИЕ СЧЕТА И БАЗОВЫЕ ДЕЙСТВИЯ +---\n")
    account = BankAccount("Иван", 100.0)
    print(f"Владелец: {account.get_holder()}")
    print(f"Баланс: {account.get_balance()}")

    # пополнение
    animate_loading("Идет пополнение баланса на 500.0 руб.")
    account.deposit(500.0)
    print(f"Успешно! Текущий баланс: {account.get_balance()}")

    # снятие
    animate_loading("Идет снятие 200.0 руб. с баланса")
    account.withdraw(200.0)
    print(f"Успешно! Текущий баланс: {account.get_balance()}")


    print("\n--++ ПРОВЕРКА ИСКЛЮЧЕНИЙ ++--\n")

    # Ошибка 1: Попытка снять больше, чем есть
    print("Тест #1: Снятие суммы, превышающей баланс (1000.0)")
    try:
        animate_loading("Идет снятие 1000.0 руб. с баланса")
        account.withdraw(1000.0)
    except InsufficientFundsError as e:
        print(f"Ошибка: {e}")

    # Ошибка 2: Передача отрицательной суммы
    print("Тест #2: Пополнение на отрицательную сумму (-50.0)")
    try:
        animate_loading("Идет пополнение баланса на -50.0 руб.")
        account.withdraw(-50.0)
    except InvalidAmountError as e:
        print(f"Ошибка: {e}")

    # Ошибка 3: Создание счета с отрицательным балансом
    print("Тест #3: Создание счета с балансом -500.0 руб.")
    try:
        bad_account = BankAccount("Андрей", -500.0)
    except NegativeInitialBalanceError as e:
        print(f"Ошибка: {e}")


    print("\n-==- ДЕМОНСТРАЦИЯ УСПЕШНО ЗАВЕРШЕНА -==-")



if __name__ == "__main__":
    main()