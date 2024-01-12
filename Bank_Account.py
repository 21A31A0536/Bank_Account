class BankAccount:
    def __init__(self,accountHolderName,accountNumber,balance):
        self.accountHolderName = accountHolderName
        self.accountNumber = accountNumber
        self.balance = balance
    def deposit( self , amount ):
        self.balance += amount
        print(" Deposited : " , amount)
    def withdraw( self , amount ):
        if amount <= self.balance:
            self.balance -= amount
            print(" Withdrawn : " , amount)
        else:
            print(" Insufficient Balance , Unable to Withdraw ")
    def displayBalance(self):
        print(" Current Balance : " , self.balance)
accountHolderName = str(input(" Name : "))
accountNumber = input(" Account Number : ")
while True:
    if not accountNumber.isdigit() or len(accountNumber) > 12 or len(accountNumber) < 11:
        print(" Invalid Account Number... Please Enter Valid  Account Number... ")
        accountNumber = input(" Valid Account Number : ")
    else:
        break
balance = float(input(" Enter Balance : "))
account = BankAccount(accountHolderName,accountNumber,balance)
while (True):
    print(" Operations : " + " \n " + " 1. Deposit " + " \n " + " 2. Withdraw " + " \n " + " 3. Display Balance " + " \n " + " 4. Exit ")
    choice = int(input(" Enter Operation : "))
    if choice == 1:
        amount = float(input(" Enter Amount to Deposit : "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input(" Enter Amount to Withdraw : "))
        account.withdraw(amount)
    elif choice == 3:
        account.displayBalance()
    elif choice == 4:
        print(" Thank You for Your Transaction... Process Completed.... ")
        break
    else:
        print(" Invalid Operation... Please Try Again... ")
