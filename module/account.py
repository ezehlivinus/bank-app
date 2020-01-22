import uuid
from .user import User


class Account(User):
    def __init__(self, name, email, age, password):
        super().__init__(name, email, age, password)
        self.total = 0.0
        
    def create_account(self):
        num = uuid.uuid4()
        account = num.fields[5]
        self.account = account
        self.user = self
        return self
    
    def account_detail(self):
        return self
    
    def check_balance(self, account):
            
        return self.total

    def check_account_details(self):
        return self.account
    
    def withdraw(self, amount):
        balance = self.check_balance
        if balance < amount:
            return 'Insuficient balance'
        new_balance = balance - amount
        self.total = new_balance
        return f'Take your cash: {amount}'

    def deposit(self, amount, account):
        self.total += amount
        return f'New balance is {self.check_balance(account)}'
    
    def transfer(self, account, amount):
        balance = self.check_balance
        if balance < amount:
            return 'Insuficient balance'
        # check if the account number does exits

    def process_transfer(self, account, amount):
        pass
        # determine if the user exit if it does
        # add the amount to the user existing account