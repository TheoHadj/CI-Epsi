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
    def __init__(self, armor:int = 0,  arme:int=1):
        args = [armor, arme]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁCharacterǁ__init____mutmut_orig(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_1(self, armor:int = 1,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_2(self, armor:int = 0,  arme:int=2):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_3(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_4(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (1 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_5(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 < int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_6(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(None) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_7(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) < 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_8(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 101):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_9(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError(None)
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_10(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("XXL'armure doit être comprise entre 0 et 100XX")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_11(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("l'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_12(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'ARMURE DOIT ÊTRE COMPRISE ENTRE 0 ET 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_13(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = None
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_14(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 2
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_15(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = None
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_16(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 11
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_17(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = None
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_18(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 2
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_19(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = None

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_20(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 1

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_21(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = None
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_22(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 1
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_23(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = None
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_24(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 1
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_25(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = None

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_26(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 11

        self.armor = armor
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_27(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = None
        
        self.arme = arme if arme > 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_28(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = None
        self.attack
    def xǁCharacterǁ__init____mutmut_29(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme >= 0 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_30(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 1 else 1
        self.attack
    def xǁCharacterǁ__init____mutmut_31(self, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        
        self.baseEndurance = 1
        self.baseHp = 10
        self.baseForce = 1
       
        self.lvl = 0

        self.force = 0
        self.endurance = 0
        self.hp = 10

        self.armor = armor
        
        self.arme = arme if arme > 0 else 2
        self.attack
    
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
        'xǁCharacterǁ__init____mutmut_20': xǁCharacterǁ__init____mutmut_20, 
        'xǁCharacterǁ__init____mutmut_21': xǁCharacterǁ__init____mutmut_21, 
        'xǁCharacterǁ__init____mutmut_22': xǁCharacterǁ__init____mutmut_22, 
        'xǁCharacterǁ__init____mutmut_23': xǁCharacterǁ__init____mutmut_23, 
        'xǁCharacterǁ__init____mutmut_24': xǁCharacterǁ__init____mutmut_24, 
        'xǁCharacterǁ__init____mutmut_25': xǁCharacterǁ__init____mutmut_25, 
        'xǁCharacterǁ__init____mutmut_26': xǁCharacterǁ__init____mutmut_26, 
        'xǁCharacterǁ__init____mutmut_27': xǁCharacterǁ__init____mutmut_27, 
        'xǁCharacterǁ__init____mutmut_28': xǁCharacterǁ__init____mutmut_28, 
        'xǁCharacterǁ__init____mutmut_29': xǁCharacterǁ__init____mutmut_29, 
        'xǁCharacterǁ__init____mutmut_30': xǁCharacterǁ__init____mutmut_30, 
        'xǁCharacterǁ__init____mutmut_31': xǁCharacterǁ__init____mutmut_31
    }
    xǁCharacterǁ__init____mutmut_orig.__name__ = 'xǁCharacterǁ__init__'
    
    def ajouter_arme(self, arme:int):
        args = [arme]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁajouter_arme__mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁajouter_arme__mutmut_mutants'), args, kwargs, self)
    
    def xǁCharacterǁajouter_arme__mutmut_orig(self, arme:int):
        self.arme = arme if arme > 0 else 1
    
    def xǁCharacterǁajouter_arme__mutmut_1(self, arme:int):
        self.arme = None
    
    def xǁCharacterǁajouter_arme__mutmut_2(self, arme:int):
        self.arme = arme if arme >= 0 else 1
    
    def xǁCharacterǁajouter_arme__mutmut_3(self, arme:int):
        self.arme = arme if arme > 1 else 1
    
    def xǁCharacterǁajouter_arme__mutmut_4(self, arme:int):
        self.arme = arme if arme > 0 else 2
    
    xǁCharacterǁajouter_arme__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁajouter_arme__mutmut_1': xǁCharacterǁajouter_arme__mutmut_1, 
        'xǁCharacterǁajouter_arme__mutmut_2': xǁCharacterǁajouter_arme__mutmut_2, 
        'xǁCharacterǁajouter_arme__mutmut_3': xǁCharacterǁajouter_arme__mutmut_3, 
        'xǁCharacterǁajouter_arme__mutmut_4': xǁCharacterǁajouter_arme__mutmut_4
    }
    xǁCharacterǁajouter_arme__mutmut_orig.__name__ = 'xǁCharacterǁajouter_arme'

    def ajouter_armure(self, armor:int):
        args = [armor]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁajouter_armure__mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁajouter_armure__mutmut_mutants'), args, kwargs, self)

    def xǁCharacterǁajouter_armure__mutmut_orig(self, armor:int):
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_1(self, armor:int):
        if (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_2(self, armor:int):
        if not (1 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_3(self, armor:int):
        if not (0 < int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_4(self, armor:int):
        if not (0 <= int(None) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_5(self, armor:int):
        if not (0 <= int(armor) < 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_6(self, armor:int):
        if not (0 <= int(armor) <= 101):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_7(self, armor:int):
        if not (0 <= int(armor) <= 100):
            raise ValueError(None)
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_8(self, armor:int):
        if not (0 <= int(armor) <= 100):
            raise ValueError("XXL'armure doit être comprise entre 0 et 100XX")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_9(self, armor:int):
        if not (0 <= int(armor) <= 100):
            raise ValueError("l'armure doit être comprise entre 0 et 100")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_10(self, armor:int):
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'ARMURE DOIT ÊTRE COMPRISE ENTRE 0 ET 100")
        self.armor = armor
                

    def xǁCharacterǁajouter_armure__mutmut_11(self, armor:int):
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        self.armor = None
                
    
    xǁCharacterǁajouter_armure__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁajouter_armure__mutmut_1': xǁCharacterǁajouter_armure__mutmut_1, 
        'xǁCharacterǁajouter_armure__mutmut_2': xǁCharacterǁajouter_armure__mutmut_2, 
        'xǁCharacterǁajouter_armure__mutmut_3': xǁCharacterǁajouter_armure__mutmut_3, 
        'xǁCharacterǁajouter_armure__mutmut_4': xǁCharacterǁajouter_armure__mutmut_4, 
        'xǁCharacterǁajouter_armure__mutmut_5': xǁCharacterǁajouter_armure__mutmut_5, 
        'xǁCharacterǁajouter_armure__mutmut_6': xǁCharacterǁajouter_armure__mutmut_6, 
        'xǁCharacterǁajouter_armure__mutmut_7': xǁCharacterǁajouter_armure__mutmut_7, 
        'xǁCharacterǁajouter_armure__mutmut_8': xǁCharacterǁajouter_armure__mutmut_8, 
        'xǁCharacterǁajouter_armure__mutmut_9': xǁCharacterǁajouter_armure__mutmut_9, 
        'xǁCharacterǁajouter_armure__mutmut_10': xǁCharacterǁajouter_armure__mutmut_10, 
        'xǁCharacterǁajouter_armure__mutmut_11': xǁCharacterǁajouter_armure__mutmut_11
    }
    xǁCharacterǁajouter_armure__mutmut_orig.__name__ = 'xǁCharacterǁajouter_armure'
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
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_1(self, amount):
        if isinstance(amount, (int, float)) or amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_2(self, amount):
        if isinstance(amount, (int, float)) and amount >= 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_3(self, amount):
        if isinstance(amount, (int, float)) and amount > 1:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_4(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = None
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_5(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount / (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_6(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 + (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_7(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (2 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_8(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor * 100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_9(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/101))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_10(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(None) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_11(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 + 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_12(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount / 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_13(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 2 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_14(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 1.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_15(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) <= 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_16(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1.000000001:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_17(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = None
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_18(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(None)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_19(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=None
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_20(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(None)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_21(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount >= 0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_22(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>1):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_23(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp = amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_24(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp += amount
                if self.hp < 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_25(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp <= 0:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_26(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 1:
                    self.hp = 0

    def xǁCharacterǁtake_damage__mutmut_27(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
                self.hp -= amount
                if self.hp < 0:
                    self.hp = None

    def xǁCharacterǁtake_damage__mutmut_28(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            amount = amount * (1 - (self.armor/100))
            if abs(amount % 1 - 0.5) < 1e-9:
                amount = int(amount)
            else:
                amount=round(amount)
                            
            if(amount>0):
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
        'xǁCharacterǁtake_damage__mutmut_18': xǁCharacterǁtake_damage__mutmut_18, 
        'xǁCharacterǁtake_damage__mutmut_19': xǁCharacterǁtake_damage__mutmut_19, 
        'xǁCharacterǁtake_damage__mutmut_20': xǁCharacterǁtake_damage__mutmut_20, 
        'xǁCharacterǁtake_damage__mutmut_21': xǁCharacterǁtake_damage__mutmut_21, 
        'xǁCharacterǁtake_damage__mutmut_22': xǁCharacterǁtake_damage__mutmut_22, 
        'xǁCharacterǁtake_damage__mutmut_23': xǁCharacterǁtake_damage__mutmut_23, 
        'xǁCharacterǁtake_damage__mutmut_24': xǁCharacterǁtake_damage__mutmut_24, 
        'xǁCharacterǁtake_damage__mutmut_25': xǁCharacterǁtake_damage__mutmut_25, 
        'xǁCharacterǁtake_damage__mutmut_26': xǁCharacterǁtake_damage__mutmut_26, 
        'xǁCharacterǁtake_damage__mutmut_27': xǁCharacterǁtake_damage__mutmut_27, 
        'xǁCharacterǁtake_damage__mutmut_28': xǁCharacterǁtake_damage__mutmut_28
    }
    xǁCharacterǁtake_damage__mutmut_orig.__name__ = 'xǁCharacterǁtake_damage'

    def attack(self, target):
        args = [target]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁattack__mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁattack__mutmut_mutants'), args, kwargs, self)

    def xǁCharacterǁattack__mutmut_orig(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force + 1) * self.arme)

    def xǁCharacterǁattack__mutmut_1(self, target):
        if self.is_alive():
            target.take_damage(None)

    def xǁCharacterǁattack__mutmut_2(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force + 1) / self.arme)

    def xǁCharacterǁattack__mutmut_3(self, target):
        if self.is_alive():
            target.take_damage(random.randint(None, self.force + 1) * self.arme)

    def xǁCharacterǁattack__mutmut_4(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, None) * self.arme)

    def xǁCharacterǁattack__mutmut_5(self, target):
        if self.is_alive():
            target.take_damage(random.randint(self.force + 1) * self.arme)

    def xǁCharacterǁattack__mutmut_6(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, ) * self.arme)

    def xǁCharacterǁattack__mutmut_7(self, target):
        if self.is_alive():
            target.take_damage(random.randint(1, self.force + 1) * self.arme)

    def xǁCharacterǁattack__mutmut_8(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force - 1) * self.arme)

    def xǁCharacterǁattack__mutmut_9(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force + 2) * self.arme)
    
    xǁCharacterǁattack__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁattack__mutmut_1': xǁCharacterǁattack__mutmut_1, 
        'xǁCharacterǁattack__mutmut_2': xǁCharacterǁattack__mutmut_2, 
        'xǁCharacterǁattack__mutmut_3': xǁCharacterǁattack__mutmut_3, 
        'xǁCharacterǁattack__mutmut_4': xǁCharacterǁattack__mutmut_4, 
        'xǁCharacterǁattack__mutmut_5': xǁCharacterǁattack__mutmut_5, 
        'xǁCharacterǁattack__mutmut_6': xǁCharacterǁattack__mutmut_6, 
        'xǁCharacterǁattack__mutmut_7': xǁCharacterǁattack__mutmut_7, 
        'xǁCharacterǁattack__mutmut_8': xǁCharacterǁattack__mutmut_8, 
        'xǁCharacterǁattack__mutmut_9': xǁCharacterǁattack__mutmut_9
    }
    xǁCharacterǁattack__mutmut_orig.__name__ = 'xǁCharacterǁattack'
    
    def levelUp(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁlevelUp__mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁlevelUp__mutmut_mutants'), args, kwargs, self)
    
    def xǁCharacterǁlevelUp__mutmut_orig(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_1(self):
        self.lvl = 1
        self.force += 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_2(self):
        self.lvl -= 1
        self.force += 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_3(self):
        self.lvl += 2
        self.force += 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_4(self):
        self.lvl += 1
        self.force = 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_5(self):
        self.lvl += 1
        self.force -= 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_6(self):
        self.lvl += 1
        self.force += 2 / self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_7(self):
        self.lvl += 1
        self.force += 3*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_8(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance = 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_9(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance -= 2*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_10(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance += 2 / self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_11(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance += 3*self.baseEndurance
        self.hp += 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_12(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp = 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_13(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp -= 2*self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_14(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 2 / self.baseEndurance
        
        
    
    def xǁCharacterǁlevelUp__mutmut_15(self):
        self.lvl += 1
        self.force += 2*self.baseForce
        self.endurance += 2*self.baseEndurance
        self.hp += 3*self.baseEndurance
        
        
    
    xǁCharacterǁlevelUp__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁlevelUp__mutmut_1': xǁCharacterǁlevelUp__mutmut_1, 
        'xǁCharacterǁlevelUp__mutmut_2': xǁCharacterǁlevelUp__mutmut_2, 
        'xǁCharacterǁlevelUp__mutmut_3': xǁCharacterǁlevelUp__mutmut_3, 
        'xǁCharacterǁlevelUp__mutmut_4': xǁCharacterǁlevelUp__mutmut_4, 
        'xǁCharacterǁlevelUp__mutmut_5': xǁCharacterǁlevelUp__mutmut_5, 
        'xǁCharacterǁlevelUp__mutmut_6': xǁCharacterǁlevelUp__mutmut_6, 
        'xǁCharacterǁlevelUp__mutmut_7': xǁCharacterǁlevelUp__mutmut_7, 
        'xǁCharacterǁlevelUp__mutmut_8': xǁCharacterǁlevelUp__mutmut_8, 
        'xǁCharacterǁlevelUp__mutmut_9': xǁCharacterǁlevelUp__mutmut_9, 
        'xǁCharacterǁlevelUp__mutmut_10': xǁCharacterǁlevelUp__mutmut_10, 
        'xǁCharacterǁlevelUp__mutmut_11': xǁCharacterǁlevelUp__mutmut_11, 
        'xǁCharacterǁlevelUp__mutmut_12': xǁCharacterǁlevelUp__mutmut_12, 
        'xǁCharacterǁlevelUp__mutmut_13': xǁCharacterǁlevelUp__mutmut_13, 
        'xǁCharacterǁlevelUp__mutmut_14': xǁCharacterǁlevelUp__mutmut_14, 
        'xǁCharacterǁlevelUp__mutmut_15': xǁCharacterǁlevelUp__mutmut_15
    }
    xǁCharacterǁlevelUp__mutmut_orig.__name__ = 'xǁCharacterǁlevelUp'
class Equipe:
    def __init__(self, perso_1:Character, perso_2:Character):
        args = [perso_1, perso_2]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁEquipeǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁEquipeǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁEquipeǁ__init____mutmut_orig(self, perso_1:Character, perso_2:Character):
        self.perso_1 = perso_1
        self.perso_2 = perso_2
    def xǁEquipeǁ__init____mutmut_1(self, perso_1:Character, perso_2:Character):
        self.perso_1 = None
        self.perso_2 = perso_2
    def xǁEquipeǁ__init____mutmut_2(self, perso_1:Character, perso_2:Character):
        self.perso_1 = perso_1
        self.perso_2 = None
    
    xǁEquipeǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁEquipeǁ__init____mutmut_1': xǁEquipeǁ__init____mutmut_1, 
        'xǁEquipeǁ__init____mutmut_2': xǁEquipeǁ__init____mutmut_2
    }
    xǁEquipeǁ__init____mutmut_orig.__name__ = 'xǁEquipeǁ__init__'

    def est_morte(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁEquipeǁest_morte__mutmut_orig'), object.__getattribute__(self, 'xǁEquipeǁest_morte__mutmut_mutants'), args, kwargs, self)

    def xǁEquipeǁest_morte__mutmut_orig(self):
        if self.perso_1.hp > 0 and self.perso_2.hp > 0:
            return False
        else:
            return True

    def xǁEquipeǁest_morte__mutmut_1(self):
        if self.perso_1.hp > 0 or self.perso_2.hp > 0:
            return False
        else:
            return True

    def xǁEquipeǁest_morte__mutmut_2(self):
        if self.perso_1.hp >= 0 and self.perso_2.hp > 0:
            return False
        else:
            return True

    def xǁEquipeǁest_morte__mutmut_3(self):
        if self.perso_1.hp > 1 and self.perso_2.hp > 0:
            return False
        else:
            return True

    def xǁEquipeǁest_morte__mutmut_4(self):
        if self.perso_1.hp > 0 and self.perso_2.hp >= 0:
            return False
        else:
            return True

    def xǁEquipeǁest_morte__mutmut_5(self):
        if self.perso_1.hp > 0 and self.perso_2.hp > 1:
            return False
        else:
            return True

    def xǁEquipeǁest_morte__mutmut_6(self):
        if self.perso_1.hp > 0 and self.perso_2.hp > 0:
            return True
        else:
            return True

    def xǁEquipeǁest_morte__mutmut_7(self):
        if self.perso_1.hp > 0 and self.perso_2.hp > 0:
            return False
        else:
            return False
    
    xǁEquipeǁest_morte__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁEquipeǁest_morte__mutmut_1': xǁEquipeǁest_morte__mutmut_1, 
        'xǁEquipeǁest_morte__mutmut_2': xǁEquipeǁest_morte__mutmut_2, 
        'xǁEquipeǁest_morte__mutmut_3': xǁEquipeǁest_morte__mutmut_3, 
        'xǁEquipeǁest_morte__mutmut_4': xǁEquipeǁest_morte__mutmut_4, 
        'xǁEquipeǁest_morte__mutmut_5': xǁEquipeǁest_morte__mutmut_5, 
        'xǁEquipeǁest_morte__mutmut_6': xǁEquipeǁest_morte__mutmut_6, 
        'xǁEquipeǁest_morte__mutmut_7': xǁEquipeǁest_morte__mutmut_7
    }
    xǁEquipeǁest_morte__mutmut_orig.__name__ = 'xǁEquipeǁest_morte'
    

class Duel:
    def __init__(self, equipe_1:Equipe, equipe_2:Equipe):
        args = [equipe_1, equipe_2]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁDuelǁ__init____mutmut_orig(self, equipe_1:Equipe, equipe_2:Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.perso_1 = equipe_1.perso_1
        self.perso_2= equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
        
    def xǁDuelǁ__init____mutmut_1(self, equipe_1:Equipe, equipe_2:Equipe):
        self.equipe_1 = None
        self.equipe_2 = equipe_2
        self.perso_1 = equipe_1.perso_1
        self.perso_2= equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
        
    def xǁDuelǁ__init____mutmut_2(self, equipe_1:Equipe, equipe_2:Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = None
        self.perso_1 = equipe_1.perso_1
        self.perso_2= equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
        
    def xǁDuelǁ__init____mutmut_3(self, equipe_1:Equipe, equipe_2:Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.perso_1 = None
        self.perso_2= equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
        
    def xǁDuelǁ__init____mutmut_4(self, equipe_1:Equipe, equipe_2:Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.perso_1 = equipe_1.perso_1
        self.perso_2= None
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
        
    def xǁDuelǁ__init____mutmut_5(self, equipe_1:Equipe, equipe_2:Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.perso_1 = equipe_1.perso_1
        self.perso_2= equipe_1.perso_2
        self.perso_3 = None
        self.perso_4 = equipe_2.perso_2
        
    def xǁDuelǁ__init____mutmut_6(self, equipe_1:Equipe, equipe_2:Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.perso_1 = equipe_1.perso_1
        self.perso_2= equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = None
        
    
    xǁDuelǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁ__init____mutmut_1': xǁDuelǁ__init____mutmut_1, 
        'xǁDuelǁ__init____mutmut_2': xǁDuelǁ__init____mutmut_2, 
        'xǁDuelǁ__init____mutmut_3': xǁDuelǁ__init____mutmut_3, 
        'xǁDuelǁ__init____mutmut_4': xǁDuelǁ__init____mutmut_4, 
        'xǁDuelǁ__init____mutmut_5': xǁDuelǁ__init____mutmut_5, 
        'xǁDuelǁ__init____mutmut_6': xǁDuelǁ__init____mutmut_6
    }
    xǁDuelǁ__init____mutmut_orig.__name__ = 'xǁDuelǁ__init__'
    def who_wins(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁwho_wins__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁwho_wins__mutmut_mutants'), args, kwargs, self)
    def xǁDuelǁwho_wins__mutmut_orig(self):
        if self.equipe_1.est_morte():
            return 1
        elif self.equipe_2.est_morte():
            return 2
        return False
        
    def xǁDuelǁwho_wins__mutmut_1(self):
        if self.equipe_1.est_morte():
            return 2
        elif self.equipe_2.est_morte():
            return 2
        return False
        
    def xǁDuelǁwho_wins__mutmut_2(self):
        if self.equipe_1.est_morte():
            return 1
        elif self.equipe_2.est_morte():
            return 3
        return False
        
    def xǁDuelǁwho_wins__mutmut_3(self):
        if self.equipe_1.est_morte():
            return 1
        elif self.equipe_2.est_morte():
            return 2
        return True
        
    
    xǁDuelǁwho_wins__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁwho_wins__mutmut_1': xǁDuelǁwho_wins__mutmut_1, 
        'xǁDuelǁwho_wins__mutmut_2': xǁDuelǁwho_wins__mutmut_2, 
        'xǁDuelǁwho_wins__mutmut_3': xǁDuelǁwho_wins__mutmut_3
    }
    xǁDuelǁwho_wins__mutmut_orig.__name__ = 'xǁDuelǁwho_wins'
    def hp_equipe(self, equipe:Equipe):
        args = [equipe]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁhp_equipe__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁhp_equipe__mutmut_mutants'), args, kwargs, self)
    def xǁDuelǁhp_equipe__mutmut_orig(self, equipe:Equipe):
        return equipe.perso_1.hp + equipe.perso_2.hp
        
    def xǁDuelǁhp_equipe__mutmut_1(self, equipe:Equipe):
        return equipe.perso_1.hp - equipe.perso_2.hp
        
    
    xǁDuelǁhp_equipe__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁhp_equipe__mutmut_1': xǁDuelǁhp_equipe__mutmut_1
    }
    xǁDuelǁhp_equipe__mutmut_orig.__name__ = 'xǁDuelǁhp_equipe'
    def attaque_equipe(self, equipe_attaque:Equipe, cible_1:Character, cible_2:Character):
        args = [equipe_attaque, cible_1, cible_2]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁattaque_equipe__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁattaque_equipe__mutmut_mutants'), args, kwargs, self)
    def xǁDuelǁattaque_equipe__mutmut_orig(self, equipe_attaque:Equipe, cible_1:Character, cible_2:Character):
        equipe_attaque.perso_1.attack(cible_1)
        equipe_attaque.perso_2.attack(cible_2)

        
    def xǁDuelǁattaque_equipe__mutmut_1(self, equipe_attaque:Equipe, cible_1:Character, cible_2:Character):
        equipe_attaque.perso_1.attack(None)
        equipe_attaque.perso_2.attack(cible_2)

        
    def xǁDuelǁattaque_equipe__mutmut_2(self, equipe_attaque:Equipe, cible_1:Character, cible_2:Character):
        equipe_attaque.perso_1.attack(cible_1)
        equipe_attaque.perso_2.attack(None)

        
    
    xǁDuelǁattaque_equipe__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁattaque_equipe__mutmut_1': xǁDuelǁattaque_equipe__mutmut_1, 
        'xǁDuelǁattaque_equipe__mutmut_2': xǁDuelǁattaque_equipe__mutmut_2
    }
    xǁDuelǁattaque_equipe__mutmut_orig.__name__ = 'xǁDuelǁattaque_equipe'
    
    
