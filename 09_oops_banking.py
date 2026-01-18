class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def check_balance(self):
        print(f"Your balance is {self.balance}")

    def withdraw(self, amount):
        if amount >= self.balance:
            print("Insufficent amount")
        else:
            self.balance -= amount
        

# Account with 1000 balance
acc = BankAccount(1000)
acc.check_balance()
acc.withdraw(500)
acc.check_balance()
acc.deposit(190877)

acc.check_balance()
