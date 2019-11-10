import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    test class that determines test case for user class behaviours.
    '''
    def setup(self):
        '''
        
        '''
        self.new_user = User("mickey","mikelkarije@gmail.com", "mickey22")
        
    
        self.assertEqual(self.new_user.user_name,)
        self.assertEqual(self.new_user.email,)
        self.assertEqual(self.new_user.password,) 
    def test_save_user(self):
        
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(self),1)
        
        
        if __name__ ==  '__main__':
            unittest.main()