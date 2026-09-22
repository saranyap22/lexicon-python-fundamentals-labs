class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        if self.pages > 300:
            return True
        return False


book1 = Book("Clean Code", "Robert C. Martin", 464)
book2 = Book("The Pragmatic Programmer", "David Thomas", 352)
book3 = Book("Fluent Python", "Luciano Ramalho", 792)
book4 = Book("  Design PAtterns", "Erich Gamma", 464)
print(book4.title)
book4.title = "Design Patterns"
print(book4.title)

print("Is Long:", book4.is_long())
# -------------------------------------------


class Laptop:
    def __init__(self, brand, model, price,  ram_gb=4):
        self.brand = brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price


laptop1 = Laptop("Dell", "XPS 13", 1199.89, 16)
laptop2 = Laptop("Dell", "XPS 13", 1199.89, 16)

# Though the Same arguments passed to attricutes they are having different reference.
# Both are not equal
print(laptop1 is laptop2)


# Default value 4 will be assigned to ram_gb arguments
laptop3 = Laptop("Hp", "Spectre x360", 1349.89)
print(laptop3.ram_gb)

# Create object using keyword arguments
laptop4 = Laptop(brand="Lenovo", model="Thinkpad X1", price=1899.00, ram_gb=32)
print(laptop4.brand, laptop4.model, laptop4.ram_gb, laptop4.price)


# -------------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        if self.validateAmount(balance):
            self.balance = balance

    def deposit(self, amount):
        self.validateAmount(amount)
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Amount is greater than Balance")

        self.validateAmount(amount)
        self.balance -= amount

    def validateAmount(self, amount):
        if not amount >= 0:
            raise ValueError("Amount should be greater than or equal to 0")


# Positive cases
account1 = BankAccount("sara", 1000)
print("Account details:", account1.owner, account1.balance)
account1.deposit(100)
print("Account details after deposit:", account1.owner, account1.balance)
account1.withdraw(50)
print("Account details after withdraw:", account1.owner, account1.balance)

# ValueError

account2 = BankAccount("Meena", 900)
account2.withdraw(3000)
account2.deposit(-1)


# ---------------------------------------

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False
