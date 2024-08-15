# Example 4: BankAccount Class
# A class representing a bank account with attributes for the account number, account holder, and balance, and methods to deposit, withdraw, and get account details.

class bankAccount:
    def __init__(self, account_number, account_holder, balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. new balance is {self.balance}.")

    
    def withdraw(self, amount):
        if amount  <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. new balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def get_account_details(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, balance: {self.balance}"
    


#usage
account1 = bankAccount("101", "Devarshi Tambulkar", 10000)
print(account1.get_account_details())
account1.deposit(500)
account1.withdraw(2000)