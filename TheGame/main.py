# import typing
from TheGame.Battle import Battle
from TheGame.Choice import Choice
from TheGame.Warrior import Warrior
from TheGame.Character import Character
from TheGame.Mage import Mage
from TheGame.Hunter import Hunter
from TheGame.Typing import typing


# mage = Mage()
class main:
    def __init__(self):
        game = Choice()
        game.menu()
        battle = Battle(game.player1, game.player2)
        typing(battle.battle())


if __name__ == "__main__":
    main()
