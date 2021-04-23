import unittest
import mock
import io
import sys
sys.path.append('TheGame')
from Mage import Mage
from Warrior import Warrior
from Hunter import Hunter

class Characters_test(unittest.TestCase):
    # Mage tests
    def test_CM1(self):
        mage = Mage()
        self.assertTrue(19 <= mage.simple__attack() <= 31)   
    
    def test_CM2(self):
        mage = Mage()
        self.assertTrue(mage.hard__attack()>=85)   
    
    def test_CM3(self):
        mage = Mage()
        self.assertTrue(mage.alt__attack()>=80)  

    # Warrior tests
    def test_CW1(self):
        warrior = Warrior()
        self.assertTrue(27 <= warrior.simple__attack() <= 31)

    def test_CW2(self):
        warrior = Warrior()
        self.assertTrue(warrior.hard__attack()>=50)

    def test_CW3(self):
        warrior = Warrior()
        self.assertTrue(warrior.alt__attack()>=80)
    
    # Hunter tests
    def test_CH1(self):
        hunter = Hunter()
        self.assertTrue(24 <= hunter.simple__attack() <= 36)

    def test_CH2(self):
        hunter = Hunter()
        self.assertTrue(hunter.hard__attack()>=100)

    def test_CH3(self):
        hunter = Hunter()
        self.assertTrue(hunter.alt__attack()>=30)

if __name__ == '__main__':
    unittest.main()