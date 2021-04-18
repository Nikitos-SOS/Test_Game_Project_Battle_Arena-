
import unittest
import mock
import io
import sys
sys.path.append('TheGame')
from Battle import Battle
from Mage import Mage
from Hunter import Hunter


class Turn_test(unittest.TestCase):
    
    def test_mage_turn(self):
        battle = Battle(Mage(),Hunter())
        with mock.patch('builtins.input', return_value=1):
            assert battle.make_a_turn(battle.player1) < 35    

    def test_hunter_turn(self):
        battle = Battle(Mage(),Hunter())
        with mock.patch('builtins.input', return_value=1):
            assert battle.make_a_turn(battle.player2) > 20 

    
    
if __name__ == '__main__':
    unittest.main()