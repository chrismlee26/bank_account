## Welcome

![GitHub top language](https://img.shields.io/github/languages/top/chrismlee26/bank_account?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/chrismlee26/bank_account?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/chrismlee26/bank_account?style=for-the-badge)

This project is my bank account program in Python3. The Project encompasses OOP Methods & Attributes as Assignment #1 for CS1.1 (OOP).

## Run

$ "python3 BankAccount.py" to run.
$ Or just press the run button in VScode

## Operation

1. The **BankAccount** class creates an instance of BankAccount when called.
2. The **BankAccount** class takes the @params "Full Name" (string), Balance (int). Balance is defaulted to 0.
3. The class has the following attributes:

- **full_name** : Full name of Owner
- **account_number** : Randomly generated 8 digit umber. Unique Per Account
- **routing_number** : 9 Digit Number, same for all accounts.
- **balance** : The balance of the account, should start at 0

4. Methods for the BankAccount class:

- **deposit** takes one parameter 'amount' and will add 'amount' to the 'balance'. Prints the message: "Amount Deposited: $X.XX"
- **withdraw** takes one parameter 'amount' and will subtract 'amount' from the 'balance'. Prints the message: "Amount Withdrawn: $X.XX". If the user tries to withdraw an amount greater than current balance, prints "Insufficicent Funds" and charges and overdraft fee of $10.
- **get_balance** prints a user friendly message with the balance and returns the current balance.
- **add_interest** adds interest to the users balance. The annual interest rate is 1%.
- **print_recept** prints a receipt with the account name, number and balance in a specific order.

5. There are 3 examples of BankAccount() objects to demonstrate methods. These are found on lines 45-58.
