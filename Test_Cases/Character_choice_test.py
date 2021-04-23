import unittest
import mock
import io
import sys
sys.path.append('TheGame')
from Choice import Choice

class Character_choice_test(unittest.TestCase):
            
    def test_C0_mage(self):
        char = Choice()
        with mock.patch('builtins.input', return_value=1):
            assert char.choice__character().name == "Mage"
    
    def test_C0_war(self):
        char = Choice()
        with mock.patch('builtins.input', return_value=2):
            assert char.choice__character().name == "Warrior"

    def test_C0_hunt(self):
        char = Choice()
        with mock.patch('builtins.input', return_value=3):
            assert char.choice__character().name == "Hunter"
   
    def test_C1(self):
        pass


if __name__ == '__main__':
    unittest.main()