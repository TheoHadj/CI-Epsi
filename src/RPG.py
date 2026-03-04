import random


class Character:
    def __init__(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def attack(self, target):
        if self.is_alive():
            target.take_damage(self.baseAttack_power)