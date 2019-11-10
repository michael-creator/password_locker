import pyperclip

class User:

    '''
    this class generates instance of new users
    '''
    user_list = []
    def __init__(self, account ,username , email, password):

        self.username = username,
        self.email = email,
        self.password = password,
    def save_user(self):
        '''
        function that adds user credentials to the user_list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        this method deletes users 
        '''
        User.user_list.remove(self)
    @classmethod
    def find_by_name(cls,username):
        '''
        method that checks the username of the user and matches it to the one given.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def display_user(cls):
        '''
        returns user list with user account details
        '''
        return cls.user_list
