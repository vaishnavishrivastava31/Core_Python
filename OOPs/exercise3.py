class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def account_number(self):
        return self.account_number
    def balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit {amount}. New balance is {self.balance}")
        else:
            print("deposit cannot be negative")
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdraw {amount}. New balance is {self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Withdraw cannot be negative")
account = BankAccount("123456789", 1000)
print(f"Account Number: {account.account_number}")
print(f"Balance: {account.balance}")
account.deposit(500)
account.withdraw(300)
print(f"Final Balance: ${account.balance}")