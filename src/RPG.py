import random
class Character:
    
    def __init__(self, arme_multiplicator:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10
        self.arme_multiplicator = arme_multiplicator if arme_multiplicator > 0 else 1
        self.attack
    
    def ajouter_arme(self, arme_multiplicator:int):
        self.arme_multiplicator = arme_multiplicator if arme_multiplicator > 0 else 1
                
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount)
            self.hp -= amount
            self.hp = round(self.hp)
            if self.hp < 0:
                self.hp = 0

    def attack(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force + 1) * self.arme_multiplicator)
    
    def levelUp(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2*self.baseEndurance