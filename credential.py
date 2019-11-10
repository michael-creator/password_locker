import random
import string 
import pyperclip

class Credential:
     credential_list =  []
     def __init__(self, app_title, password):
         self.app_title = app_title
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