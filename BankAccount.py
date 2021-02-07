import random


class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = "full_name"
        self.account_number = random.randint(100000000, 999999999)
        self.routing_number = routing_number
        self.balance = 0

    def deposit(self, amount, balance):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

    def withdraw(self, amount, balance):
        self.balance -= amount
        if self.balance < amount:
            self.balance -= 10
            print("Insufficient Funds.")
        print(f"Amount Withdrawn: ${amount}")

    def get_balance(self, balance):
        print(f"Balance: {balance} ")

    def add_interest(self, interest, balance):
        self.interest = self.balance * 0.083

    def print_receipt(self, full_name, account_number, routing_number, balance):
        print(f"{full_name}\nAccount No.: {account_number}\nRouting No.:{routing_number}\nBalance: ${balance}")


chris = BankAccount("asdfg asdfg", 12345, 12345, 12)
print(chris)
