class Character:
    def __init__(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
       
        self.lvl = 0

        self.attack_power = 2*self.baseAttack_power* self.lvl
        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 0
        
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def attack(self, target):
        if self.is_alive():
            target.take_damage(self.attack_power)