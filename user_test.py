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
        
    def test_init(self):
        '''
        test init tests if object in the user list are initialized correctly.
        '''
        self.assertEqual(self.new_user.user_name,)
        self.assertEqual(self.new_user.email,)
        self.assertEqual(self.new_user.password,) 
    def test_save_user(self):
        
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(self),1)
    def test_save_multiple_user(self):
        '''
        this function will add multiple user inputs
        '''
        self.new_user.save_user()
        test_user = User("Test","mickeey","mikelkarije@.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
    def test_display_all_user(self):
        '''
        test_display_all_user returns a list of all users in the list
        '''
        self.assertEqual(User.display_user(),User.user_list)
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list

        '''
        self.new_user.save_user()
        test_user = User("Test","mickey") 
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
    

    
    if __name__ ==  '__main__':
            unittest.main()