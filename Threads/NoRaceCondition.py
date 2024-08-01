from time import sleep
from threading import *

class Account:
    balance = 0

    def getBalance(self):
        sleep(2)
        return self.balance

    def setBalance(self, amount):
        sleep(2)
        self.balance = amount
    def deposit(self, amount):
        bal = self.getBalance()
        self.setBalance(amount + bal)

# Create a class by inheriting Thread class
class Racing(Thread):
    account: Account
    name = "no name"

    def __init__(self, account, name):
        super(Racing, self).__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.deposit(100)
            print(self.name, self.account.getBalance())

def main_task():
    acc = Account()
    # create thread instances
    t1 = Racing(acc, "Ram")
    t2= Racing(acc, "Shyam")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('Finish')

main_task()


