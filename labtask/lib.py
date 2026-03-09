class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposit ho gaya!")
        else:
            print("Amount 0 se zyada hona chahiye!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Itna balance nahi hai!")
        elif amount <= 0:
            print("Amount 0 se zyada hona chahiye!")
        else:
            self.balance -= amount
            print(f"{amount} withdraw ho gaya!")

    def show_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")


# Test karo
b1 = Bank("Mubashir", 1000)
b1.show_balance()
b1.deposit(500)
b1.withdraw(200)
b1.show_balance()