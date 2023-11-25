class Account:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    # make a deposit
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise RuntimeError('Low balance')

    def __del__(self):
        del self


class Debit(Account):
    def __init__(self):
        super().__init__(0)

    def transfer(self, credit_account, amount):
        try:
            self.withdraw(amount)
            credit_account.deposit(amount)
            return f'The Amount {amount} € is added to your account. Balance: {self.check_balance()} €'
        except Exception as e:
            self.deposit(amount)


class Credit(Account):
    def __init__(self, interest, limit):
        super().__init__(0)
        self.interest = interest
        self.limit = limit

    def withdraw(self, amount):
        if amount <= self.limit - self.balance:
            self.balance -= amount + amount * self.interest
            return f'The Amount {amount} € has been withdrawn from your account. New Balance: {self.check_balance()} €'
        else:
            raise RuntimeError('Overdraft')

    def deposit(self, amount):
        if amount + self.balance <= 0:
            self.balance += amount
            return f'The Amount {amount} € has been credited to your account. New Balance: {self.check_balance()} €'
        else:
            raise RuntimeError('Overpay')


class Saving(Account):
    def __init__(self, interest):
        super().__init__(0)
        self.interest = interest

    def add_interest(self):
        self.balance = self.balance + self.balance * self.interest


if __name__ == '__main__':

    debit_account = Debit()
    print(f'Debit Account. Balance: {debit_account.check_balance()} €')
    debit_account.deposit(1000)
    print(f'The amount has been credit to your account. New Balance: {debit_account.check_balance()} €')

    credit_account = Credit(0.50, 2000)
    credit_account.withdraw(500)
    print(f'The amount has been withdrawn from your account. New Balance: {credit_account.check_balance()} €')
    credit_account.deposit(300)
    print(f'The amount has been credit to your account. New Balance: {credit_account.check_balance()} €')

    saving_account = Saving(0.03)
    saving_account.deposit(1500)
    saving_account.add_interest()
    print(f'Saving Account. Balance: {saving_account.check_balance()} €')
