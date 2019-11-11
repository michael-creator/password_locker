import unittest
import string
import pyperclip
from user import User
from random import choice
from credential import Credential


class TestUser():
    def setUp(self):
        self.new_credential = User("facebook","mickey")

    def Test__init__(self, account, account_name,account_password ):

        self.account = account
        self.account_name = account_name
        self.account_email = account_email
        self.account_password = account_password

    def save_credential(self, account_name, password):
        '''
        save_credential method saves credentials if __name__ == '__main__':
    unittest.main()
objects into credential_list
        '''
        Credential.credential_list.append(self)
    def generate_password(cls):      
        '''
        Method that generates a random alphanumeric password
        '''

        size = 8

        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        password = ''.join(choice(alphanum) for num in range(size))

        return password
    def display_credentials(cls):
        '''
        This function displays credentials after saving
        '''
        for credential in cls.credential_list:
             return credential
  
if __name__ == '__main__':
    unittest.main()
    