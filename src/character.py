class Character:
    def __init__(self):
        self.hp = 10

    def attack(self, other):
        if other.hp > 0:
            other.hp -= 1
        if other.hp < 0:
            other.hp = 0

    def is_alive(self):
        return self.hp > 0
