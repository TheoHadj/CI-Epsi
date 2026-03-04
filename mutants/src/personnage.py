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
class Personnage:
    def __init__(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPersonnageǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁPersonnageǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁPersonnageǁ__init____mutmut_orig(self):
        self.points_de_vie = 10
        
    def xǁPersonnageǁ__init____mutmut_1(self):
        self.points_de_vie = None
        
    def xǁPersonnageǁ__init____mutmut_2(self):
        self.points_de_vie = 11
        
    
    xǁPersonnageǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPersonnageǁ__init____mutmut_1': xǁPersonnageǁ__init____mutmut_1, 
        'xǁPersonnageǁ__init____mutmut_2': xǁPersonnageǁ__init____mutmut_2
    }
    xǁPersonnageǁ__init____mutmut_orig.__name__ = 'xǁPersonnageǁ__init__'
    def get_points_vie(self):
        return self.points_de_vie

    def est_vivant(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPersonnageǁest_vivant__mutmut_orig'), object.__getattribute__(self, 'xǁPersonnageǁest_vivant__mutmut_mutants'), args, kwargs, self)

    def xǁPersonnageǁest_vivant__mutmut_orig(self):
        return self.points_de_vie > 0

    def xǁPersonnageǁest_vivant__mutmut_1(self):
        return self.points_de_vie >= 0

    def xǁPersonnageǁest_vivant__mutmut_2(self):
        return self.points_de_vie > 1
    
    xǁPersonnageǁest_vivant__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPersonnageǁest_vivant__mutmut_1': xǁPersonnageǁest_vivant__mutmut_1, 
        'xǁPersonnageǁest_vivant__mutmut_2': xǁPersonnageǁest_vivant__mutmut_2
    }
    xǁPersonnageǁest_vivant__mutmut_orig.__name__ = 'xǁPersonnageǁest_vivant'
    
    def subir_degats(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPersonnageǁsubir_degats__mutmut_orig'), object.__getattribute__(self, 'xǁPersonnageǁsubir_degats__mutmut_mutants'), args, kwargs, self)
    
    def xǁPersonnageǁsubir_degats__mutmut_orig(self):
        self.points_de_vie -= 1
    
    def xǁPersonnageǁsubir_degats__mutmut_1(self):
        self.points_de_vie = 1
    
    def xǁPersonnageǁsubir_degats__mutmut_2(self):
        self.points_de_vie += 1
    
    def xǁPersonnageǁsubir_degats__mutmut_3(self):
        self.points_de_vie -= 2
    
    xǁPersonnageǁsubir_degats__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPersonnageǁsubir_degats__mutmut_1': xǁPersonnageǁsubir_degats__mutmut_1, 
        'xǁPersonnageǁsubir_degats__mutmut_2': xǁPersonnageǁsubir_degats__mutmut_2, 
        'xǁPersonnageǁsubir_degats__mutmut_3': xǁPersonnageǁsubir_degats__mutmut_3
    }
    xǁPersonnageǁsubir_degats__mutmut_orig.__name__ = 'xǁPersonnageǁsubir_degats'