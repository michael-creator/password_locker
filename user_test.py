import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    test class that determines test case for user class behaviours.
    '''
    def setup(self):
        '''
        
        '''
        self.new_user = User("facebook""mickey","mikelkarije@gmail.com", "mickey22")
        
        self.assertEqual(self.new_user.account,)
        self.assertEqual(self.new_user.user_name,)
        self.assertEqual(self.new_user.email,)
        self.assertEqual(self.new_user.password,) 
        
        
        
        if __name__ ==  '__main__':
            unittest.main()