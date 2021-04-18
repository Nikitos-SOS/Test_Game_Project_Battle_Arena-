from random import randrange

from TheGame.attack.type.CommonAttack import CommonAttack


class MageCommonAttack(CommonAttack):
    damage = randrange(10, 15)
    range = 10.0
