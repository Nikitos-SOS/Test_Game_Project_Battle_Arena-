from random import randrange

from TheGame.attack.type.CommonAttack import CommonAttack


class HunterCommonAttack(CommonAttack):
    damage = randrange(15, 20)
    range = 8.0
