
import unittest
import mock
import io
import sys
sys.path.append("TheGame")
from Battle import Battle
from Mage import Mage
from Hunter import Hunter

class End_game_test(unittest.TestCase):
    def test_EG1(self):
        battle = Battle(Mage(),Hunter())
        battle.player1.health = battle.deal_damage(battle.player1.health, 500)
        with mock.patch('builtins.input', return_value=1):
            assert battle.battle() == 'player2 win'
    
    def test_EG2(self):
        battle = Battle(Mage(),Hunter())
        battle.player2.health = battle.deal_damage(battle.player2.health, 500)
        with mock.patch('builtins.input', return_value=1):
            assert battle.battle() == 'player1 win'
    
    def test_EG3(self):
        battle = Battle(Mage(),Hunter())
        battle.player1.health = battle.deal_damage(battle.player1.health, 500)
        battle.player2.health = battle.deal_damage(battle.player2.health, 500)
        with mock.patch('builtins.input', return_value=1):
            assert battle.battle() == 'draw'

if __name__ == "__main__":
    unittest.main()