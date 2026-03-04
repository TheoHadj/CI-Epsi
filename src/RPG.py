import random
import __future__

class Character:
    def __init__(self, name ="Unnamed", armor =0,  arme_multiplicator:int=1):
        self.name = name
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
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
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

    
def duel(self, ally: "Character", target: "Character", target1: "Character"):
        print("LE DUEL COMMENCE !")
        
        while (self.is_alive() or ally.is_alive()) and (target.is_alive() or target1.is_alive()):
            for attaquant in [self, ally, target, target1]:
                if attaquant.is_alive():
                    print(f"\nC'est au tour de {attaquant.name} (LVL {attaquant.lvl})")
                    
                    choix = ""
                    while choix not in ["1", "2","3","4"]:
                        choix = input(f"Qui attaquer ? () : ")
                    
                    cible = target if choix == "1" else target1
                    
                    if cible.is_alive():
                        attaquant.attack(cible)
                    else:
                        print("Cette cible est déjà KO ! Vous passez votre tour.")

        print("\n--- FIN DU COMBAT ---")