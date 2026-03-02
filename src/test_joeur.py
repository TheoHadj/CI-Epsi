class Joeur:
    def __init__(self):
        self.hp = 100
    def attack(self, other):
        other.hp -= 10
          if other.hp < 0:
            other.hp = 0
