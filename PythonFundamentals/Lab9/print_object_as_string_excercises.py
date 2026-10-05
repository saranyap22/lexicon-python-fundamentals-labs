# Excercises to print object as str using __str__ method

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product1 = Product("Laptop", 7654.98)
print(product1)
print(str(product1))
# when we dont have __str__ method the class name and object reference is printed.
# Result is same even when using str() to cast


# -----------------------------------
# with __str__ method

class Productt:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name: {self.name} Price: {self.price}"


product2 = Productt("Grinder", 9000.45)
print(product2)
print(str(product2))

# Here __str__ method provide the infomation to be retrieved
# and printed while try to print or accessing with str() casting


# ------------------------------------------------------

# __str__ with inheritance

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return (
            f"Name: {self.owner}"
            f"Balance: - {self.balance}"
        )


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)

        self.interest_rate = interest_rate

    def __str__(self):
        return (
            f"Name: {self.owner} "
            f"Balance: {self.balance} "
            f"Interest rate: {self.interest_rate}"
        )


account = Account("Sara", 7888)
savings_account = SavingsAccount("Grace", 9000, 6.0)
print(account)
print(savings_account)
