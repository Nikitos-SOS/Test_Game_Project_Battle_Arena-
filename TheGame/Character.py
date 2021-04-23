from abc import ABC, abstractmethod


class Character:
    name: str

    strength: int
    dexterity: int
    intelligence: int

    mana: int
    health: int
    damage: int

    def __init__(self) -> None:
        pass

    @abstractmethod
    def simple__attack(self):
        """Переместить объект"""

    @abstractmethod
    def hard__attack(self):
        """Переместить объект"""

    @abstractmethod
    def alt__attack(self):
        """Переместить объект"""
