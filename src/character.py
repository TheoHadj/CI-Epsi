import random

class Character:
    def __init__(self, name, damage=1, rng=None):
        self.name = name
        self.hp = 10
        self.damage = damage
        self.rng = rng if rng else random

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        if not other.is_alive():
            return

        damage = self.rng.randint(0, self.damage)
        other.hp = max(0, other.hp - damage)
