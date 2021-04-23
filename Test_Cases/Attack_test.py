import unittest

from TheGame.Mage import Mage


class Attack_test(unittest.TestCase):
    def simple_attack_test(self):
        character = Mage()
        damage = character.simple__attack()
        self.assertTrue(19 < damage < 31)

    def hard__attack_test(self):
        character = Mage()
        damage = character.hard__attack()
        self.assertTrue(damage == 110.5)

    def alt_attack_test(self):
        character = Mage()
        damage = character.alt__attack()
        self.assertTrue(damage == 104)
