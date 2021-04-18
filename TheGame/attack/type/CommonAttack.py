from TheGame.attack.AbstractAttack import AbstractAttack


"""
    Класс обычной атаки (с руки).
"""
class CommonAttack(AbstractAttack):
    type_name = "Обычная атака"

    mana_cost = 0

    aoe_zone_radius = 1
