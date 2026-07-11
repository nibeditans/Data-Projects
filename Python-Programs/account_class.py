class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Printing Total Balance
    def print_balance(self):
        print(f"Total Balance: {self.balance} INR.")

    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited.")

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited.")

    # Updating Balance
    def update_balance(self):
        print(f"Total Balance after updation: {self.balance} INR.")

acc1 = Account(10000, 1234567890)
# print(acc1.balance)
# print(acc1.account_no)

acc1.print_balance()
acc1.debit(500)
acc1.credit(20000)
acc1.update_balance()
acc1.debit(5000)
acc1.credit(200000)
acc1.update_balance()
acc1.debit(20000)
acc1.credit(500000)
acc1.update_balance()
