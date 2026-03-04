import random

class Character:
    def __init__(self,level:int,end:int,force:int, agi:int, chn:int, armor:int = 0,  arme:int=1):
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
        self.agi= 0
        self.chn=0
        #la chance marche comme suis => chaque tour quelqu'un esquive forcément parmis les chance une et tiré
        self.hp = self.baseHp + self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
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
    def __init__(self, perso1:Character, perso2:Character):
        self.perso1 = perso1
        self.perso2 = perso2

    def isAlive(self):
        if self.perso_1.hp==0 and self.perso_2.hp==0:
            return False
        else:
            return True
    
    def whoLowest(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) ==1):
                return self.perso1
            else:
                return self.perso2

            
        
            

class Duel:
    def __init__(self, equipe1:Equipe, equipe2:Equipe):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        
    def fight(self):

        while(self.equipe1.isAlive==False or self.equipe2.isAlive==False):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def getOrder(self):
        tous_les_combattants = [
        self.equipe1.perso_1, self.equipe1.perso_2,
        self.equipe2.perso_1, self.equipe2.perso_2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso_1, self.equipe1.perso_2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso_1, eq_adverse.perso_2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso_2 if p1 == eq_attaquante.perso_1 else eq_attaquante.perso_1
        p4 = eq_adverse.perso_2 if p2 == eq_adverse.perso_1 else eq_adverse.perso_1

        return [p1, p2, p3, p4]
    
    def get_enemy_team(self, character):
        return self.equipe2 if character in (self.equipe1.perso1, self.equipe1.perso2) else self.equipe1
    
    def get_enemy_team(self, character):
        return self.equipe2 if character in (self.equipe1.perso1, self.equipe1.perso2) else self.equipe1