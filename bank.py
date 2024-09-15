class BankAccount:
    def __init__(self):
        self.balance = 1000

    def deposite(self, amount):
        self.balance += amount
        print(f"You deposited {amount}. Your current balance is {self.balance}\n")

    def withddrow(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"You withdowed {amount}. Your current balance is {self.balance}\n")
        elif amount > self.balance:
            print("Insufficient balance.")
    
    def check_balance(self):
        print(f"Your current balance is {self.balance}\n")

    def run(self):
        while True:
            print("1. view balance")
            print("2. Deposite")
            print("3. Withdrow")
            print("4. Exit.")
            choice = input("Please enter your choice: ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposite: "))
                self.deposite(amount)
            elif choice == '3':
                amount = float(input("Enter amout to withdrow: "))
                self.withddrow(amount)
            elif choice ==  '4':
                print("exiting the system.")
                break
            else:
                print("Please enter proper choice.")

if (__name__) == "__main__":
    bank = BankAccount()
    bank.run()

