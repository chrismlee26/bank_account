import random

# This is the class that initializes the BankAccount object


class BankAccount:
    # @params: "Full Name" & Balance (default is 0)
    def __init__(self, full_name, balance=0):
        self.full_name = full_name
        # This needs to censor the first few digits with ***
        self.account_number = random.randint(10000000, 99999999)
        self.routing_number = 631492825
        self.balance = balance

    # deposit function
    # @params: amount, given by user, 0 is default
    def deposit(self, amount=0):
        self.amount = amount
        self.balance += amount  # Amount is added to balance
        print(f"Amount Deposited: ${amount}")

    # withdraw function
    # @ params: amount, given by user, 0 is default
    def withdraw(self, amount=0):
        self.balance -= amount
        # Maybe we can add in functionality that will allow overdraft up do a specific number then just reject.
        if self.balance < amount:
            self.balance -= 10
            print("Insufficient Funds. Overdraft Fee of $10 has been charged.")
        print(f"Amount Withdrawn: ${amount}")

    def get_balance(self):
        # Missing a return value?
        print(f"Hi beautiful, your balance is: {self.balance}")

    # This needs to add to balance immediately when the class is created. Strange but ok.
    def add_interest(self):
        self.interest = self.balance * 0.00083
        print(f"Interest: ${self.interest}")

    def print_receipt(self):
        print(f"Name: {self.full_name}\nAccount No.: {self.account_number}\nRouting No.:{self.routing_number}\nBalance: ${self.balance}")


print("-----Example #1-----")
chris = BankAccount("Chris Lee")
chris.deposit(5000)
chris.print_receipt()
print("-----Example #2-----")
pringles = BankAccount("Pringles Dog")
pringles.deposit(550)
pringles.withdraw(600)
pringles.print_receipt()
print("-----Example #3-----")
bone = BankAccount("Bone Bone")
bone.get_balance()
bone.add_interest()
bone.print_receipt()


# Add more things to Readme
# Add comments in code
# Initial balance should start at 0
# self.amount = 0 does nothing, can remove
# check withdraw before deposit -- maybe add an if function to now allow
# get_balance has no return value
# balance needs to update to add interest
# print_receipt needs to hide first ##'s in the account_number
