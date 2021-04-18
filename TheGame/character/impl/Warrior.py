from TheGame.character.AbstractCharacter import AbstractCharacter
from TheGame.attack.type.common.warrior.WarriorCommonAttack import WarriorCommonAttack


class Warrior(AbstractCharacter):
    name = "Воин"

    health = 1500
    mana = 200

    walk_range = 20

    common_attack = WarriorCommonAttack
    spells = []

    def use_common_attack(self):
        damage = Warrior.common_attack.damage
        return damage

    def cast_spell(self, spell_id):
        pass
