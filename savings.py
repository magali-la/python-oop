# savings account sub-class of bank account. import first
from bank import BankAccount

# inherit the class as a parameter
class SavingsAccount(BankAccount):
    # initialize it - it's going to get all of the methods associated with BankAccount
    def __init__(self, account_number, owner, balance=0):
        super().__init__(account_number, owner, balance)