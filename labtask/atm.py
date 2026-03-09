class Account:
    def __init__(self,account_number,name):
        self.account_number = account_number
        self.name = name
        self.total_amount = 0
    
    def deposit(self,amount):
        pin = int(input("Enter pin code \n"))
        if pin == 1530 :
            self.total_amount += amount
        else :
            print("Pin missmatched\n ")

            