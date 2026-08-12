# this is the bank account base class
class BankAccount:
    # define variables and initial value for the balance - self represents the object itself for the class
    def __init__(self, account_number, owner, balance=0):
        # use self and dot notation to assign attributes to the values passed
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
