# savings account sub-class of bank account. import first
from bank import BankAccount

# inherit the class as a parameter
class SavingsAccount(BankAccount):
    # initialize it - add the interest rate parameter specific to this subclass at 5%
    def __init__(self, account_number, owner, balance=0, interest_rate=.05):
        # this gets the parent's methods
        super().__init__(account_number, owner, balance)

        # initialize interest_rate attribute
        self.interest_rate = interest_rate

    # method to add interest - nothing else is used as an argument so you only need self
    def apply_interest(self):
        account_interest = self.balance * self.interest_rate

        # add to the balance
        self.balance += account_interest

    # string override - make a new addition to the original string with info on the savings account
    def __str__(self):
        return f"{super().__str__()} \n Interest rate: {self.interest_rate * 100}%"