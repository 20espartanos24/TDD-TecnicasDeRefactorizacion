class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Encapsulamos el saldo

    def get_balance(self):
        return self._balance  # Getter para acceder al saldo

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Retiro exitoso.")
        else:
            print("Saldo insuficiente.")

account = BankAccount(1000)
print("Saldo actual:", account.get_balance())  # Utilizando el getter
account.withdraw(500)
print("Saldo actual:", account.get_balance())  # Utilizando el getter

