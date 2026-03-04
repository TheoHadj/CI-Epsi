import random

class Character:
    def __init__(self, armor =0,  arme_multiplicator:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= armor <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme_multiplicator = arme_multiplicator if arme_multiplicator > 0 else 1
        self.attack
    
    def ajouter_arme(self, arme_multiplicator:int):
        self.arme_multiplicator = arme_multiplicator if arme_multiplicator > 0 else 1
                
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if(amount%1 ==0.5):
                amount = round(amount-0.1)
            else:
                amount=round(amount)
            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0
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
