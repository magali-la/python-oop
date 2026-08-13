# testing functionality of bankaccount - import the class
from bank import BankAccount
from savings import SavingsAccount

# create instance of BankAccount and give it a value
bob_account = BankAccount(2468, "Bob", 100)

print(f"Bob's starting balance is: {bob_account.balance}")

# this will print the balance because theres a return statement within the withdraw method
print(f"Bob wants to withdraw $25. His balance will be {bob_account.withdraw(25)}")

# this will print it and convert the object into the string from our string method
print(f"Here is Bob's account info. {bob_account}")

print(f"Bob wants to deposit $50.")
# call this directly. there wasn't a return statement for the balance, so this will just print the string. If it was in the formatted string above, it would resolve to None.
bob_account.deposit(50)

print(f"Here is Bob's account info. {bob_account}")

# bob should be at 125 - try to withdraw 126 to get error message
print("Bob wants to withdraw 126, but he's at 125")

# use a try except block to catch the error without halting the program
try:
    # if successful it'll print, if not it'll throw the value error
    bob_account.withdraw(126)
except ValueError as error:
    print(error)


# test for the savings account - interest rate is defaulted in the subclass definition so no need to declare it, but do override the amount instead of $0
bob_savings = SavingsAccount(1357, "Bob", 100)
print(f"Bob's starting balance in his savings account is: {bob_savings.balance}")

# deposit - need to write the method separately since there is no return statement
print("Bob is depositing $100 into savings")
bob_savings.deposit(100)

# this will print the interest rate as well
print(bob_savings)

# withdraw
print("Bob wants to withdraw $50 from his savings")
bob_savings.withdraw(50)

print(bob_savings)

# add interest
print(f"Bob wants to see how much interest he has accumulated. The interest rate is {bob_savings.interest_rate * 100}%")

bob_savings.apply_interest()

print(bob_savings)