class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


account1 = SavingsAccount("sara", 1000, 1.5)
account2 = SavingsAccount("Meha", 400, 10)

print(account1.owner, account1.balance, account1.interest_rate)
print(account2.owner, account2.balance, account2.interest_rate)

# Here Account and Savings Account has shared properties and establish "IS-A" relationship
