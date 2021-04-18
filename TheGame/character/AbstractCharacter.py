from abc import ABC, abstractmethod

from TheGame.attack.type.CommonAttack import CommonAttack


class AbstractCharacter:
    name: str

    health: int
    mana: int

    walk_range: int

    common_attack: CommonAttack
    spells: list

    def __init__(self) -> None:
        pass

    """
        Использование обычной атаки.
        @return damage
    """
    @abstractmethod
    def use_common_attack(self):
        """Переместить объект"""

    """
        Использование умения атаки.
        @return ???
    """
    @abstractmethod
    def cast_spell(self, spell_id):
        """Переместить объект"""