import pytest

from Final_Project import Account


def test_deposit():
    account = Account(0)
    account.deposit(50)
    assert account.balance == 50


def test_withdraw():
    account = Account(150)
    account.withdraw(99)
    assert account.balance == 51


def test_withdraw_overdraft():
    account = Account(150)
    with pytest.raises(RuntimeError):
        account.withdraw(160)
    assert account.balance == 150


from Final_Project import Credit


def test_withdraw_c():
    credit_account = Credit(0.1, 1000)
    credit_account.withdraw(100)
    assert credit_account.balance == -110


def test_withdraw_overdraft_c():
    credit_account = Credit(20, 500)
    with pytest.raises(RuntimeError):
        credit_account.withdraw(700)
    assert credit_account.balance == 0


def test_deposit_c():
    credit_account = Credit(0.05, 1000)
    with pytest.raises(RuntimeError):
        credit_account.deposit(400)
    assert credit_account.balance == 0


from Final_Project import Saving


def test_add_interest():
    saving_account = Saving(0.15)
    saving_account.balance = 150
    saving_account.add_interest()
    assert saving_account.balance == 172.5

from Final_Project import Debit

def test_transfer_d():
    debit_account = Debit()
    credit_account = Credit(0.05, 1000)
    debit_account.deposit(500)
    credit_account.withdraw(600)
    result_success = debit_account.transfer(credit_account, 300)
    assert debit_account.balance == 200
    






if __name__ == '__name__':
    pytest.main()
