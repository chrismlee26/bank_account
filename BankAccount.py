import random


class BankAccount:
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self.account_number = random.randint(100000000, 999999999)
        self.routing_number = 631492825
        self.balance = balance

    def deposit(self, amount):
        self.amount = 0
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            self.balance -= 10
            print("Insufficient Funds.")
        print(f"Amount Withdrawn: ${amount}")

    def get_balance(self):
        print(f"Balance: {self.balance}")

    def add_interest(self):
        self.interest = self.balance * 0.00083
        print(f"Interest: ${self.interest}")

    def print_receipt(self):
        print(f"{self.full_name}\nAccount No.: {self.account_number}\nRouting No.:{self.routing_number}\nBalance: ${self.balance}")


print("-----Example #1-----")
chris = BankAccount("chris", 12)
chris.deposit(5000)
chris.print_receipt()
print("-----Example #2-----")
bob = BankAccount("bob", 400)
bob.deposit(100)
bob.withdraw(600)
bob.print_receipt()
print("-----Example #3-----")
bone = BankAccount("bone", 50)
bone.add_interest()
bone.print_receipt()
