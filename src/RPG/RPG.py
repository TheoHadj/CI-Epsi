import random

class Character:
    def __init__(self, level: int = 1, end: int = 0, force: int = 0, agi: int = 0, chn: int = 0, armor: int = 0, arme: int = 1):
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if arme < 0:
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if level <= 0:
            raise ValueError("Le niveau doit être strictement positif")

        self.lvl = level
        self.force = force
        self.endurance = end
        self.agi = agi
        self.chn = chn
        self.armor = armor        
        self.arme = arme
        self.hp = 10 + self.endurance + 2 * self.lvl
        self.maxHp = self.hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
            if not isinstance(amount, (int, float)) or amount <= 0:
                return
                
            reduction = self.armor / 100
            reduced_amount = amount * (1 - reduction)
            
            if abs(reduced_amount % 1 - 0.5) < 1e-9:
                final_damage = int(reduced_amount)
            else:
                final_damage = round(reduced_amount)
            
            if amount >= 1 and final_damage <= 0 and reduction < 1:
                final_damage = 1
                
            self.hp -= final_damage
            if self.hp < 0:
                self.hp = 0

    def attack(self, target):
        if self.is_alive() and target:
            damage = random.randint(1, self.force + 2 + 2 * self.lvl) * self.arme
            target.take_damage(damage)
    
    def levelUp(self):
        self.lvl += 1
        self.hp += 2
        self.maxHp += 2
        
class Equipe:
    def __init__(self, perso1: Character, perso2: Character):
        self.perso1 = perso1
        self.perso2 = perso2

    def isAlive(self):
        return self.perso1.is_alive() or self.perso2.is_alive()
    
    def whoLowest(self):
        p1_alive = self.perso1.is_alive()
        p2_alive = self.perso2.is_alive()
        
        if not p1_alive and not p2_alive: return None
        if not p1_alive: return self.perso2
        if not p2_alive: return self.perso1
        
        ratio1 = self.perso1.hp / self.perso1.maxHp
        ratio2 = self.perso2.hp / self.perso2.maxHp
        
        return self.perso1 if ratio1 <= ratio2 else self.perso2

class Duel:
    def __init__(self, equipe1: Equipe, equipe2: Equipe):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        
    def fight(self):
        limit = 0
        while self.equipe1.isAlive() and self.equipe2.isAlive() and limit < 1000:
            for p in self.getOrder():
                if p.is_alive():
                    enemy = self.get_enemy_team(p)
                    target = enemy.whoLowest()
                    if target: p.attack(target)
            limit += 1
        return 1 if self.equipe1.isAlive() else 2
        
    def getOrder(self):
        tous = [self.equipe1.perso1, self.equipe1.perso2, self.equipe2.perso1, self.equipe2.perso2]
        return sorted(tous, key=lambda p: p.agi, reverse=True)
    
    def get_enemy_team(self, character):
        if character in (self.equipe1.perso1, self.equipe1.perso2):
            return self.equipe2
        return self.equipe1