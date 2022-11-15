# Create a Budget class that can instantiate objects based on different budget categories like 
# food, clothing, and entertainment. These objects should allow for depositing and withdrawing 
# funds from each category, as well computing category balances and transferring balance amounts 
# between categories. 
class Budget:
    def __init__(self, category, balance):
        self.category = category
        self.balance = balance
    def display_info(self):
        for info in vars(self).values():
            print(info)
        return self
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds.")
        return self
    def transfer(self, amount, other_category):
        self.withdraw(amount)
        other_category.deposit(amount)
        return self

food = Budget("food", 300)
clothing = Budget("clothing", 100)
entertainment = Budget("entertainment", 50)
food.display_info().transfer(20, entertainment).display_info()
entertainment.display_info()

