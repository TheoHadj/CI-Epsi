class Character:
    def __init__(self):
        # self.name = name
        # self.hp = hp
        self.hp = 10
        # self.attack_power = attack_power
        self.attack_power = 1
        
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def attack(self, target):
        if self.is_alive():
            target.take_damage(self.attack_power)