from unittest.mock import patch
from test.utils.PersonnageBuilder import CharacterBuilder

def test_reduction_degats_par_armure():
    # ETANT DONNE une victime avec 50% d'armure et 12 PV
    victime = CharacterBuilder().with_armor(50).with_lvl(1).with_endurance(0).build()
    pv_initiaux = victime.hp
    
    # QUAND elle subit 10 points de dégâts bruts
    victime.take_damage(10)
    
    # ALORS elle ne perd que 5 PV (10 * 0.5)
    assert victime.hp == pv_initiaux - 5

def test_immunite_armure_cent_pour_cent():
    # ETANT DONNE une victime avec 100% d'armure
    victime = CharacterBuilder().with_armor(100).build()
    pv_initiaux = victime.hp
    
    # QUAND elle subit 100 points de dégâts
    victime.take_damage(100)
    
    # ALORS ses PV ne changent pas
    assert victime.hp == pv_initiaux

def test_degats_aleatoires_bornes():
    # ETANT DONNE un attaquant niveau 1 (force 0)
    attaquant = CharacterBuilder().with_lvl(1).with_force(0).build()
    victime = CharacterBuilder().build()
    
    # QUAND il attaque avec un jet de dé fixé au maximum (randint = force + 1 + 2*lvl = 3)
    with patch('random.randint', return_value=3):
        attaquant.attack(victime)
        
    # ALORS la victime perd exactement 3 PV
    assert victime.hp == victime.maxHp - 3

def test_mort_personnage():
    # ETANT DONNE un personnage avec 12 PV
    perso = CharacterBuilder().with_lvl(1).build()
    
    # QUAND il subit des dégâts supérieurs à sa vie
    perso.take_damage(20)
    
    # ALORS ses PV tombent à 0 et il est considéré comme mort
    assert perso.hp == 0
    assert not perso.is_alive()