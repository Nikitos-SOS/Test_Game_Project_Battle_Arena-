

"""
    Абстрактный класс, описывает тип атаки.
    @see CommonAttack, SpellAttack
"""
class AbstractAttack:
    type_name: str

    range: float
    damage: float
    mana_cost: int

    aoe_zone_radius: int

