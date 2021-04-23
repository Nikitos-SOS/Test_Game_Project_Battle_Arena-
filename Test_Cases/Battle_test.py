import unittest
from unittest import mock

from TheGame.Battle import Battle
from TheGame.Hunter import Hunter
from TheGame.Mage import Mage
from TheGame.Warrior import Warrior


class Battle_test(unittest.TestCase):
    def deal_damage_test(self):
        newHealth = Battle.deal_damage(self, 100, 10)
        self.assertTrue(newHealth == 90)

    def deal_damage_test_in_battle(self):
        battle = Battle(Mage(), Hunter())
        with mock.patch('builtins.input', return_value=2):
            damage = battle.make_a_turn(battle.player2)
            assert battle.deal_damage(battle.player1.health, damage) > 0

    def test_warrior_simple_attack(self):
        battle = Battle(Warrior(), Hunter())
        with mock.patch('builtins.input', return_value=1):
            damage = battle.make_a_turn(battle.player1)
            assert damage >= 27 and damage <= 31

    def test_win_player1(self):
        battle = Battle(Mage(), Hunter())
        battle.player1.health = battle.deal_damage(battle.player1.health, 500)
        with mock.patch('builtins.input', return_value=1):
            assert battle.battle() == 'player2 win'

    def test_win_player2(self):
        battle = Battle(Mage(), Hunter())
        battle.player2.health = battle.deal_damage(battle.player2.health, 500)
        with mock.patch('builtins.input', return_value=1):
            assert battle.battle() == 'player1 win'

    def test_draw(self):
        battle = Battle(Mage(), Hunter())
        battle.player1.health = battle.deal_damage(battle.player1.health, 500)
        battle.player2.health = battle.deal_damage(battle.player2.health, 500)
        with mock.patch('builtins.input', return_value=1):
            assert battle.battle() == 'draw'
