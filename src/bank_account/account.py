from src.bank_account.exceptions import (
    InvalidAmountError,
    NegativeInitialBalanceError,
    InsufficientFundsError,
)
from core.config import logger


class BankAccount:
    # инициализация баланса
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        """Создает экземпляр банковского счета.

        :param account_holder: Имя владельца счета.
        :param initial_balance: Начальный баланс (по умолчанию 0.0).
        :raises NegativeInitialBalanceError: Если начальный баланс меньше 0.
        """
        self._holder = account_holder

        try:
            if initial_balance < 0:
                raise NegativeInitialBalanceError(initial_balance)
            self._balance = initial_balance
            logger.info(
                f"Создан счет для владельца '{self._holder}' с начальным балансом {self._balance} руб."
            )
        except NegativeInitialBalanceError as e:
            logger.error(
                f"Ошибка при создании счета для '{account_holder}': {e}"
            )
            raise

    # пополнение и снятие средств
    def deposit(self, amount: float):
        """Пополняет счет на указанную сумму.

        :param amount: Сумма пополнения (должна быть > 0).
        :raises InvalidAmountError: Если сумма пополнения <= 0.
        """
        try:
            if amount <= 0:
                raise InvalidAmountError(amount, operation="пополнения")
            self._balance += amount
            logger.info(
                f"Счет '{self._holder}' пополнен на {amount} руб. Текущий баланс: {self._balance} руб."
            )
            return self._balance
        except InvalidAmountError as e:
            logger.error(
                f"Ошибка пополнения счета '{self._holder}': {e}"
            )
            raise

    def withdraw(self, amount: float):
        """Снимает указанную сумму со счета.

        :param amount: Сумма для снятия (должна быть > 0 и <= баланса).
        :raises InvalidAmountError: Если сумма снятия <= 0.
        :raises InsufficientFundsError: Если сумма снятия превышает баланс.
        """
        try:
            if amount <= 0:
                raise InvalidAmountError(amount, operation="снятия")

            if amount > self._balance:
                raise InsufficientFundsError(amount, self._balance)

            self._balance -= amount
            logger.info(
                f"Со счета '{self._holder}' снято {amount} руб. Текущий баланс: {self._balance} руб."
            )
            return self._balance

        except (InvalidAmountError, InsufficientFundsError) as e:
            logger.error(
                f"Ошибка снятия со счета '{self._holder}': {e}"
            )
            raise

    # возврат баланса и имени владельца
    def get_balance(self):
        """Возвращает текущий баланс счета."""
        return self._balance

    def get_holder(self):
        """Возвращает имя владельца счета."""
        return self._holder

    # строковое представление
    def __str__(self):
        """Строковое представление счета для пользователя."""
        return f"Владелец: {self._holder}\nБаланс: {self._balance}"

    def __repr__(self):
        """Официальное строковое представление для отладки."""
        return f"Holder: {self._holder}\nBalance: {self._balance}"