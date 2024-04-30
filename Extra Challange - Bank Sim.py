class BankAccount:
    def __init__(self, account_number, name, password):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('Deposit', amount))
        return f"Deposited {amount}. New balance is {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds or invalid amount."
        self.balance -= amount
        self.transactions.append(('Withdrawal', amount))
        return f"Withdrew {amount}. New balance is {self.balance}."

    def check_balance(self):
        return f"Your current balance is {self.balance}."

    def check_transactions(self):
        return self.transactions

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, password):
        if account_number in self.accounts:
            return "Account already exists."
        self.accounts[account_number] = BankAccount(account_number, name, password)
        return f"Account created successfully for {name}."

    def authenticate(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            return account
        else:
            return "Invalid credentials."

def main():
    bank = Bank()
    while True:
        print("\n1. Create Account")
        print("2. Authenticate")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Check Transactions")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            account_number = input("Enter account number: ")
            name = input("Enter name: ")
            password = input("Enter password: ")
            print(bank.create_account(account_number, name, password))
        elif choice == '2':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = bank.authenticate(account_number, password)
            if account == "Invalid credentials.":
                print(account)
            else:
                global current_account
                current_account = account
        elif choice == '3':
            amount = float(input("Enter the amount to deposit: "))
            print(current_account.deposit(amount))
        elif choice == '4':
            amount = float(input("Enter the amount to withdraw: "))
            print(current_account.withdraw(amount))
        elif choice == '5':
            print(current_account.check_balance())
        elif choice == '6':
            print(current_account.check_transactions())
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
