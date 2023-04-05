class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

# deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here

# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if amount < self.balance:
            amount -= self.balance
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
        # your code here

# display_account(self) - print to the console: eg. "Balance: $100"
    def display_account(self):
        print(f"Your current balance is {self.balance}")
        print(f"Your interest rate is {self.int_rate}")
        return self
        # your code here

# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        self.balance *= self.int_rate
        return self
        # your code here

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account()
        return cls
        # your code here

account1 = BankAccount()
account1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account()
account2 = BankAccount()
account2.deposit(500).deposit(1000).withdraw(200).withdraw(150).withdraw(50).withdraw(100).yield_interest().display_account()

BankAccount.print_accounts()



