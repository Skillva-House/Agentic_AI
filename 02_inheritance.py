class Account:
    def __init__(self, owner, balance=0):
       self.owner = owner
       self._balance = balance
     
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        
    @property
    def balance(self):
        return self._balance
    
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, rate=0.05):
        super().__init__(owner, balance)
        self.rate = rate
        
    def add_interest(self):
        self.deposit(self._balance * self.rate)
        
acc = SavingsAccount("Suleman", 1000)
acc.add_interest()
print(acc.balance)