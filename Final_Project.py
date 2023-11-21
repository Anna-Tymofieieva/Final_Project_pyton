from tkinter import *


window = Tk()
window.title("Главное окно")
window.minsize(width=400,height=400)


Entry(window).pack()
Label(window, text="Ввести текст").pack()
Button(window, text="OK").pack()

class Account:
    def __inut__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    # make a deposit
    def deposit(self, amount):
        amount = float(input("Enter amount"))
        self.balance += amount
        return "New Balance {self.balance}"

    # withdraw cash
    def withdraw(self, amount):
        amount = float(input("Enter amount"))
        if amount <= self.balance:
            self.balance -= amount
            return "New Balance {self.balance}"
        else:
            return f"Not enough money! Enter another amount"

    def __del__(self):
        del self


# Class Debit(Account):
    #def __inut__(self, balance):
    #super().__init__()


class Kredit(Account):
    def __init__(self, interest):
        super().__init__()
        self.interest = interest

    def withdraw(self, amount):
        amount = float(input("Enter amount"))
        self.interest = 0.10
        total_amount = amount + amount * self.interest
        if total_amount <= self.balance:
            # n = int(input("Enter the number of payments from 1 to 6")
            # new_amount = total_amount / n
            # return self.balance -= new_amount
            return "New Balance {self.balance} -= {total_amount}"
        else:
            return "Not enough money! Enter another amount"


class Saving(Account):
    def __init__(self, interest):
        super().__init__()
        self.interest = interest

    def calculate_interest(self):
        interest = 0, 5
        return self.balance * interest

    def add_interest(self):
        return "New Balance self.balance + self.calculate_interest()"
window.tk.mainloop()