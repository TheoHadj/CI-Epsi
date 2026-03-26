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
    
    def est_en_danger(self):
        return self.hp < (self.maxHp * 0.3)

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
        
    def __str__(self):
        return f"Aventurier (Niv. {self.lvl}) - Santé: {self.hp}/{self.maxHp}"

class Equipe:
    def __init__(self, membre1: Character, membre2: Character):
        self.membre1 = membre1
        self.membre2 = membre2

    def isAlive(self):
        return self.membre1.is_alive() or self.membre2.is_alive()
    
    def whoLowest(self):
        m1_en_vie = self.membre1.is_alive()
        m2_en_vie = self.membre2.is_alive()
        
        if not m1_en_vie and not m2_en_vie: return None
        if not m1_en_vie: return self.membre2
        if not m2_en_vie: return self.membre1
        
        m1_danger = self.membre1.est_en_danger()
        m2_danger = self.membre2.est_en_danger()
        
        if m1_danger and not m2_danger:
            return self.membre1
        if m2_danger and not m1_danger:
            return self.membre2
            
        ratio1 = self.membre1.hp / self.membre1.maxHp
        ratio2 = self.membre2.hp / self.membre2.maxHp
        
        return self.membre1 if ratio1 <= ratio2 else self.membre2

class Duel:
    def __init__(self, equipe1: Equipe, equipe2: Equipe):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        
    def fight(self):
        limite_tours = 0
        while self.equipe1.isAlive() and self.equipe2.isAlive() and limite_tours < 1000:
            for combattant in self.getOrder():
                if combattant.is_alive():
                    equipe_ennemie = self.get_enemy_team(combattant)
                    cible = equipe_ennemie.whoLowest()
                    if cible: combattant.attack(cible)
            limite_tours += 1
        return 1 if self.equipe1.isAlive() else 2
        
    def getOrder(self):
        tous = [self.equipe1.membre1, self.equipe1.membre2, self.equipe2.membre1, self.equipe2.membre2]
        return sorted(tous, key=lambda p: p.agi, reverse=True)
    
    def get_enemy_team(self, combattant):
        if combattant in (self.equipe1.membre1, self.equipe1.membre2):
            return self.equipe2
        return self.equipe1