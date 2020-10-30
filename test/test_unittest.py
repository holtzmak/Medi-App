import unittest
from input import function

class TestUserInput(unittest.TestCase):
    def test_user_input_rejected_containing_mistake(self):
        strin=('feaver cough')
        i = function(strin)
        self.assertEqual(None, i)
    
    def test_user_input_accepted(self):
        strin=('fever cough')
        i = function(strin)
        self.assertEqual(['fever', 'cough'], i)

if __name__ == '__main__':
    unittest.main()
