# import typing
from Battle import Battle
from Choice import Choice
from Warrior import Warrior
from Character import Character
from Mage import Mage
from Hunter import Hunter
from Typing import typing


# mage = Mage()
class main:
    def __init__(self):
        game = Choice()
        game.menu()
        battle = Battle(game.player1, game.player2)
        typing(battle.battle())


if __name__ == "__main__":
    main()
