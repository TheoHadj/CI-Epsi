import random

class Character:
    def __init__(self,level:int,end:int,force:int, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if(level<=0):
            raise ValueError("Le niveau doit être strictement positif")

        self.baseHp = 10

        self.lvl = level
        self.force = force
        self.endurance = end
        self.hp = self.baseHp + self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

                
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
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) * self.arme)
    
    def levelUp(self): #doesn't exists
        self.lvl += 1
        
        
class Equipe:
    def __init__(self, perso_1:Character, perso_2:Character):
        self.perso_1 = perso_1
        self.perso_2 = perso_2

    def est_morte(self):
        if self.perso_1.hp > 0 and self.perso_2.hp > 0:
            return False
        else:
            return True
    

class Duel:
    def __init__(self, equipe_1:Equipe, equipe_2:Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.perso_1 = equipe_1.perso_1
        self.perso_2= equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
        
    def who_wins(self):
        if self.equipe_1.est_morte():
            return 1
        elif self.equipe_2.est_morte():
            return 2
        return False
        
    def hp_equipe(self, equipe:Equipe):
        return equipe.perso_1.hp + equipe.perso_2.hp
        
    def attaque_equipe(self, equipe_attaque:Equipe, cible_1:Character, cible_2:Character):
        equipe_attaque.perso_1.attack(cible_1)
        equipe_attaque.perso_2.attack(cible_2)