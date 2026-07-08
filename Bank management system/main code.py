import json
class Bank:
    def __init__(self):
        self.name='' 
        self.__pin=''
        self.__balance=0
        self.logged_in_account=None
        self.accounts={}
        self.load_accounts()

    def create_account(self):

        name = input("Enter your name: ")

        if name in self.accounts:
            print("Account already exists.")
            return

        pin = int(input("Enter your 4-digit PIN: "))
        balance = int(input("Enter your initial balance: "))

        self.accounts[name] = {
        "pin": pin,
        "balance": balance,
        "history": [f"Account created with initial balance: {balance}"]}
        print("Account created successfully.")
        self.save_accounts()
    
    def login(self):

        name=input("Enter your name:")
        pin=int(input("Enter your pin:"))
        for account_name in self.accounts:
            if name==account_name and self.accounts[account_name]["pin"]==pin:
                print("login succcessfull")
                self.logged_in_account=account_name
                return True
        else:
            print('Please check your name or pin and try again.')
            return False
    
    def deposit(self):
        amount=int(input("Enter your amount to deposit:"))
        if amount > 0:
            self.accounts[self.logged_in_account]["balance"] += amount
            print('Deposit succcessful')
            print('Current balance:',self.accounts[self.logged_in_account]["balance"])
            self.accounts[self.logged_in_account]["history"].append(f"Deposited ₹{amount}")
        else:
            print("Invalid amount. Please enter a positive value.")
        self.save_accounts()
    
    def withdraw(self):
        amount=int(input("Enter your amount to withdraw:"))
        if amount <0:
            print("Invalid amount. Please enter a positive value.")
        elif amount>self.accounts[self.logged_in_account]["balance"]:
            print("Insufficient balance.")
        elif amount <= self.accounts[self.logged_in_account]["balance"]:
            self.accounts[self.logged_in_account]["balance"] -= amount
            self.accounts[self.logged_in_account]["history"].append(f"Withdrawn ₹{amount}")
            print("Withdrawal successful.")
            return 'Remaining balance:', self.accounts[self.logged_in_account]["balance"]
        else:
            print("Invalid amount or insufficient balance.")
        self.save_accounts()

    def check_balance(self):
        return 'Current balance:',self.accounts[self.logged_in_account]["balance"]

    def menu(self):
        while True:
            user_input=int(input("""*** HI WELCOME TO BANK MANAGEMENT SYSTEM ***
                1.create account
                2.login
                3.exit 
                Enter your choice: """))          
            if user_input==1:
                self.create_account()
            elif user_input==2:
                if len(self.accounts)==0:
                    print("Please create an account first.")
                else:
                    if self.login():
                        self.account_menu()
            elif user_input==3:
                print("Thank you for using our services.")
                break
            else:
                print("Invalid input. Please try again.")
    def account_menu(self):
        while True:
            user_input=int(input("""
                1.Deposit
                2.Withdraw
                3.Check balance
                4.Transaction history
                5.Change pin
                6.Exit
                Enter your choice: """))
            if user_input==1:
                self.deposit()
            elif user_input==2:
                self.withdraw()
            elif user_input==3:
                print('Current balance:',self.accounts[self.logged_in_account]["balance"])
            elif user_input==4:
                self.transaction_history()
            elif user_input==5:
                self.change_pin()
            elif user_input==6:
                self.logged_in_account = None
                print(" Exiting... Thank you for using our services.")
                break
            else:
                print("Invalid input. Please try again.")
    
    def transaction_history(self):
        if self.logged_in_account:
            history = self.accounts[self.logged_in_account]["history"]
            if history:
                print("Transaction History:")
                for transaction in history:
                    print(transaction)
            else:
                print("No transaction history available.")
        else:
            print("Please log in to view transaction history.")
    
    def change_pin(self):
        if self.logged_in_account:

            current_pin = int(input("Enter your current PIN: "))

            if current_pin == self.accounts[self.logged_in_account]["pin"]:

                new_pin = int(input("Enter your new PIN: "))

                if len(str(new_pin)) != 4:
                    print("PIN must be exactly 4 digits.")
                    return

                self.accounts[self.logged_in_account]["pin"] = new_pin

                self.accounts[self.logged_in_account]["history"].append(
                    "PIN changed successfully")

                self.save_accounts()

                print("PIN changed successfully.")

            else:
                print("Incorrect current PIN.")

    def load_accounts(self):
        try:
            with open("accounts.json",'r') as file:
                self.accounts=json.load(file)
        except FileNotFoundError:
            self.accounts={}
    
    def save_accounts(self):
        with open("accounts.json",'w') as file:
            json.dump(self.accounts,file)
    
                  

b=Bank()
b.menu()
              
