from module.user import User
from module.account import Account
import sys, csv, os
import uuid

# Create your views here.
def perform_another_transaction():
    perform = input('Perform another transaction? y/n ')
    if(perform == 'y'):
        prompt()
    else:
        sys.exit(0)
        
def prompt():
    print('Press 1: Create Account\nPress 2: Transaction')
    choice = int(input('Enter a number: '))
    if(choice == 1):
        return new_account_details()
    elif choice == 2:
        return transactions()
    
    perform_another_transaction()

def transactions():
    print('Press 1: Check balance\n')
    choice = int(input('Enter a number: '))
    if choice == 1:
        # check_balance('ezeh@gmail.com', 1234)
        pass

def new_account_details():
    print('Enter your details separated with space: name email age password\ne.g: Ade ade@gmail.com 20 1234')
    detail = input('Your details: ')
    try:
        user_detail = detail.split(' ')
        if not len(user_detail) == 4:
            print('The details you entered is less or more ')
            prompt()
        int(user_detail[2]) # Trying to see if we actually recieved integer
        return create_account(user_detail)
    except:
        raise
    

def create_account(detail):
    # detail = new_account_details()
    # user = User(detail[0], detail[1], int(detail[2]), detail[3]).create_account()
    
    try:
        user = Account(detail[0], detail[1], int(detail[2]), detail[3]).create_account()
        
        with open('bank-db.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # user = user.user_details()
            user = {
                'name': user.name,
                'email': user.email,
                'age': user.age[0], # This is return as tuple: (age, ) ; i dont know why
                'password': user.password,
                'account': user.account,
                'total': user.total,
            }
            
            writer.writerow([user])
        file.close()
        perform_another_transaction()
    
    except:
        raise


# def check_balance(email, password):
#     user = User.objects.filter(email = email)
#     account = Account.objects.all()
#     print(f'{user} your balance is: {account}')
prompt()