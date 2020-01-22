# from .account import Account

class User():
    def __init__(self, name, email, age, password):
        super()
        self.name = name
        self.age = age,
        self.email = email
        self.password = password
    
    def user_details(self):
        user = {
            'name': self.name, 
            'email': self.email,
            'password': self.password,
            'age': self.age,
        }
        
        return self