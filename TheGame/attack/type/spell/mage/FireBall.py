from TheGame.attack.type.AbstractSpellAttack import AbstractSpellAttack


class FireBall(AbstractSpellAttack):
    type_name = "Атакующее умение"

    range: 10.0
    damage: 10.0
    mana_cost: 10

    aoe_zone_radius = 1

    is_targeted_enemy: True
    is_targeted_yourself: False
    is_targeted_zone: False
