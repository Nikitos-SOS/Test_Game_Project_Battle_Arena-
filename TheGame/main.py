import typing
from Battle import Battle
from Choice import Choice
from Warrior import Warrior
from Character import Character
from Mage import Mage
from Hunter import Hunter




# mage = Mage()


game = Choice()

game.menu()

battle = Battle(game.player1, game.player2)

typing(battle.battle())

