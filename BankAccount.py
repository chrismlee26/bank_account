import random


class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        balance = 0

    def deposit(amount):
        deposit += amount
        return f"Amount Deposited: ${amount}"

    def withdraw(amount):
        balance -= amount
        if balance < amount:
            balance -= 10
            print("Insufficient Funds.")
        return f"Amount Withdrawn: ${amount}"

    def get_balance():
        print(f"Balance: {balance} ")
