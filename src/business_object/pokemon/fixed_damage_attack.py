from business_object.pokemon.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def __init__(self, name, power, description):
        super().__init__(name=name, power=power, description=description)

    def compute_damage(self):
        return self._power
