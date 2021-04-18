import unittest
import mock
import io
import sys
sys.path.append('TheGame')
from Choice import Choice

class Cherecter_choice_test(unittest.TestCase):
            
    def test_mage(self):
        char = Choice()
        with mock.patch('builtins.input', return_value=1):
            assert char.choice__character().name == "Mage"
    
    def test_war(self):
        char = Choice()
        with mock.patch('builtins.input', return_value=2):
            assert char.choice__character().name == "Warrior"

    def test_hunt(self):
        char = Choice()
        with mock.patch('builtins.input', return_value=3):
            assert char.choice__character().name == "Hunter"
   
    def test_warr_strength(self):
        char = Choice()
        with mock.patch('builtins.input', return_value=2):
            assert char.choice__character().health > 100

if __name__ == '__main__':
    unittest.main()