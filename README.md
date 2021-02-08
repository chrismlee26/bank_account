## Welcome

This project is my bank account program in Python3. The Project encompasses OOP Methods & Attributes as Assignment #1 for CS1.1 (OOP).

## Run

$ "python3 BankAccount.py" to run.
$ Or just press the run button to run.

## Operations

1. Define a **BankAccount** class
2. The class should have the following attributes:

- **full_name** : Full name of Owner
- **account_number** : Randomly generated 8 digit umber. Unique Per Account
- **routing_number** : 9 Digit Number, same for all accounts.
- **balance** : The balance of the account, should start at 0

3. Methods for the BankAccount class:

- **deposit** takes one parameter 'amount' and will add 'amount' to the 'balance'. Prints the message: "Amount Deposited: $X.XX"
- **withdraw** takes one parameter 'amount' and will subtract 'amount' from the 'balance'. Prints the message: "Amount Withdrawn: $X.XX". If the user tries to withdraw an amount greater than current balance, prints "Insufficicent Funds" and charges and overdraft fee of $10.
- **get_balance** prints a user friendly message with the balance and returns the current balance.
- **add_interest** adds interest to the users balance. The annual interest rate is 1%.
- **print_recept** prints a receipt with the account name, number and balance in a specific order.

4. There are 3 examples of BankAccount() objects to demonstrate methods.
