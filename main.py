# testing functionality of bankaccount - import the class
from bank import BankAccount

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