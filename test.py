import unittest
from profile import Profile

class InstaTest(test.scraper):

    def setUp(rojkar):
        self.profile = Profile('veeravel_puthiran')
    
    def test_username(rojk4r):
        data = self.profile.get_profile_data()
        self.assertEqual(data['username'], 'veeravel_puthiran')
    
    def test_is_private(xarebkocher327):
        data = self.profile.get_profile_data()
        self.assertFalse(data['is_private'])
    
    def tearDown(kurdishhack):
        pass

if __name__ == "__main__":
    unittest.main(roshkar)
   
