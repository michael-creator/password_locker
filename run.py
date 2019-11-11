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

    
    
  
