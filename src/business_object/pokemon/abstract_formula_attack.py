import random

from business_object.pokemon.abstract_attack import AbstractAttack


class AbstractFormulaAttack(AbstractAttack):
    def __init__(self, name, power, description):
        super().__init__(name=name, power=power, description=description)

    def compute_damage(self):
        random_factor = random.uniform(0.85, 1.0)
        base = (2 * self.level / 5) + 2
        modifier = (self.power * self.attack) / (self.defense * 50)
        damage = (base * modifier + 2) * random_factor
        return damage

    @abstractmethod
    def get_attack_stat(ABC):
        pass
