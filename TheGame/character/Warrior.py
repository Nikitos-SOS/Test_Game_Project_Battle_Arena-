from Typing import typing
from Character import Character
import random

class Warrior(Character):
    name="Warrior"
    strength= 25
    dexterity= 20
    intelligence= 18

    mana = 75 + 75*(intelligence / 100)
    health= 200 + 200*(strength / 100)
    

    def __init__(self) -> None:
        pass

    def simple__attack(self):
        damage = random.randrange(27,31)
        typing("Воин наносит сокрушительный удар топором и наносит: " + str(damage) + "урона")
        return damage
    
    def hard__attack(self):
        damage = 50 + 50*(self.dexterity / 100)
        self.mana = self.mana - 30
        typing("Приводит врага в бешенство, замедляя его и нанося ему урон. Наносит: " + str(damage) +" урона")
        return damage
    
    def alt__attack(self):
        damage = 80 + 80*(self.dexterity / 100)
        self.mana = self.mana - 50
        typing("Герой отвечает на удары противников, нанося чистый урон всем врагам вокруг себя. Наносит: " + str(damage) +" урона")
        return damage
