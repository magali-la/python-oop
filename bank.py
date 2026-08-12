# this is the bank account base class
class BankAccount:
    # define variables and initial value for the balance - self represents the object itself for the class
    def __init__(self, account_number, owner, balance=0):
        # use self and dot notation to assign attributes to the values passed
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    # create methods for deposit
    def deposit(self, amount):
        # set condition that the amount has to be 1 or more to be deposited
        if amount > 0:
            self.balance += amount
            print(f"You have deposited {amount} into your account. Balance is {self.balance}")
        # raise an error that it can't be processed 
        else:
            raise ValueError("Unable to process deposit for amounts less than $0.01")

    # create method for withdraw
    def withdraw(self, amount):
        # condition needs to be less than or equal to the balance to pass
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn {amount} from your account. Balance is {self.balance}")

            # return the balance
            return self.balance
        # error - insufficient funds error
        else:
            raise ValueError("Unable to process withdrawal. Insufficient funds")

    # create method to print the object with the account info and balance formatted
    def __str__(self):
        # this method needs to return a string
        return f"Account {self.account_number} \n Owner: {self.owner} \n Balance: ${self.balance}"
