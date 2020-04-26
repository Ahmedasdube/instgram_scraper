import unittest
from profile import Profile

class InstaTest(unittest.TestCase):

    def setUp(self):
        self.profile = Profile('veeravel_puthiran')
    
    def test_username(self):
        data = self.profile.get_profile_data()
        self.assertEqual(data['username'], 'veeravel_puthiran')
    
    def test_is_private(self):
        data = self.profile.get_profile_data()
        self.assertFalse(data['is_private'])
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()   