class BankAccountError(Exception):
    """Базовое исключение для всех ошибок банковского счета."""


class NegativeInitialBalanceError(BankAccountError):
    """Выбрасывается при попытке создать счет с отрицательным начальным балансом."""

    def __init__(self, initial_balance: float) -> None:
        if initial_balance >= 0:
            raise ValueError(
                "NegativeInitialBalanceError можно поднимать только для "
                f"отрицательного баланса, получено: {initial_balance}"
            )
        self.initial_balance = initial_balance
        message = (
            "Начальный баланс не может быть отрицательным "
            f"(передано: {initial_balance})."
        )
        super().__init__(message)


class InvalidAmountError(BankAccountError):
    """Выбрасывается, если сумма операции (пополнения или снятия) <= 0."""

    def __init__(self, amount: float, operation: str = "операции") -> None:
        if amount > 0:
            raise ValueError(
                "InvalidAmountError можно поднимать только для суммы <= 0, "
                f"получено: {amount}"
            )
        self.amount = amount
        self.operation = operation
        message = f"Сумма {operation} должна быть больше нуля (передано: {amount})."
        super().__init__(message)


class InsufficientFundsError(BankAccountError):
    """Выбрасывается при попытке снять сумму, превышающую текущий баланс."""

    def __init__(self, amount: float, balance: float) -> None:
        if amount <= balance:
            raise ValueError(
                "InsufficientFundsError можно поднимать только когда "
                f"amount > balance, получено amount={amount}, balance={balance}"
            )
        self.amount = amount
        self.balance = balance
        self.shortfall = amount - balance
        message = (
            f"Недостаточно средств. Запрошено: {amount} руб., "
            f"доступно: {balance} руб."
        )
        super().__init__(message)