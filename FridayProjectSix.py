# Define the BankAccount class
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Account number for the bank account
        self.balance = balance                # Current balance, initialized to zero by default

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance:.2f}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance:.2f}")

    # Method to check current balance
    def check_balance(self):
        return self.balance

# Create an instance of BankAccount
account = BankAccount(account_number="123456")

# Main program loop for user interaction
print("Welcome to the Bank Account Manager!")
while True:
    # Prompt user for account number
    user_account_number = input("Enter your account number to access your account: ")
    
    # Check if entered account number matches
    if user_account_number == account.account_number:
        # Display menu options
        print("\nWhat would you like to do?")
        print("1: Deposit Money")
        print("2: Withdraw Money")
        print("3: Check Balance")
        print("4: Exit")

        # Get user action
        action = input("Choose an option (1-4): ")
        
        if action == "1":
            # Deposit money
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        
        elif action == "2":
            # Withdraw money
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        
        elif action == "3":
            # Check balance
            balance = account.check_balance()
            print(f"Your current balance is: ${balance:.2f}")
        
        elif action == "4":
            # Exit program
            print("Thank you for using the Bank Account Manager!")
            break
        else:
            print("Invalid option. Please choose a valid action.")
    else:
        print("Account number not recognized. Please try again.")