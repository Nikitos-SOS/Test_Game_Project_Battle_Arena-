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

    def test_DD1(self):
        battle = Battle(Mage(),Hunter())
        health = battle.player2.health
        with mock.patch('builtins.input', return_value=2):
            damage = battle.make_a_turn(battle.player1)
            assert health > battle.deal_damage(battle.player2.health,damage)>0

    def test_DD2(self):
        battle = Battle(Warrior(),Hunter())
        health = battle.player1.health
        with mock.patch('builtins.input', return_value=1):
            damage = battle.make_a_turn(battle.player2)
            assert health > battle.deal_damage(battle.player1.health,damage)>0
           
    def test_DD3(self):
        battle = Battle(Warrior(),Hunter())
        health = battle.player1.health
        with mock.patch('builtins.input', return_value='yrt'):
            damage = battle.make_a_turn(battle.player2)
            assert health == battle.deal_damage(battle.player1.health,damage)
 

if __name__ == '__main__':
    unittest.main()