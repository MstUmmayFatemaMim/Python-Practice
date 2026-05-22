########    3. Bank account /// Create a BankAccount class with balance. Add deposit(amount)
# and withdraw(amount) methods. Prevent balance from going negative.

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        print(f"Bank account balance is {balance}")
    def deposit(self,amount):
        self.balance += amount
        print(f"You have deposited {amount}and your balance is {self.balance}")
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:         #######     Prevent negative balance
            print("You don't have enough money!")
        elif amount<self.balance:
            self.balance -= amount
            print("After withdraw balance is:",self.balance)
        else:
            self.balance = amount
            print("Your balance is:0")
        return self.balance
x=BankAccount(1000)
# print(f"Bank account balance is {x.balance}")
# print(f"Bank account deposit balance is {x.deposit(100)}")
# print(f"After withdraw balance is {x.withdraw(2000)}")
x.deposit(20000)        ######### Add money
x.withdraw(10000)       ######### Withdraw money
