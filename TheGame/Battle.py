from Typing import typing
from Character import Character


class Battle():
    # player1: Character
    # player2: Character 

    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2

    def battle(self):
        round_counter = 1
        while(True):
            typing("Раунд "+ str(round_counter))

            typing("Ходит игрок 1")
            damage = self.make_a_turn(self.player1)
            self.player2.health = self.player2.health - int(damage)
            typing("HP player2 " + str(self.player2.health))

            typing("\nХодит игрок 2")
            damage = self.make_a_turn(self.player2)
            self.player1.health = self.player1.health - int(damage)
            typing("HP player2 " + str(self.player1.health))

            if(self.player2.health <= 0):
                return "player1 win"
            elif(self.player1.health <= 0):
                return "player2 win"
            
            round_counter += 1


    def make_a_turn(self,player):
        typing("Введите число [1,2,3]: ")
        attack = int(input())
        if(attack == 1):
            return int(player.simple__attack())
        elif(attack == 2):
            return int(player.hard__attack())
        elif(attack == 3):
            return int(player.alt__attack())
        else:
            typing("Промазал")
            return 0
        
