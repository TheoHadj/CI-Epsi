import random
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


class Character:
    def __init__(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁCharacterǁ__init____mutmut_orig(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_1(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = None
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_2(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 2
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_3(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = None
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_4(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 2
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_5(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = None
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_6(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 11
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_7(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = None
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_8(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 2
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_9(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = None

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_10(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 2

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_11(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = None
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_12(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance / self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_13(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2 / self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_14(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 3*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_15(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = None
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_16(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp - self.endurance
        self.force = 2*self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_17(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = None
        
    def xǁCharacterǁ__init____mutmut_18(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2*self.baseForce / self.lvl
        
    def xǁCharacterǁ__init____mutmut_19(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 2 / self.baseForce * self.lvl
        
    def xǁCharacterǁ__init____mutmut_20(self):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        self.baseAttack_power = 1
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.endurance = 2*self.baseEndurance * self.lvl
        self.hp = self.baseHp + self.endurance
        self.force = 3*self.baseForce * self.lvl
        
    
    xǁCharacterǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁ__init____mutmut_1': xǁCharacterǁ__init____mutmut_1, 
        'xǁCharacterǁ__init____mutmut_2': xǁCharacterǁ__init____mutmut_2, 
        'xǁCharacterǁ__init____mutmut_3': xǁCharacterǁ__init____mutmut_3, 
        'xǁCharacterǁ__init____mutmut_4': xǁCharacterǁ__init____mutmut_4, 
        'xǁCharacterǁ__init____mutmut_5': xǁCharacterǁ__init____mutmut_5, 
        'xǁCharacterǁ__init____mutmut_6': xǁCharacterǁ__init____mutmut_6, 
        'xǁCharacterǁ__init____mutmut_7': xǁCharacterǁ__init____mutmut_7, 
        'xǁCharacterǁ__init____mutmut_8': xǁCharacterǁ__init____mutmut_8, 
        'xǁCharacterǁ__init____mutmut_9': xǁCharacterǁ__init____mutmut_9, 
        'xǁCharacterǁ__init____mutmut_10': xǁCharacterǁ__init____mutmut_10, 
        'xǁCharacterǁ__init____mutmut_11': xǁCharacterǁ__init____mutmut_11, 
        'xǁCharacterǁ__init____mutmut_12': xǁCharacterǁ__init____mutmut_12, 
        'xǁCharacterǁ__init____mutmut_13': xǁCharacterǁ__init____mutmut_13, 
        'xǁCharacterǁ__init____mutmut_14': xǁCharacterǁ__init____mutmut_14, 
        'xǁCharacterǁ__init____mutmut_15': xǁCharacterǁ__init____mutmut_15, 
        'xǁCharacterǁ__init____mutmut_16': xǁCharacterǁ__init____mutmut_16, 
        'xǁCharacterǁ__init____mutmut_17': xǁCharacterǁ__init____mutmut_17, 
        'xǁCharacterǁ__init____mutmut_18': xǁCharacterǁ__init____mutmut_18, 
        'xǁCharacterǁ__init____mutmut_19': xǁCharacterǁ__init____mutmut_19, 
        'xǁCharacterǁ__init____mutmut_20': xǁCharacterǁ__init____mutmut_20
    }
    xǁCharacterǁ__init____mutmut_orig.__name__ = 'xǁCharacterǁ__init__'
    def is_alive(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁis_alive__mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁis_alive__mutmut_mutants'), args, kwargs, self)
    def xǁCharacterǁis_alive__mutmut_orig(self):
        return self.hp > 0
    def xǁCharacterǁis_alive__mutmut_1(self):
        return self.hp >= 0
    def xǁCharacterǁis_alive__mutmut_2(self):
        return self.hp > 1
    
    xǁCharacterǁis_alive__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁis_alive__mutmut_1': xǁCharacterǁis_alive__mutmut_1, 
        'xǁCharacterǁis_alive__mutmut_2': xǁCharacterǁis_alive__mutmut_2
    }
    xǁCharacterǁis_alive__mutmut_orig.__name__ = 'xǁCharacterǁis_alive'

    def take_damage(self, amount):
        args = [amount]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁtake_damage__mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁtake_damage__mutmut_mutants'), args, kwargs, self)

    def xǁCharacterǁtake_damage__mutmut_orig(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_1(self, amount):
        if isinstance(amount, (int, float)) or amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_2(self, amount):
        if isinstance(amount, (int, float)) and amount >= 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_3(self, amount):
        if isinstance(amount, (int, float)) and amount > 1:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_4(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = None
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_5(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) - self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_6(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(None) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_7(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = None
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_8(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(None, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_9(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, None)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_10(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_11(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, )
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_12(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(1, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_13(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp = amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_14(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp += amount
            if self.hp < 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_15(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp <= 0:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_16(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 1:
                self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_17(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = None

    def xǁCharacterǁtake_damage__mutmut_18(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = int(amount) + self.force
            amount = random.randint(0, amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 1
    
    xǁCharacterǁtake_damage__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁtake_damage__mutmut_1': xǁCharacterǁtake_damage__mutmut_1, 
        'xǁCharacterǁtake_damage__mutmut_2': xǁCharacterǁtake_damage__mutmut_2, 
        'xǁCharacterǁtake_damage__mutmut_3': xǁCharacterǁtake_damage__mutmut_3, 
        'xǁCharacterǁtake_damage__mutmut_4': xǁCharacterǁtake_damage__mutmut_4, 
        'xǁCharacterǁtake_damage__mutmut_5': xǁCharacterǁtake_damage__mutmut_5, 
        'xǁCharacterǁtake_damage__mutmut_6': xǁCharacterǁtake_damage__mutmut_6, 
        'xǁCharacterǁtake_damage__mutmut_7': xǁCharacterǁtake_damage__mutmut_7, 
        'xǁCharacterǁtake_damage__mutmut_8': xǁCharacterǁtake_damage__mutmut_8, 
        'xǁCharacterǁtake_damage__mutmut_9': xǁCharacterǁtake_damage__mutmut_9, 
        'xǁCharacterǁtake_damage__mutmut_10': xǁCharacterǁtake_damage__mutmut_10, 
        'xǁCharacterǁtake_damage__mutmut_11': xǁCharacterǁtake_damage__mutmut_11, 
        'xǁCharacterǁtake_damage__mutmut_12': xǁCharacterǁtake_damage__mutmut_12, 
        'xǁCharacterǁtake_damage__mutmut_13': xǁCharacterǁtake_damage__mutmut_13, 
        'xǁCharacterǁtake_damage__mutmut_14': xǁCharacterǁtake_damage__mutmut_14, 
        'xǁCharacterǁtake_damage__mutmut_15': xǁCharacterǁtake_damage__mutmut_15, 
        'xǁCharacterǁtake_damage__mutmut_16': xǁCharacterǁtake_damage__mutmut_16, 
        'xǁCharacterǁtake_damage__mutmut_17': xǁCharacterǁtake_damage__mutmut_17, 
        'xǁCharacterǁtake_damage__mutmut_18': xǁCharacterǁtake_damage__mutmut_18
    }
    xǁCharacterǁtake_damage__mutmut_orig.__name__ = 'xǁCharacterǁtake_damage'

    def attack(self, target):
        args = [target]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁattack__mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁattack__mutmut_mutants'), args, kwargs, self)

    def xǁCharacterǁattack__mutmut_orig(self, target):
        if self.is_alive():
            target.take_damage(self.baseAttack_power)

    def xǁCharacterǁattack__mutmut_1(self, target):
        if self.is_alive():
            target.take_damage(None)
    
    xǁCharacterǁattack__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁattack__mutmut_1': xǁCharacterǁattack__mutmut_1
    }
    xǁCharacterǁattack__mutmut_orig.__name__ = 'xǁCharacterǁattack'