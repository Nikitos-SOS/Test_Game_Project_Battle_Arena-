from TheGame.attack.type.AbstractSpellAttack import AbstractSpellAttack


class SunStrike(AbstractSpellAttack):
    type_name = "Атакующее умение"

    range: 999.0
    damage: 200.0
    mana_cost: 150

    aoe_zone_radius = 5

    is_targeted_enemy: False
    is_targeted_yourself: False
    is_targeted_zone: True
