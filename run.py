import pyperclip
from credential import Credential
from user import User


def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name ,password  )


def save_users():
    '''
    Function to save user
    '''
    user.Credential.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def display_user():
    '''
    function that displays users
    ''' 
    user.display_user()
def display_credential():
    '''
    function that displays users credentials
    ''' 
    return Credential.display_credential()
def main():
    print("Hello welcome to password locker")
    print("lets begin to create an account")
    print("_"*25)
    print("i. create Account")
    print("Enter username")
    user = input()  
    print("Enter password")
    password = input()
    # save_users(create_user(user , email ,password))
    print(f"Welcome {user} you have created an account with us, please enjoy")
    print("press (a)login into an account, or (b) exit the program")


    
    
  
