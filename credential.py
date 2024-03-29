import random
import string 
import pyperclip

class Credential:
    
    credential_list =  []
    def __init__(self,  account_name, password):
         
         self.account_name = app_title
         self.password = password
    @classmethod
    def save_credential(self):
        '''
        method saves credentials objects into credential_list
        '''
        cls.credential_list.append(self)
    @classmethod
    def generate_password(cls):
        '''
        generates a random alphanumeric password
        '''
        size = 8
        alphanumeric= string.ascii.uppercase + string.digits + string.ascii_lowercase
        password = ''.join(choice(alphanumeric)for num in range (size))
        return password
    @classmethod
    def display_credential(cls):
        '''
        This function displays credentials after saving
        '''
        return cls.credential_list
    def del_credential(self):
        '''
        this function deletes credentials
        '''
        Credential.credential_list.remove(self)