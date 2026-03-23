import random
import math

class Character:
    def __init__(self, level=1, end=0, force=0, agi=0, armor: int = 0, arme: float = 1.0):
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.lvl = level
        self.endurance = end
        self.force = force
        self.agi = agi
        self.armor = armor
        self.arme_multiplicator = arme if arme > 0 else 1.0
        
        self.max_hp = self._calculate_max_hp()
        self.hp = self.max_hp

    def _calculate_max_hp(self):
        return 10 + self.endurance + (2 * (self.lvl - 1))

    def _calculate_max_damage(self):
        return 1 + self.force + (2 * (self.lvl - 1))

    @property
    def is_priority_target(self):
        return self.hp < (0.3 * self.max_hp)

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            reduced_amount = amount * (1 - (self.armor / 100))
            
            if abs(reduced_amount % 1 - 0.5) < 1e-9:
                final_damage = int(reduced_amount)
            else:
                final_damage = round(reduced_amount)
            
            if final_damage > 0:
                self.hp -= final_damage
                if self.hp < 0:
                    self.hp = 0

    def attack(self, target):
        if self.is_alive():
            d_max = self._calculate_max_damage()
            base_dmg = random.randint(0, int(d_max))
            
            final_dmg = base_dmg * self.arme_multiplicator
            target.take_damage(final_dmg)

    def level_up(self):
        self.lvl += 1
        
        stat_to_boost = random.choice(['force', 'endurance', 'agi'])
        setattr(self, stat_to_boost, getattr(self, stat_to_boost) + 1)
        
        old_max_hp = self.max_hp
        self.max_hp = self._calculate_max_hp()
        
        self.hp += (self.max_hp - old_max_hp)

    def __repr__(self):
        return f"Char(Lvl:{self.lvl}, HP:{self.hp}/{self.max_hp}, FOR:{self.force}, AGI:{self.agi})"