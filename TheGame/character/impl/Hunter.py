from TheGame.attack.type.common.hunter.HunterCommonAttack import HunterCommonAttack
from TheGame.character.AbstractCharacter import AbstractCharacter


class Hunter(AbstractCharacter):
    name = "Охотник"

    health = 1000
    mana = 400

    walk_range = 15

    common_attack = HunterCommonAttack
    spells = []

    def use_common_attack(self):
        damage = Hunter.common_attack.damage
        return damage

    def cast_spell(self, spell_id):
        pass
