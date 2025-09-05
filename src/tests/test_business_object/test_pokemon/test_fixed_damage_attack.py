from business_object.pokemon.fixed_damage_attack import FixedDamageAttack


class TestFixedAttackDamage:
    def test_compute_damage(self):
        # GIVEN
        attaque = FixedDamageAttack(name="Maiwenn", power=999, description="Pelle")

        # WHEN
        damage = attaque.compute_damage()

        # THEN
        assert damage == 999


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
