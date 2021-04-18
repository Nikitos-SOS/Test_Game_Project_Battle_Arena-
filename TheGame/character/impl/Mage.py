from TheGame.attack.type.common.mage.MageCommonAttack import MageCommonAttack
from TheGame.attack.type.spell.mage.FireBall import FireBall
from TheGame.attack.type.spell.mage.SunStrike import SunStrike
from TheGame.character.AbstractCharacter import AbstractCharacter


class Mage(AbstractCharacter):
    name = "Маг"

    health = 1000
    mana = 1000

    walk_range = 10

    common_attack = MageCommonAttack
    spells = [FireBall, SunStrike]

    def use_common_attack(self):
        damage = Mage.common_attack.damage
        return damage

    def cast_spell(self, spell_id):
        pass