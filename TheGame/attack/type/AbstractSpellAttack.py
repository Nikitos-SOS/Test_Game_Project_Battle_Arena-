from TheGame.attack.AbstractAttack import AbstractAttack


"""
    Абстрактный класс умения.
"""
class AbstractSpellAttack(AbstractAttack):
    is_targeted_enemy: bool
    is_targeted_yourself: bool
    is_targeted_zone: bool
