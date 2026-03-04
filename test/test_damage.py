from rpg.character import Character

class FakeRandom:
    def randint(self, a, b):
        return 3  # valeur fixe pour test

def test_attack_random_damage_between_0_and_D():
    rng = FakeRandom()
    attacker = Character("Hero", damage=5, rng=rng)
    defender = Character("Monster")

    attacker.attack(defender)

    assert defender.hp == 7  # 10 - 3
