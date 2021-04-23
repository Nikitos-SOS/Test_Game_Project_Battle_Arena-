from TheGame.Typing import typing
from TheGame.Hunter import Hunter
from TheGame.Warrior import Warrior
from TheGame.Mage import Mage
from TheGame.Character import Character


class Choice:
    player1: Character
    player2: Character

    def __init__(self) -> None:
        pass

    def choice__character(self):
        typing("1. Маг-волшебник ")
        typing("2. Воин-варвар ")
        typing("3. Охотник-следопыт ")

        typing(" \n Введите число [1,2,3]: ")
        player_class = int(input())
        if player_class == 1:
            return Mage()
        elif player_class == 2:
            return Warrior()
        elif player_class == 3:
            return Hunter()
        else:
            print("Что-то пошло не так(\nПопробуйте снова")
            return self.choice__character()

    def menu(self):
        typing("Перед началом поединка, выберите персонажа!")

        typing("Игрок №1 ")
        self.player1 = self.choice__character()

        typing("Игрок №2 ")
        self.player2 = self.choice__character()
