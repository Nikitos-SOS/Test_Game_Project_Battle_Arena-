from random import randrange

from TheGame.attack.type.CommonAttack import CommonAttack


class WarriorCommonAttack(CommonAttack):
    damage = randrange(20, 25)
    range = 1.0
