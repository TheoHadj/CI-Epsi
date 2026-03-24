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
    def __init__(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        args = [level, end, force, agi, chn, armor, arme]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁCharacterǁ__init____mutmut_orig(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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


                
    def xǁCharacterǁ__init____mutmut_1(self,level:int=2,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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


                
    def xǁCharacterǁ__init____mutmut_2(self,level:int=1,end:int=1,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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


                
    def xǁCharacterǁ__init____mutmut_3(self,level:int=1,end:int=0,force:int=1, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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


                
    def xǁCharacterǁ__init____mutmut_4(self,level:int=1,end:int=0,force:int=0, agi:int=1, chn:int=0, armor:int = 0,  arme:int=1):
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


                
    def xǁCharacterǁ__init____mutmut_5(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=1, armor:int = 0,  arme:int=1):
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


                
    def xǁCharacterǁ__init____mutmut_6(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 1,  arme:int=1):
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


                
    def xǁCharacterǁ__init____mutmut_7(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=2):
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


                
    def xǁCharacterǁ__init____mutmut_8(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if (0 <= int(armor) <= 100):
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


                
    def xǁCharacterǁ__init____mutmut_9(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (1 <= int(armor) <= 100):
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


                
    def xǁCharacterǁ__init____mutmut_10(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 < int(armor) <= 100):
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


                
    def xǁCharacterǁ__init____mutmut_11(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(None) <= 100):
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


                
    def xǁCharacterǁ__init____mutmut_12(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) < 100):
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


                
    def xǁCharacterǁ__init____mutmut_13(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 101):
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


                
    def xǁCharacterǁ__init____mutmut_14(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError(None)
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


                
    def xǁCharacterǁ__init____mutmut_15(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("XXL'armure doit être comprise entre 0 et 100XX")
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


                
    def xǁCharacterǁ__init____mutmut_16(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("l'armure doit être comprise entre 0 et 100")
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


                
    def xǁCharacterǁ__init____mutmut_17(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'ARMURE DOIT ÊTRE COMPRISE ENTRE 0 ET 100")
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


                
    def xǁCharacterǁ__init____mutmut_18(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme <= 0):
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


                
    def xǁCharacterǁ__init____mutmut_19(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 1):
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


                
    def xǁCharacterǁ__init____mutmut_20(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError(None)
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


                
    def xǁCharacterǁ__init____mutmut_21(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("XXLe multiplicateur d'arme ne peut pas être négatifXX")
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


                
    def xǁCharacterǁ__init____mutmut_22(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("le multiplicateur d'arme ne peut pas être négatif")
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


                
    def xǁCharacterǁ__init____mutmut_23(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("LE MULTIPLICATEUR D'ARME NE PEUT PAS ÊTRE NÉGATIF")
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


                
    def xǁCharacterǁ__init____mutmut_24(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if(level < 0):
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


                
    def xǁCharacterǁ__init____mutmut_25(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if(level<=1):
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


                
    def xǁCharacterǁ__init____mutmut_26(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if(level<=0):
            raise ValueError(None)

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


                
    def xǁCharacterǁ__init____mutmut_27(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if(level<=0):
            raise ValueError("XXLe niveau doit être strictement positifXX")

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


                
    def xǁCharacterǁ__init____mutmut_28(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if(level<=0):
            raise ValueError("le niveau doit être strictement positif")

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


                
    def xǁCharacterǁ__init____mutmut_29(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if(level<=0):
            raise ValueError("LE NIVEAU DOIT ÊTRE STRICTEMENT POSITIF")

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


                
    def xǁCharacterǁ__init____mutmut_30(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if(level<=0):
            raise ValueError("Le niveau doit être strictement positif")

        self.baseHp = None

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


                
    def xǁCharacterǁ__init____mutmut_31(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
        # self.name = name
        # self.hp = hp
        # self.attack_power = attack_power
        if not (0 <= int(armor) <= 100):
            raise ValueError("L'armure doit être comprise entre 0 et 100")
        if (arme < 0):
            raise ValueError("Le multiplicateur d'arme ne peut pas être négatif")
        if(level<=0):
            raise ValueError("Le niveau doit être strictement positif")

        self.baseHp = 11

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


                
    def xǁCharacterǁ__init____mutmut_32(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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

        self.lvl = None
        self.force = force
        self.endurance = end
        self.agi= 0
        self.chn=0
        #la chance marche comme suis => chaque tour quelqu'un esquive forcément parmis les chance une et tiré
        self.hp = self.baseHp + self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_33(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.force = None
        self.endurance = end
        self.agi= 0
        self.chn=0
        #la chance marche comme suis => chaque tour quelqu'un esquive forcément parmis les chance une et tiré
        self.hp = self.baseHp + self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_34(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.endurance = None
        self.agi= 0
        self.chn=0
        #la chance marche comme suis => chaque tour quelqu'un esquive forcément parmis les chance une et tiré
        self.hp = self.baseHp + self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_35(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.agi= None
        self.chn=0
        #la chance marche comme suis => chaque tour quelqu'un esquive forcément parmis les chance une et tiré
        self.hp = self.baseHp + self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_36(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.agi= 1
        self.chn=0
        #la chance marche comme suis => chaque tour quelqu'un esquive forcément parmis les chance une et tiré
        self.hp = self.baseHp + self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_37(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.chn=None
        #la chance marche comme suis => chaque tour quelqu'un esquive forcément parmis les chance une et tiré
        self.hp = self.baseHp + self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_38(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.chn=1
        #la chance marche comme suis => chaque tour quelqu'un esquive forcément parmis les chance une et tiré
        self.hp = self.baseHp + self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_39(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.hp = None
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_40(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.hp = self.baseHp + self.endurance - 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_41(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.hp = self.baseHp - self.endurance + 2*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_42(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.hp = self.baseHp + self.endurance + 2 / self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_43(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.hp = self.baseHp + self.endurance + 3*self.lvl
        self.armor = armor        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_44(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.armor = None        
        self.arme = arme

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_45(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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
        self.arme = None

        self.maxHp = self.baseHp + self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_46(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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

        self.maxHp = None


                
    def xǁCharacterǁ__init____mutmut_47(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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

        self.maxHp = self.baseHp + self.endurance - 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_48(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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

        self.maxHp = self.baseHp - self.endurance + 2*self.lvl


                
    def xǁCharacterǁ__init____mutmut_49(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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

        self.maxHp = self.baseHp + self.endurance + 2 / self.lvl


                
    def xǁCharacterǁ__init____mutmut_50(self,level:int=1,end:int=0,force:int=0, agi:int=0, chn:int=0, armor:int = 0,  arme:int=1):
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

        self.maxHp = self.baseHp + self.endurance + 3*self.lvl


                
    
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
        'xǁCharacterǁ__init____mutmut_37': xǁCharacterǁ__init____mutmut_37, 
        'xǁCharacterǁ__init____mutmut_38': xǁCharacterǁ__init____mutmut_38, 
        'xǁCharacterǁ__init____mutmut_39': xǁCharacterǁ__init____mutmut_39, 
        'xǁCharacterǁ__init____mutmut_40': xǁCharacterǁ__init____mutmut_40, 
        'xǁCharacterǁ__init____mutmut_41': xǁCharacterǁ__init____mutmut_41, 
        'xǁCharacterǁ__init____mutmut_42': xǁCharacterǁ__init____mutmut_42, 
        'xǁCharacterǁ__init____mutmut_43': xǁCharacterǁ__init____mutmut_43, 
        'xǁCharacterǁ__init____mutmut_44': xǁCharacterǁ__init____mutmut_44, 
        'xǁCharacterǁ__init____mutmut_45': xǁCharacterǁ__init____mutmut_45, 
        'xǁCharacterǁ__init____mutmut_46': xǁCharacterǁ__init____mutmut_46, 
        'xǁCharacterǁ__init____mutmut_47': xǁCharacterǁ__init____mutmut_47, 
        'xǁCharacterǁ__init____mutmut_48': xǁCharacterǁ__init____mutmut_48, 
        'xǁCharacterǁ__init____mutmut_49': xǁCharacterǁ__init____mutmut_49, 
        'xǁCharacterǁ__init____mutmut_50': xǁCharacterǁ__init____mutmut_50
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
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) * self.arme)

    def xǁCharacterǁattack__mutmut_1(self, target):
        if self.is_alive():
            target.take_damage(None)

    def xǁCharacterǁattack__mutmut_2(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force + 1 + 2*self.lvl) / self.arme)

    def xǁCharacterǁattack__mutmut_3(self, target):
        if self.is_alive():
            target.take_damage(random.randint(None, self.force + 1 + 2*self.lvl) * self.arme)

    def xǁCharacterǁattack__mutmut_4(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, None) * self.arme)

    def xǁCharacterǁattack__mutmut_5(self, target):
        if self.is_alive():
            target.take_damage(random.randint(self.force + 1 + 2*self.lvl) * self.arme)

    def xǁCharacterǁattack__mutmut_6(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, ) * self.arme)

    def xǁCharacterǁattack__mutmut_7(self, target):
        if self.is_alive():
            target.take_damage(random.randint(1, self.force + 1 + 2*self.lvl) * self.arme)

    def xǁCharacterǁattack__mutmut_8(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force + 1 - 2*self.lvl) * self.arme)

    def xǁCharacterǁattack__mutmut_9(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force - 1 + 2*self.lvl) * self.arme)

    def xǁCharacterǁattack__mutmut_10(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force + 2 + 2*self.lvl) * self.arme)

    def xǁCharacterǁattack__mutmut_11(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force + 1 + 2 / self.lvl) * self.arme)

    def xǁCharacterǁattack__mutmut_12(self, target):
        if self.is_alive():
            target.take_damage(random.randint(0, self.force + 1 + 3*self.lvl) * self.arme)
    
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
        'xǁCharacterǁattack__mutmut_12': xǁCharacterǁattack__mutmut_12
    }
    xǁCharacterǁattack__mutmut_orig.__name__ = 'xǁCharacterǁattack'
    
    def levelUp(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCharacterǁlevelUp__mutmut_orig'), object.__getattribute__(self, 'xǁCharacterǁlevelUp__mutmut_mutants'), args, kwargs, self)
    
    def xǁCharacterǁlevelUp__mutmut_orig(self): #doesn't exists
        self.lvl += 1
        
        
    
    def xǁCharacterǁlevelUp__mutmut_1(self): #doesn't exists
        self.lvl = 1
        
        
    
    def xǁCharacterǁlevelUp__mutmut_2(self): #doesn't exists
        self.lvl -= 1
        
        
    
    def xǁCharacterǁlevelUp__mutmut_3(self): #doesn't exists
        self.lvl += 2
        
        
    
    xǁCharacterǁlevelUp__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCharacterǁlevelUp__mutmut_1': xǁCharacterǁlevelUp__mutmut_1, 
        'xǁCharacterǁlevelUp__mutmut_2': xǁCharacterǁlevelUp__mutmut_2, 
        'xǁCharacterǁlevelUp__mutmut_3': xǁCharacterǁlevelUp__mutmut_3
    }
    xǁCharacterǁlevelUp__mutmut_orig.__name__ = 'xǁCharacterǁlevelUp'
class Equipe:
    def __init__(self, perso1:Character, perso2:Character):
        args = [perso1, perso2]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁEquipeǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁEquipeǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁEquipeǁ__init____mutmut_orig(self, perso1:Character, perso2:Character):
        self.perso1 = perso1
        self.perso2 = perso2
    def xǁEquipeǁ__init____mutmut_1(self, perso1:Character, perso2:Character):
        self.perso1 = None
        self.perso2 = perso2
    def xǁEquipeǁ__init____mutmut_2(self, perso1:Character, perso2:Character):
        self.perso1 = perso1
        self.perso2 = None
    
    xǁEquipeǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁEquipeǁ__init____mutmut_1': xǁEquipeǁ__init____mutmut_1, 
        'xǁEquipeǁ__init____mutmut_2': xǁEquipeǁ__init____mutmut_2
    }
    xǁEquipeǁ__init____mutmut_orig.__name__ = 'xǁEquipeǁ__init__'

    def isAlive(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁEquipeǁisAlive__mutmut_orig'), object.__getattribute__(self, 'xǁEquipeǁisAlive__mutmut_mutants'), args, kwargs, self)

    def xǁEquipeǁisAlive__mutmut_orig(self):
        if self.perso_1.hp==0 and self.perso_2.hp==0:
            return False
        else:
            return True

    def xǁEquipeǁisAlive__mutmut_1(self):
        if self.perso_1.hp==0 or self.perso_2.hp==0:
            return False
        else:
            return True

    def xǁEquipeǁisAlive__mutmut_2(self):
        if self.perso_1.hp != 0 and self.perso_2.hp==0:
            return False
        else:
            return True

    def xǁEquipeǁisAlive__mutmut_3(self):
        if self.perso_1.hp==1 and self.perso_2.hp==0:
            return False
        else:
            return True

    def xǁEquipeǁisAlive__mutmut_4(self):
        if self.perso_1.hp==0 and self.perso_2.hp != 0:
            return False
        else:
            return True

    def xǁEquipeǁisAlive__mutmut_5(self):
        if self.perso_1.hp==0 and self.perso_2.hp==1:
            return False
        else:
            return True

    def xǁEquipeǁisAlive__mutmut_6(self):
        if self.perso_1.hp==0 and self.perso_2.hp==0:
            return True
        else:
            return True

    def xǁEquipeǁisAlive__mutmut_7(self):
        if self.perso_1.hp==0 and self.perso_2.hp==0:
            return False
        else:
            return False
    
    xǁEquipeǁisAlive__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁEquipeǁisAlive__mutmut_1': xǁEquipeǁisAlive__mutmut_1, 
        'xǁEquipeǁisAlive__mutmut_2': xǁEquipeǁisAlive__mutmut_2, 
        'xǁEquipeǁisAlive__mutmut_3': xǁEquipeǁisAlive__mutmut_3, 
        'xǁEquipeǁisAlive__mutmut_4': xǁEquipeǁisAlive__mutmut_4, 
        'xǁEquipeǁisAlive__mutmut_5': xǁEquipeǁisAlive__mutmut_5, 
        'xǁEquipeǁisAlive__mutmut_6': xǁEquipeǁisAlive__mutmut_6, 
        'xǁEquipeǁisAlive__mutmut_7': xǁEquipeǁisAlive__mutmut_7
    }
    xǁEquipeǁisAlive__mutmut_orig.__name__ = 'xǁEquipeǁisAlive'
    
    def whoLowest(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁEquipeǁwhoLowest__mutmut_orig'), object.__getattribute__(self, 'xǁEquipeǁwhoLowest__mutmut_mutants'), args, kwargs, self)
    
    def xǁEquipeǁwhoLowest__mutmut_orig(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_1(self):
        if(self.perso1.hp * self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_2(self):
        if(self.perso1.hp/self.perso1.maxHp >= self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_3(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp * self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_4(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp * self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_5(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp <= self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_6(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp * self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_7(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(None, 2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_8(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, None) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_9(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_10(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, ) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_11(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(2, 2) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_12(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 3) ==1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_13(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) != 1):
                return self.perso1
            else:
                return self.perso2
    
    def xǁEquipeǁwhoLowest__mutmut_14(self):
        if(self.perso1.hp/self.perso1.maxHp > self.perso2.hp/self.perso2.maxHp):
            return self.perso2
        elif(self.perso1.hp/self.perso1.maxHp < self.perso2.hp/self.perso2.maxHp):
            return self.perso1
        else:
            if(random.randint(1, 2) ==2):
                return self.perso1
            else:
                return self.perso2
    
    xǁEquipeǁwhoLowest__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁEquipeǁwhoLowest__mutmut_1': xǁEquipeǁwhoLowest__mutmut_1, 
        'xǁEquipeǁwhoLowest__mutmut_2': xǁEquipeǁwhoLowest__mutmut_2, 
        'xǁEquipeǁwhoLowest__mutmut_3': xǁEquipeǁwhoLowest__mutmut_3, 
        'xǁEquipeǁwhoLowest__mutmut_4': xǁEquipeǁwhoLowest__mutmut_4, 
        'xǁEquipeǁwhoLowest__mutmut_5': xǁEquipeǁwhoLowest__mutmut_5, 
        'xǁEquipeǁwhoLowest__mutmut_6': xǁEquipeǁwhoLowest__mutmut_6, 
        'xǁEquipeǁwhoLowest__mutmut_7': xǁEquipeǁwhoLowest__mutmut_7, 
        'xǁEquipeǁwhoLowest__mutmut_8': xǁEquipeǁwhoLowest__mutmut_8, 
        'xǁEquipeǁwhoLowest__mutmut_9': xǁEquipeǁwhoLowest__mutmut_9, 
        'xǁEquipeǁwhoLowest__mutmut_10': xǁEquipeǁwhoLowest__mutmut_10, 
        'xǁEquipeǁwhoLowest__mutmut_11': xǁEquipeǁwhoLowest__mutmut_11, 
        'xǁEquipeǁwhoLowest__mutmut_12': xǁEquipeǁwhoLowest__mutmut_12, 
        'xǁEquipeǁwhoLowest__mutmut_13': xǁEquipeǁwhoLowest__mutmut_13, 
        'xǁEquipeǁwhoLowest__mutmut_14': xǁEquipeǁwhoLowest__mutmut_14
    }
    xǁEquipeǁwhoLowest__mutmut_orig.__name__ = 'xǁEquipeǁwhoLowest'

class Duel:
    def __init__(self, equipe1:Equipe, equipe2:Equipe):
        args = [equipe1, equipe2]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁDuelǁ__init____mutmut_orig(self, equipe1:Equipe, equipe2:Equipe):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        
    def xǁDuelǁ__init____mutmut_1(self, equipe1:Equipe, equipe2:Equipe):
        self.equipe1 = None
        self.equipe2 = equipe2
        
    def xǁDuelǁ__init____mutmut_2(self, equipe1:Equipe, equipe2:Equipe):
        self.equipe1 = equipe1
        self.equipe2 = None
        
    
    xǁDuelǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁ__init____mutmut_1': xǁDuelǁ__init____mutmut_1, 
        'xǁDuelǁ__init____mutmut_2': xǁDuelǁ__init____mutmut_2
    }
    xǁDuelǁ__init____mutmut_orig.__name__ = 'xǁDuelǁ__init__'
    def fight(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁfight__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁfight__mutmut_mutants'), args, kwargs, self)
    def xǁDuelǁfight__mutmut_orig(self):

        while(self.equipe1.isAlive==False or self.equipe2.isAlive==False):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_1(self):

        while(self.equipe1.isAlive==False and self.equipe2.isAlive==False):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_2(self):

        while(self.equipe1.isAlive != False or self.equipe2.isAlive==False):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_3(self):

        while(self.equipe1.isAlive==True or self.equipe2.isAlive==False):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_4(self):

        while(self.equipe1.isAlive==False or self.equipe2.isAlive != False):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_5(self):

        while(self.equipe1.isAlive==False or self.equipe2.isAlive==True):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_6(self):

        while(self.equipe1.isAlive==False or self.equipe2.isAlive==False):
            order= None
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_7(self):

        while(self.equipe1.isAlive==False or self.equipe2.isAlive==False):
            order= self.getOrder()
            for p in order:
                p.attack(None)
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_8(self):

        while(self.equipe1.isAlive==False or self.equipe2.isAlive==False):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(None).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_9(self):

        while(self.equipe1.isAlive==False or self.equipe2.isAlive==False):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 2
        else:
            return 2
        
    def xǁDuelǁfight__mutmut_10(self):

        while(self.equipe1.isAlive==False or self.equipe2.isAlive==False):
            order= self.getOrder()
            for p in order:
                p.attack(self.get_enemy_team(p).whoLowest())
       
        if(self.equipe1.isAlive):
            return 1
        else:
            return 3
        
    
    xǁDuelǁfight__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁfight__mutmut_1': xǁDuelǁfight__mutmut_1, 
        'xǁDuelǁfight__mutmut_2': xǁDuelǁfight__mutmut_2, 
        'xǁDuelǁfight__mutmut_3': xǁDuelǁfight__mutmut_3, 
        'xǁDuelǁfight__mutmut_4': xǁDuelǁfight__mutmut_4, 
        'xǁDuelǁfight__mutmut_5': xǁDuelǁfight__mutmut_5, 
        'xǁDuelǁfight__mutmut_6': xǁDuelǁfight__mutmut_6, 
        'xǁDuelǁfight__mutmut_7': xǁDuelǁfight__mutmut_7, 
        'xǁDuelǁfight__mutmut_8': xǁDuelǁfight__mutmut_8, 
        'xǁDuelǁfight__mutmut_9': xǁDuelǁfight__mutmut_9, 
        'xǁDuelǁfight__mutmut_10': xǁDuelǁfight__mutmut_10
    }
    xǁDuelǁfight__mutmut_orig.__name__ = 'xǁDuelǁfight'
    def getOrder(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁgetOrder__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁgetOrder__mutmut_mutants'), args, kwargs, self)
    def xǁDuelǁgetOrder__mutmut_orig(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_1(self):
        tous_les_combattants = None
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_2(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = None
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_3(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(None, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_4(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=None)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_5(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_6(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, )
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_7(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: None)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_8(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = None
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_9(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 not in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_10(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = None
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_11(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante != self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_12(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = None            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_13(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max(None, key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_14(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=None)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_15(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max(key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_16(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], )            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_17(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: None)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_18(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = None
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_19(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 != eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 == eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_20(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = None

        return [p1, p2, p3, p4]
    def xǁDuelǁgetOrder__mutmut_21(self):
        tous_les_combattants = [
        self.equipe1.perso1, self.equipe1.perso2,
        self.equipe2.perso1, self.equipe2.perso2
        ]
                
        p1 = max(tous_les_combattants, key=lambda p: p.agi)
        eq_attaquante = self.equipe1 if p1 in [self.equipe1.perso1, self.equipe1.perso2] else self.equipe2
        eq_adverse = self.equipe2 if eq_attaquante == self.equipe1 else self.equipe1
        p2 = max([eq_adverse.perso1, eq_adverse.perso2], key=lambda p: p.agi)            
        p3 = eq_attaquante.perso2 if p1 == eq_attaquante.perso1 else eq_attaquante.perso1
        p4 = eq_adverse.perso2 if p2 != eq_adverse.perso1 else eq_adverse.perso1

        return [p1, p2, p3, p4]
    
    xǁDuelǁgetOrder__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁgetOrder__mutmut_1': xǁDuelǁgetOrder__mutmut_1, 
        'xǁDuelǁgetOrder__mutmut_2': xǁDuelǁgetOrder__mutmut_2, 
        'xǁDuelǁgetOrder__mutmut_3': xǁDuelǁgetOrder__mutmut_3, 
        'xǁDuelǁgetOrder__mutmut_4': xǁDuelǁgetOrder__mutmut_4, 
        'xǁDuelǁgetOrder__mutmut_5': xǁDuelǁgetOrder__mutmut_5, 
        'xǁDuelǁgetOrder__mutmut_6': xǁDuelǁgetOrder__mutmut_6, 
        'xǁDuelǁgetOrder__mutmut_7': xǁDuelǁgetOrder__mutmut_7, 
        'xǁDuelǁgetOrder__mutmut_8': xǁDuelǁgetOrder__mutmut_8, 
        'xǁDuelǁgetOrder__mutmut_9': xǁDuelǁgetOrder__mutmut_9, 
        'xǁDuelǁgetOrder__mutmut_10': xǁDuelǁgetOrder__mutmut_10, 
        'xǁDuelǁgetOrder__mutmut_11': xǁDuelǁgetOrder__mutmut_11, 
        'xǁDuelǁgetOrder__mutmut_12': xǁDuelǁgetOrder__mutmut_12, 
        'xǁDuelǁgetOrder__mutmut_13': xǁDuelǁgetOrder__mutmut_13, 
        'xǁDuelǁgetOrder__mutmut_14': xǁDuelǁgetOrder__mutmut_14, 
        'xǁDuelǁgetOrder__mutmut_15': xǁDuelǁgetOrder__mutmut_15, 
        'xǁDuelǁgetOrder__mutmut_16': xǁDuelǁgetOrder__mutmut_16, 
        'xǁDuelǁgetOrder__mutmut_17': xǁDuelǁgetOrder__mutmut_17, 
        'xǁDuelǁgetOrder__mutmut_18': xǁDuelǁgetOrder__mutmut_18, 
        'xǁDuelǁgetOrder__mutmut_19': xǁDuelǁgetOrder__mutmut_19, 
        'xǁDuelǁgetOrder__mutmut_20': xǁDuelǁgetOrder__mutmut_20, 
        'xǁDuelǁgetOrder__mutmut_21': xǁDuelǁgetOrder__mutmut_21
    }
    xǁDuelǁgetOrder__mutmut_orig.__name__ = 'xǁDuelǁgetOrder'
    
    def get_enemy_team(self, character):
        args = [character]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁget_enemy_team__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁget_enemy_team__mutmut_mutants'), args, kwargs, self)
    
    def xǁDuelǁget_enemy_team__mutmut_orig(self, character):
        return self.equipe2 if character in (self.equipe1.perso1, self.equipe1.perso2) else self.equipe1
    
    def xǁDuelǁget_enemy_team__mutmut_1(self, character):
        return self.equipe2 if character not in (self.equipe1.perso1, self.equipe1.perso2) else self.equipe1
    
    xǁDuelǁget_enemy_team__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁget_enemy_team__mutmut_1': xǁDuelǁget_enemy_team__mutmut_1
    }
    xǁDuelǁget_enemy_team__mutmut_orig.__name__ = 'xǁDuelǁget_enemy_team'
    
    def get_enemy_team(self, character):
        args = [character]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDuelǁget_enemy_team__mutmut_orig'), object.__getattribute__(self, 'xǁDuelǁget_enemy_team__mutmut_mutants'), args, kwargs, self)
    
    def xǁDuelǁget_enemy_team__mutmut_orig(self, character):
        return self.equipe2 if character in (self.equipe1.perso1, self.equipe1.perso2) else self.equipe1
    
    def xǁDuelǁget_enemy_team__mutmut_1(self, character):
        return self.equipe2 if character not in (self.equipe1.perso1, self.equipe1.perso2) else self.equipe1
    
    xǁDuelǁget_enemy_team__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDuelǁget_enemy_team__mutmut_1': xǁDuelǁget_enemy_team__mutmut_1
    }
    xǁDuelǁget_enemy_team__mutmut_orig.__name__ = 'xǁDuelǁget_enemy_team'