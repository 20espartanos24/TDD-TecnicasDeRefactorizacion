class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Retiro exitoso.")
        else:
            print("Saldo insuficiente.")

account = BankAccount(1000)
print("Saldo actual:", account.balance)
account.withdraw(500)
print("Saldo actual:", account.balance)

