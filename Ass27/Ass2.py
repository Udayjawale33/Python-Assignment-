class BankAccount:
    100
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Current Balance     :", self.Amount)

    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.Amount += amt
        print("Amount Deposited Successfully.")

    def Withdraw(self):

        amt = float(input("Enter amount to withdraw: "))

        if amt <= self.Amount:

            self.Amount -= amt
            print("Amount Withdrawn Successfully.")

        else:
            print("Insufficient Balance!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest
    
def main():
    
    obj1 = BankAccount("Uday",5000)
    obj2 = BankAccount("Swami",10000)

    print("----- Account 1 -----")
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.Display()
    print("Interest =",obj1.CalculateInterest())

    print("\n----- Account 2 -----")
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.Display()
    print("Interest =",obj2.CalculateInterest())

if __name__ == "__main__":
    main()