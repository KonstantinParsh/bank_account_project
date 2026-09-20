from src.bank_account.account import BankAccount
import pytest


@pytest.fixture
def account_with_balance():
    """Фикстура для создания счета с начальным балансом"""
    return BankAccount("Test", 1000.0)


@pytest.fixture
def empty_account():
    """Фикстура для создания счета с нулевым балансом"""
    return BankAccount("Empty", 0.0)