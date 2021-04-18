from Typing import typing
from Character import Character
import random

class Hunter(Character):
    name="Hunter"

    strength = 18
    dexterity = 17
    intelligence = 18

    mana = 75 + 75*(intelligence / 100)
    health= 200 + 200*(strength / 100)
    

    def __init__(self) -> None:
        pass

    def simple__attack(self):
        damage = random.randrange(24,36)
        typing("Охотник выпускает стрелу из лука и наносит: " + str(damage) + "урона")
        return damage
    
    def hard__attack(self):
        damage = 100 + 100*(self.dexterity / 100)
        self.mana = self.mana - 70
        typing("Охотник заряжает свой лук несколько секунд и делает одиночный выстрел. Наносит: " + str(damage) +" урона")
        return damage
    
    def alt__attack(self):
        damage = 30 + 30*(self.dexterity / 100)
        self.mana = self.mana - 20
        typing("Охотник направляет ветер в сторону врага, чтобы увеличить скорость атаки. Наносит: " + str(damage) +" урона")
        return damage
