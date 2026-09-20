from src.bank_account.account import BankAccount
from src.bank_account.exceptions import (
    InsufficientFundsError,
    InvalidAmountError,
    NegativeInitialBalanceError
)
import pytest


# Создание счета
@pytest.mark.smoke
def test_create_account_with_positive_balance():
    """Тестирует создание счета с положительным начальным балансом."""
    account = BankAccount("Test", 1000.0)
    assert account.get_holder() == "Test"
    assert account.get_balance() == 1000.0

def test_create_account_with_zero_balance():
    """Тестирует создание счета с нулевым начальным балансом."""
    account = BankAccount("Empty")
    assert account.get_holder() == "Empty"
    assert account.get_balance() == 0.0

@pytest.mark.regression
def test_create_account_with_negative_balance():
    """Тестирует создание счета с отрицательным начальным балансом."""
    with pytest.raises(NegativeInitialBalanceError, match="не может быть отрицательным"):
        BankAccount("Negative", -100.0)


# Пополнение счета
@pytest.mark.smoke
def test_deposit_positive_amount(account_with_balance):
    """Тестирует пополнение счета положительной суммой."""
    new_balance = account_with_balance.deposit(500.0)
    assert new_balance == 1500.0
    assert account_with_balance.get_balance() == 1500.0

def test_deposit_negative_amount(account_with_balance):
    """Тестирует пополнение счета отрицательной суммой."""
    with pytest.raises(InvalidAmountError, match="должна быть больше нуля"):
        account_with_balance.deposit(-50.0)


# Снятие со счета
@pytest.mark.smoke
def test_withdraw_valid_amount(account_with_balance):
    """Тестирует снятие допустимой суммы со счета."""
    new_balance = account_with_balance.withdraw(300.0)
    assert new_balance == 700.0
    assert account_with_balance.get_balance() == 700.0

@pytest.mark.parametrize("amount", [1500.0, 2000.0, 10000.0])
def test_withdraw_insufficient_funds(account_with_balance, amount):
    """Тестирует снятие суммы, превышающей баланс счета."""
    with pytest.raises(InsufficientFundsError, match="Недостаточно средств"):
        account_with_balance.withdraw(amount)

@pytest.mark.parametrize("amount", [-100.0, -50.0, -1.0])
def test_withdraw_negative_amount(account_with_balance, amount):
    """Тестирует снятие отрицательной суммы со счета."""
    with pytest.raises(InvalidAmountError, match="должна быть больше нуля"):
        account_with_balance.withdraw(amount)


# Геттеры и строки
def test_get_holder_and_balance(account_with_balance):
    """Тестирует методы получения имени владельца и баланса счета."""
    assert account_with_balance.get_holder() == "Test"
    assert account_with_balance.get_balance() == 1000.0

def test_account_str_representation(account_with_balance):
    """Тестирует строковое представление счета."""
    assert str(account_with_balance) == "Владелец: Test\nБаланс: 1000.0"

def test_account_repr_representation(account_with_balance):
    """Тестирует официальное строковое представление счета."""
    assert repr(account_with_balance) == "Holder: Test\nBalance: 1000.0"


# Тест на последовательность операций
def test_sequence_of_operations(empty_account):
    """Тестирует последовательность операций: пополнение, снятие, пополнение."""
    empty_account.deposit(1000.0)
    empty_account.withdraw(200.0)
    empty_account.deposit(300.0)
    assert empty_account.get_balance() == 1100.0
    