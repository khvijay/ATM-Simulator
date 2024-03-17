class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  
            return f"Deposit successful. Your new balance is {self.balance}."
        else:
            return "Invalid amount. Please enter a positive number."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount  
            return f"Withdrawal successful. Your new balance is {self.balance}."
        else:
            return "Insufficient funds or invalid amount."

def main():
    atm = ATM()  # Initialize ATM with zero balance
    while True:
        print("1. Check Balance.")
        print("2. Deposit.")
        print("3. Withdraw.")
        print("4. Quit.")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Your balance is:", atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the Vijay khot ATM. Have a good day:!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
