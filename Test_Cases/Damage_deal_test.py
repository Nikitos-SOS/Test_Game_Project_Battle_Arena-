import sys

import unittest
import mock
import io
sys.path.append('TheGame')
from Battle import Battle
from Mage import Mage
from Warrior import Warrior
from Hunter import Hunter


class Damage_deal_test(unittest.TestCase):

    def test_damage_deal(self):
        battle = Battle(Mage(),Hunter())
        with mock.patch('builtins.input', return_value=2):
            damage = battle.make_a_turn(battle.player2)
            assert battle.deal_damage(battle.player1.health,damage)>0

    def test_warrior_simple_attack(self):
        battle = Battle(Warrior(),Hunter())
        with mock.patch('builtins.input', return_value=1):
            damage = battle.make_a_turn(battle.player1)
            assert damage >= 27 and damage <= 31
           
 

if __name__ == '__main__':
    unittest.main()