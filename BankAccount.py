import random

# This is the class that initializes the BankAccount object


class BankAccount:
    # @params: "Full Name" & Balance (default is 0)
    def __init__(self, full_name, balance=0):
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999)
        self.routing_number = 631492825
        self.balance = balance

    # deposit function
    # @params: amount, given by user
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount  # Amount is added to balance
        print(f"Amount Deposited: ${amount}")

    # withdraw function
    # @ params: amount, given by user, 0 is default
    def withdraw(self, amount=0):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")

        elif amount*.9 >= self.balance and amount*1.1 <= self.balance:
            self.balance -= amount + 10
            print("Funds Overdrawn. Overdraft Fee of $10 has been charged.")
            print(f"Amount Withdrawn: ${amount}")

        elif amount*1.1 > self.balance:
            self.balance -= 10
            print("Insufficient Funds. Overdraft Fee of $10 has been charged.")
            print(f"Attempted Withdraw: ${amount}")
            print(f"Amount Withdrawn: $0.00")

    def get_balance(self):
        # Missing a return value?
        print(f"Hi {self.full_name}, your balance is: {self.balance:.2f}")

    def add_interest(self):
        self.interest = self.balance * 0.00083
        self.balance += self.interest
        print(f"Interest: ${self.interest:.2f}")

    def print_receipt(self):
        print(
            f"Name: {self.full_name}\nAccount No.: ****{str(self.account_number)[-4:]}\nRouting No.:{self.routing_number}\nBalance: ${self.balance:.2f}")


print("Transaction 1: Create account, deposit and print_receipt")
print("Transaction 2: Create account, deposit, withdraw (overdraw) and print_receipt")
print("Transaction 3: Create account, get_balance, add_interest and print_receipt", "\n")
print("-----TRANSACTION #1-----")
chris = BankAccount("Chris Lee")
chris.deposit(5000)
print("$$$$$$$$$$ PRINTING RECEIPT $$$$$$$$$")
chris.print_receipt()
print("$$$$$$$$$$ END OF TRANSACTION $$$$$$$$$")
print('\n')
print("-----TRANSACTION #2-----")
pringles = BankAccount("Pringles Dog")
pringles.deposit(550)
pringles.withdraw(10050)
print("$$$$$$$$$$ PRINTING RECEIPT $$$$$$$$$")
pringles.print_receipt()
print("$$$$$$$$$$ END OF TRANSACTION $$$$$$$$$")
print('\n')
print("-----TRANSACTION #3-----")
bone = BankAccount("Bone Bone")
bone.deposit(20)
bone.withdraw(22)
print("########## CHECKING BALANCE ##########")
bone.get_balance()
print('\n')
print("########## CHECKING INTEREST ##########")
bone.add_interest()
print('\n')
print("$$$$$$$$$$ PRINTING RECEIPT $$$$$$$$$")
bone.print_receipt()
print("$$$$$$$$$$ END OF TRANSACTION $$$$$$$$$")


# Add more things to Readme
# Add comments in code
# Initial balance should start at 0
# self.amount = 0 does nothing, can remove
# check withdraw before deposit -- maybe add an if function to now allow
# get_balance has no return value
# balance needs to update to add interest
# print_receipt needs to hide first ##'s in the account_number
