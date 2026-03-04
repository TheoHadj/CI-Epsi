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
    def __init__(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
        args = [force, endurance, agilite, chance, armor, arme]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁCharacterǁ__init____mutmut_orig(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_1(self, force:int=1, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_2(self, force:int=0, endurance:int=1, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_3(self, force:int=0, endurance:int=0, agilite:int=1, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_4(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=1, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_5(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 1,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_6(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=2):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_7(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_8(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_9(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_10(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_11(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_12(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_13(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_14(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_15(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_16(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_17(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_18(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_19(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_20(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_21(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_22(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_23(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_24(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_25(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_26(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_27(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_28(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_29(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_30(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_31(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_32(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_33(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_34(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_35(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_36(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = None
        self.chance = chance
    def xǁCharacterǁ__init____mutmut_37(self, force:int=0, endurance:int=0, agilite:int=0, chance:int=0, armor:int = 0,  arme:int=1):
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
        self.agilite = agilite
        self.chance = None
    
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
        'xǁCharacterǁ__init____mutmut_31': xǁCharacterǁ__init____mutmut_31, 
        'xǁCharacterǁ__init____mutmut_32': xǁCharacterǁ__init____mutmut_32, 
        'xǁCharacterǁ__init____mutmut_33': xǁCharacterǁ__init____mutmut_33, 
        'xǁCharacterǁ__init____mutmut_34': xǁCharacterǁ__init____mutmut_34, 
        'xǁCharacterǁ__init____mutmut_35': xǁCharacterǁ__init____mutmut_35, 
        'xǁCharacterǁ__init____mutmut_36': xǁCharacterǁ__init____mutmut_36, 
        'xǁCharacterǁ__init____mutmut_37': xǁCharacterǁ__init____mutmut_37
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
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_1(self, target):
        if self.is_alive() or target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_2(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = None
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_3(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(None)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_4(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) / self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_5(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(None, self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_6(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, None) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_7(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_8(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, ) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_9(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(1, self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_10(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 - 2*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_11(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force - 1 + 2*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_12(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 2 + 2*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_13(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 + 2 / self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_14(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 + 3*self.lvl) * self.arme)
            if before_hp > 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_15(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp > 0 or not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_16(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp >= 0 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_17(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp > 1 and not target.is_alive():
                self.levelUp()
                

    def xǁCharacterǁattack__mutmut_18(self, target):
        if self.is_alive() and target.is_alive():
            before_hp = target.hp
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) * self.arme)
            if before_hp > 0 and target.is_alive():
                self.levelUp()
                
    
    xǁCharacterǁattack__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁattack__mutmut_1': xǁCharacterǁattack__mutmut_1, 
        'xǁCharacterǁattack__mutmut_2': xǁCharacterǁattack__mutmut_2, 
        'xǁCharacterǁattack__mutmut_3': xǁCharacterǁattack__mutmut_3, 
        'xǁCharacterǁattack__mutmut_4': xǁCharacterǁattack__mutmut_4, 
        'xǁCharacterǁattack__mutmut_5': xǁCharacterǁattack__mutmut_5, 
        'xǁCharacterǁattack__mutmut_6': xǁCharacterǁattack__mutmut_6, 
        'xǁCharacterǁattack__mutmut_7': xǁCharacterǁattack__mutmut_7, 
        'xǁCharacterǁattack__mutmut_8': xǁCharacterǁattack__mutmut_8, 
        'xǁCharacterǁattack__mutmut_9': xǁCharacterǁattack__mutmut_9, 
        'xǁCharacterǁattack__mutmut_10': xǁCharacterǁattack__mutmut_10, 
        'xǁCharacterǁattack__mutmut_11': xǁCharacterǁattack__mutmut_11, 
        'xǁCharacterǁattack__mutmut_12': xǁCharacterǁattack__mutmut_12, 
        'xǁCharacterǁattack__mutmut_13': xǁCharacterǁattack__mutmut_13, 
        'xǁCharacterǁattack__mutmut_14': xǁCharacterǁattack__mutmut_14, 
        'xǁCharacterǁattack__mutmut_15': xǁCharacterǁattack__mutmut_15, 
        'xǁCharacterǁattack__mutmut_16': xǁCharacterǁattack__mutmut_16, 
        'xǁCharacterǁattack__mutmut_17': xǁCharacterǁattack__mutmut_17, 
        'xǁCharacterǁattack__mutmut_18': xǁCharacterǁattack__mutmut_18
    }
    xǁCharacterǁattack__mutmut_orig.__name__ = 'xǁCharacterǁattack'
    def levelUp(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁlevelUp__mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁlevelUp__mutmut_mutants'), args, kwargs, self)
    def xǁCharacterǁlevelUp__mutmut_orig(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_1(self):
        self.lvl = 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_2(self):
        self.lvl -= 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_3(self):
        self.lvl += 2
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_4(self):
        self.lvl += 1
        self.hp = 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_5(self):
        self.lvl += 1
        self.hp -= 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_6(self):
        self.lvl += 1
        self.hp += 3

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_7(self):
        self.lvl += 1
        self.hp += 2

        stat = None
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_8(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(None)
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_9(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["XXforceXX", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_10(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["FORCE", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_11(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "XXenduranceXX", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_12(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "ENDURANCE", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_13(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "XXagiliteXX", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_14(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "AGILITE", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_15(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "XXchanceXX"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_16(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "CHANCE"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_17(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat != "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_18(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "XXforceXX":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_19(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "FORCE":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_20(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force = 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_21(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force -= 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_22(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 2
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_23(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat != "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_24(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "XXenduranceXX":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_25(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "ENDURANCE":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_26(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance = 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_27(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance -= 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_28(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 2
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_29(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp = 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_30(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp -= 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_31(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 2
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_32(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat != "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_33(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "XXagiliteXX":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_34(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "AGILITE":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_35(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite = 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_36(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite -= 1
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_37(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 2
        elif stat == "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_38(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat != "chance":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_39(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "XXchanceXX":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_40(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "CHANCE":
            self.chance += 1
            
        
    def xǁCharacterǁlevelUp__mutmut_41(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance = 1
            
        
    def xǁCharacterǁlevelUp__mutmut_42(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance -= 1
            
        
    def xǁCharacterǁlevelUp__mutmut_43(self):
        self.lvl += 1
        self.hp += 2

        stat = random.choice(["force", "endurance", "agilite", "chance"])
        
        if stat == "force":
            self.force += 1
        elif stat == "endurance":
            self.endurance += 1
            self.hp += 1
        elif stat == "agilite":
            self.agilite += 1
        elif stat == "chance":
            self.chance += 2
            
        
    
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
        'xǁCharacterǁlevelUp__mutmut_15': xǁCharacterǁlevelUp__mutmut_15, 
        'xǁCharacterǁlevelUp__mutmut_16': xǁCharacterǁlevelUp__mutmut_16, 
        'xǁCharacterǁlevelUp__mutmut_17': xǁCharacterǁlevelUp__mutmut_17, 
        'xǁCharacterǁlevelUp__mutmut_18': xǁCharacterǁlevelUp__mutmut_18, 
        'xǁCharacterǁlevelUp__mutmut_19': xǁCharacterǁlevelUp__mutmut_19, 
        'xǁCharacterǁlevelUp__mutmut_20': xǁCharacterǁlevelUp__mutmut_20, 
        'xǁCharacterǁlevelUp__mutmut_21': xǁCharacterǁlevelUp__mutmut_21, 
        'xǁCharacterǁlevelUp__mutmut_22': xǁCharacterǁlevelUp__mutmut_22, 
        'xǁCharacterǁlevelUp__mutmut_23': xǁCharacterǁlevelUp__mutmut_23, 
        'xǁCharacterǁlevelUp__mutmut_24': xǁCharacterǁlevelUp__mutmut_24, 
        'xǁCharacterǁlevelUp__mutmut_25': xǁCharacterǁlevelUp__mutmut_25, 
        'xǁCharacterǁlevelUp__mutmut_26': xǁCharacterǁlevelUp__mutmut_26, 
        'xǁCharacterǁlevelUp__mutmut_27': xǁCharacterǁlevelUp__mutmut_27, 
        'xǁCharacterǁlevelUp__mutmut_28': xǁCharacterǁlevelUp__mutmut_28, 
        'xǁCharacterǁlevelUp__mutmut_29': xǁCharacterǁlevelUp__mutmut_29, 
        'xǁCharacterǁlevelUp__mutmut_30': xǁCharacterǁlevelUp__mutmut_30, 
        'xǁCharacterǁlevelUp__mutmut_31': xǁCharacterǁlevelUp__mutmut_31, 
        'xǁCharacterǁlevelUp__mutmut_32': xǁCharacterǁlevelUp__mutmut_32, 
        'xǁCharacterǁlevelUp__mutmut_33': xǁCharacterǁlevelUp__mutmut_33, 
        'xǁCharacterǁlevelUp__mutmut_34': xǁCharacterǁlevelUp__mutmut_34, 
        'xǁCharacterǁlevelUp__mutmut_35': xǁCharacterǁlevelUp__mutmut_35, 
        'xǁCharacterǁlevelUp__mutmut_36': xǁCharacterǁlevelUp__mutmut_36, 
        'xǁCharacterǁlevelUp__mutmut_37': xǁCharacterǁlevelUp__mutmut_37, 
        'xǁCharacterǁlevelUp__mutmut_38': xǁCharacterǁlevelUp__mutmut_38, 
        'xǁCharacterǁlevelUp__mutmut_39': xǁCharacterǁlevelUp__mutmut_39, 
        'xǁCharacterǁlevelUp__mutmut_40': xǁCharacterǁlevelUp__mutmut_40, 
        'xǁCharacterǁlevelUp__mutmut_41': xǁCharacterǁlevelUp__mutmut_41, 
        'xǁCharacterǁlevelUp__mutmut_42': xǁCharacterǁlevelUp__mutmut_42, 
        'xǁCharacterǁlevelUp__mutmut_43': xǁCharacterǁlevelUp__mutmut_43
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
    def __init__(self, equipe_1: Equipe, equipe_2: Equipe):
        args = [equipe_1, equipe_2]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁDuelǁ__init____mutmut_orig(self, equipe_1: Equipe, equipe_2: Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2

        self.perso_1 = equipe_1.perso_1
        self.perso_2 = equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
    def xǁDuelǁ__init____mutmut_1(self, equipe_1: Equipe, equipe_2: Equipe):
        self.equipe_1 = None
        self.equipe_2 = equipe_2

        self.perso_1 = equipe_1.perso_1
        self.perso_2 = equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
    def xǁDuelǁ__init____mutmut_2(self, equipe_1: Equipe, equipe_2: Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = None

        self.perso_1 = equipe_1.perso_1
        self.perso_2 = equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
    def xǁDuelǁ__init____mutmut_3(self, equipe_1: Equipe, equipe_2: Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2

        self.perso_1 = None
        self.perso_2 = equipe_1.perso_2
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
    def xǁDuelǁ__init____mutmut_4(self, equipe_1: Equipe, equipe_2: Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2

        self.perso_1 = equipe_1.perso_1
        self.perso_2 = None
        self.perso_3 = equipe_2.perso_1
        self.perso_4 = equipe_2.perso_2
    def xǁDuelǁ__init____mutmut_5(self, equipe_1: Equipe, equipe_2: Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2

        self.perso_1 = equipe_1.perso_1
        self.perso_2 = equipe_1.perso_2
        self.perso_3 = None
        self.perso_4 = equipe_2.perso_2
    def xǁDuelǁ__init____mutmut_6(self, equipe_1: Equipe, equipe_2: Equipe):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2

        self.perso_1 = equipe_1.perso_1
        self.perso_2 = equipe_1.perso_2
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
            return 2
        elif self.equipe_2.est_morte():
            return 1
        return False

    def xǁDuelǁwho_wins__mutmut_1(self):
        if self.equipe_1.est_morte():
            return 3
        elif self.equipe_2.est_morte():
            return 1
        return False

    def xǁDuelǁwho_wins__mutmut_2(self):
        if self.equipe_1.est_morte():
            return 2
        elif self.equipe_2.est_morte():
            return 2
        return False

    def xǁDuelǁwho_wins__mutmut_3(self):
        if self.equipe_1.est_morte():
            return 2
        elif self.equipe_2.est_morte():
            return 1
        return True
    
    xǁDuelǁwho_wins__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁwho_wins__mutmut_1': xǁDuelǁwho_wins__mutmut_1, 
        'xǁDuelǁwho_wins__mutmut_2': xǁDuelǁwho_wins__mutmut_2, 
        'xǁDuelǁwho_wins__mutmut_3': xǁDuelǁwho_wins__mutmut_3
    }
    xǁDuelǁwho_wins__mutmut_orig.__name__ = 'xǁDuelǁwho_wins'

    def hp_equipe(self, equipe: Equipe):
        args = [equipe]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁhp_equipe__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁhp_equipe__mutmut_mutants'), args, kwargs, self)

    def xǁDuelǁhp_equipe__mutmut_orig(self, equipe: Equipe):
        return equipe.perso_1.hp + equipe.perso_2.hp

    def xǁDuelǁhp_equipe__mutmut_1(self, equipe: Equipe):
        return equipe.perso_1.hp - equipe.perso_2.hp
    
    xǁDuelǁhp_equipe__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁhp_equipe__mutmut_1': xǁDuelǁhp_equipe__mutmut_1
    }
    xǁDuelǁhp_equipe__mutmut_orig.__name__ = 'xǁDuelǁhp_equipe'

    def choisir_cible(self, p1: Character, p2: Character):
        args = [p1, p2]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁchoisir_cible__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁchoisir_cible__mutmut_mutants'), args, kwargs, self)

    def xǁDuelǁchoisir_cible__mutmut_orig(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_1(self, p1: Character, p2: Character):
        cibles = None

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_2(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) != 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_3(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 2:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_4(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[1]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_5(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = None
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_6(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = None
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_7(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 * (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_8(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 2 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_9(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp - 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_10(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 2)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_11(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = None 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_12(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 * (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_13(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 2 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_14(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance - 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_15(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 2) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_16(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(None)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_17(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp - vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_18(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = None
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_19(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(None)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_20(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = None

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_21(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(None, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_22(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, None)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_23(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_24(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, )

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_25(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(1, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_26(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = None
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_27(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 1
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_28(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(None):
            cumul += scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_29(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul = scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_30(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul -= scores[i]
            if r <= cumul:
                return p

    def xǁDuelǁchoisir_cible__mutmut_31(self, p1: Character, p2: Character):
        cibles = [p for p in [p1, p2] if p.is_alive()]

        if len(cibles) == 1:
            return cibles[0]

        scores = []
        for p in cibles:
            vuln_hp = 1 / (p.hp + 1)
            vuln_chance = 1 / (p.chance + 1) 
            scores.append(vuln_hp + vuln_chance)

        total = sum(scores)
        r = random.uniform(0, total)

        cumul = 0
        for i, p in enumerate(cibles):
            cumul += scores[i]
            if r < cumul:
                return p
    
    xǁDuelǁchoisir_cible__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁchoisir_cible__mutmut_1': xǁDuelǁchoisir_cible__mutmut_1, 
        'xǁDuelǁchoisir_cible__mutmut_2': xǁDuelǁchoisir_cible__mutmut_2, 
        'xǁDuelǁchoisir_cible__mutmut_3': xǁDuelǁchoisir_cible__mutmut_3, 
        'xǁDuelǁchoisir_cible__mutmut_4': xǁDuelǁchoisir_cible__mutmut_4, 
        'xǁDuelǁchoisir_cible__mutmut_5': xǁDuelǁchoisir_cible__mutmut_5, 
        'xǁDuelǁchoisir_cible__mutmut_6': xǁDuelǁchoisir_cible__mutmut_6, 
        'xǁDuelǁchoisir_cible__mutmut_7': xǁDuelǁchoisir_cible__mutmut_7, 
        'xǁDuelǁchoisir_cible__mutmut_8': xǁDuelǁchoisir_cible__mutmut_8, 
        'xǁDuelǁchoisir_cible__mutmut_9': xǁDuelǁchoisir_cible__mutmut_9, 
        'xǁDuelǁchoisir_cible__mutmut_10': xǁDuelǁchoisir_cible__mutmut_10, 
        'xǁDuelǁchoisir_cible__mutmut_11': xǁDuelǁchoisir_cible__mutmut_11, 
        'xǁDuelǁchoisir_cible__mutmut_12': xǁDuelǁchoisir_cible__mutmut_12, 
        'xǁDuelǁchoisir_cible__mutmut_13': xǁDuelǁchoisir_cible__mutmut_13, 
        'xǁDuelǁchoisir_cible__mutmut_14': xǁDuelǁchoisir_cible__mutmut_14, 
        'xǁDuelǁchoisir_cible__mutmut_15': xǁDuelǁchoisir_cible__mutmut_15, 
        'xǁDuelǁchoisir_cible__mutmut_16': xǁDuelǁchoisir_cible__mutmut_16, 
        'xǁDuelǁchoisir_cible__mutmut_17': xǁDuelǁchoisir_cible__mutmut_17, 
        'xǁDuelǁchoisir_cible__mutmut_18': xǁDuelǁchoisir_cible__mutmut_18, 
        'xǁDuelǁchoisir_cible__mutmut_19': xǁDuelǁchoisir_cible__mutmut_19, 
        'xǁDuelǁchoisir_cible__mutmut_20': xǁDuelǁchoisir_cible__mutmut_20, 
        'xǁDuelǁchoisir_cible__mutmut_21': xǁDuelǁchoisir_cible__mutmut_21, 
        'xǁDuelǁchoisir_cible__mutmut_22': xǁDuelǁchoisir_cible__mutmut_22, 
        'xǁDuelǁchoisir_cible__mutmut_23': xǁDuelǁchoisir_cible__mutmut_23, 
        'xǁDuelǁchoisir_cible__mutmut_24': xǁDuelǁchoisir_cible__mutmut_24, 
        'xǁDuelǁchoisir_cible__mutmut_25': xǁDuelǁchoisir_cible__mutmut_25, 
        'xǁDuelǁchoisir_cible__mutmut_26': xǁDuelǁchoisir_cible__mutmut_26, 
        'xǁDuelǁchoisir_cible__mutmut_27': xǁDuelǁchoisir_cible__mutmut_27, 
        'xǁDuelǁchoisir_cible__mutmut_28': xǁDuelǁchoisir_cible__mutmut_28, 
        'xǁDuelǁchoisir_cible__mutmut_29': xǁDuelǁchoisir_cible__mutmut_29, 
        'xǁDuelǁchoisir_cible__mutmut_30': xǁDuelǁchoisir_cible__mutmut_30, 
        'xǁDuelǁchoisir_cible__mutmut_31': xǁDuelǁchoisir_cible__mutmut_31
    }
    xǁDuelǁchoisir_cible__mutmut_orig.__name__ = 'xǁDuelǁchoisir_cible'

    def startDuel(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁstartDuel__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁstartDuel__mutmut_mutants'), args, kwargs, self)

    def xǁDuelǁstartDuel__mutmut_orig(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_1(self):

        while self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_2(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = None

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_3(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                None,
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_4(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=None,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_5(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=None
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_6(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_7(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_8(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_9(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: None,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_10(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=False
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_11(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = None

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_12(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                None,
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_13(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=None,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_14(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=None
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_15(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_16(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_17(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_18(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: None,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_19(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=False
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_20(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = None

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_21(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[1],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_22(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[1],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_23(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[2],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_24(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[2]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_25(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_26(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    break

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_27(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant not in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_28(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = None
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_29(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(None, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_30(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, None)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_31(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_32(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, )
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_33(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = None

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_34(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(None, self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_35(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, None)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_36(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_2)

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_37(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, )

                attaquant.attack(cible)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()

    def xǁDuelǁstartDuel__mutmut_38(self):

        while not self.who_wins():

            # Tri agilité
            equipe1_joueurs = sorted(
                [self.perso_1, self.perso_2],
                key=lambda x: x.agilite,
                reverse=True
            )

            equipe2_joueurs = sorted(
                [self.perso_3, self.perso_4],
                key=lambda x: x.agilite,
                reverse=True
            )

            ordre = [
                equipe1_joueurs[0],
                equipe2_joueurs[0],
                equipe1_joueurs[1],
                equipe2_joueurs[1]
            ]

            for attaquant in ordre:

                if not attaquant.is_alive():
                    continue

                # Détermination des cibles
                if attaquant in equipe1_joueurs:
                    cible = self.choisir_cible(self.perso_3, self.perso_4)
                else:
                    cible = self.choisir_cible(self.perso_1, self.perso_2)

                attaquant.attack(None)

                if self.who_wins():
                    return self.who_wins()

        return self.who_wins()
    
    xǁDuelǁstartDuel__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁstartDuel__mutmut_1': xǁDuelǁstartDuel__mutmut_1, 
        'xǁDuelǁstartDuel__mutmut_2': xǁDuelǁstartDuel__mutmut_2, 
        'xǁDuelǁstartDuel__mutmut_3': xǁDuelǁstartDuel__mutmut_3, 
        'xǁDuelǁstartDuel__mutmut_4': xǁDuelǁstartDuel__mutmut_4, 
        'xǁDuelǁstartDuel__mutmut_5': xǁDuelǁstartDuel__mutmut_5, 
        'xǁDuelǁstartDuel__mutmut_6': xǁDuelǁstartDuel__mutmut_6, 
        'xǁDuelǁstartDuel__mutmut_7': xǁDuelǁstartDuel__mutmut_7, 
        'xǁDuelǁstartDuel__mutmut_8': xǁDuelǁstartDuel__mutmut_8, 
        'xǁDuelǁstartDuel__mutmut_9': xǁDuelǁstartDuel__mutmut_9, 
        'xǁDuelǁstartDuel__mutmut_10': xǁDuelǁstartDuel__mutmut_10, 
        'xǁDuelǁstartDuel__mutmut_11': xǁDuelǁstartDuel__mutmut_11, 
        'xǁDuelǁstartDuel__mutmut_12': xǁDuelǁstartDuel__mutmut_12, 
        'xǁDuelǁstartDuel__mutmut_13': xǁDuelǁstartDuel__mutmut_13, 
        'xǁDuelǁstartDuel__mutmut_14': xǁDuelǁstartDuel__mutmut_14, 
        'xǁDuelǁstartDuel__mutmut_15': xǁDuelǁstartDuel__mutmut_15, 
        'xǁDuelǁstartDuel__mutmut_16': xǁDuelǁstartDuel__mutmut_16, 
        'xǁDuelǁstartDuel__mutmut_17': xǁDuelǁstartDuel__mutmut_17, 
        'xǁDuelǁstartDuel__mutmut_18': xǁDuelǁstartDuel__mutmut_18, 
        'xǁDuelǁstartDuel__mutmut_19': xǁDuelǁstartDuel__mutmut_19, 
        'xǁDuelǁstartDuel__mutmut_20': xǁDuelǁstartDuel__mutmut_20, 
        'xǁDuelǁstartDuel__mutmut_21': xǁDuelǁstartDuel__mutmut_21, 
        'xǁDuelǁstartDuel__mutmut_22': xǁDuelǁstartDuel__mutmut_22, 
        'xǁDuelǁstartDuel__mutmut_23': xǁDuelǁstartDuel__mutmut_23, 
        'xǁDuelǁstartDuel__mutmut_24': xǁDuelǁstartDuel__mutmut_24, 
        'xǁDuelǁstartDuel__mutmut_25': xǁDuelǁstartDuel__mutmut_25, 
        'xǁDuelǁstartDuel__mutmut_26': xǁDuelǁstartDuel__mutmut_26, 
        'xǁDuelǁstartDuel__mutmut_27': xǁDuelǁstartDuel__mutmut_27, 
        'xǁDuelǁstartDuel__mutmut_28': xǁDuelǁstartDuel__mutmut_28, 
        'xǁDuelǁstartDuel__mutmut_29': xǁDuelǁstartDuel__mutmut_29, 
        'xǁDuelǁstartDuel__mutmut_30': xǁDuelǁstartDuel__mutmut_30, 
        'xǁDuelǁstartDuel__mutmut_31': xǁDuelǁstartDuel__mutmut_31, 
        'xǁDuelǁstartDuel__mutmut_32': xǁDuelǁstartDuel__mutmut_32, 
        'xǁDuelǁstartDuel__mutmut_33': xǁDuelǁstartDuel__mutmut_33, 
        'xǁDuelǁstartDuel__mutmut_34': xǁDuelǁstartDuel__mutmut_34, 
        'xǁDuelǁstartDuel__mutmut_35': xǁDuelǁstartDuel__mutmut_35, 
        'xǁDuelǁstartDuel__mutmut_36': xǁDuelǁstartDuel__mutmut_36, 
        'xǁDuelǁstartDuel__mutmut_37': xǁDuelǁstartDuel__mutmut_37, 
        'xǁDuelǁstartDuel__mutmut_38': xǁDuelǁstartDuel__mutmut_38
    }
    xǁDuelǁstartDuel__mutmut_orig.__name__ = 'xǁDuelǁstartDuel'